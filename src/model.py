# Model

#Import Libraries
import os
import pickle
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf
from google.colab import drive, files
from matplotlib import pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers, regularizers
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, confusion_matrix, classification_report)

# Connect to Google Drive
drive.mount('/content/drive')

# Load the dataset
file_path = '/content/drive/My Drive/student-data.csv'
df = pd.read_csv(file_path)

# Define Features and Labels
X = df.drop(columns='Target', axis=1)  # Features
y = df['Target']                      # Labels

# Map string labels to integers
label_mapping = {'Dropout': 0, 'Graduate': 1, 'Enrolled': 2}
y = y.map(label_mapping)

# Split the Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the Data
scaler = StandardScaler()
X_train = pd.DataFrame(scaler.fit_transform(X_train), columns=X_train.columns)
X_test = pd.DataFrame(scaler.transform(X_test), columns=X_test.columns)

# Save Preprocessed Data
os.makedirs('/content/data/train', exist_ok=True)
os.makedirs('/content/data/test', exist_ok=True)

X_train.to_csv('/content/data/train/X_train_standardized.csv', index=False)
y_train.to_csv('/content/data/train/y_train.csv', index=False)
X_test.to_csv('/content/data/test/X_test_standardized.csv', index=False)
y_test.to_csv('/content/data/test/y_test.csv', index=False)

# Download the saved files
print("Downloading train files...")
files.download('/content/data/train/X_train_standardized.csv')
files.download('/content/data/train/y_train.csv')

print("Downloading test files...")
files.download('/content/data/test/X_test_standardized.csv')
files.download('/content/data/test/y_test.csv')

# Define the Neural Network Model
model = Sequential([
    layers.InputLayer(input_shape=(X_train.shape[1],)),
    layers.Dense(128, activation='relu', kernel_regularizer=regularizers.l2(0.001)),
    layers.BatchNormalization(),
    layers.Dropout(0.5),
    layers.Dense(128, activation='relu', kernel_regularizer=regularizers.l2(0.001)),
    layers.BatchNormalization(),
    layers.Dropout(0.5),
    layers.Dense(128, activation='relu', kernel_regularizer=regularizers.l2(0.001)),
    layers.BatchNormalization(),
    layers.Dropout(0.5),
    layers.Dense(3, activation='softmax')  # Used softmax for multi-class classification
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',  # Used sparse_categorical_crossentropy for multi-class labels
              metrics=['accuracy'])

model.summary()

# Define Callbacks
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
lr_scheduler = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=3, min_lr=1e-6)

# Train the Model
history = model.fit(
    X_train, y_train,
    epochs=80,
    batch_size=32,
    validation_split=0.2,
    callbacks=[early_stopping, lr_scheduler]
)

# Evaluate the Model
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"Test Loss: {test_loss}")
print(f"Test Accuracy: {test_accuracy}")

# Predict on the Test Set
y_pred_prob = model.predict(X_test)
y_pred = np.argmax(y_pred_prob, axis=1)

# Calculate Metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)

print("\nModel Evaluation Metrics:")
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")

# Classification Report
class_labels = ['Dropout', 'Graduate', 'Enrolled']
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=class_labels, zero_division=0))

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)

# Visualize Confusion Matrix
plt.figure(figsize=(10, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Reds',
            xticklabels=class_labels, yticklabels=class_labels)
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.show()

# Random Forest Classifier as Comparison
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_y_pred = rf_model.predict(X_test)

# Evaluate Random Forest
rf_accuracy = accuracy_score(y_test, rf_y_pred)
rf_precision = precision_score(y_test, rf_y_pred, average='weighted', zero_division=0)
rf_recall = recall_score(y_test, rf_y_pred, average='weighted', zero_division=0)
rf_f1 = f1_score(y_test, rf_y_pred, average='weighted', zero_division=0)

print("\nRandom Forest Evaluation Metrics:")
print(f"Accuracy: {rf_accuracy:.4f}")
print(f"Precision: {rf_precision:.4f}")
print(f"Recall: {rf_recall:.4f}")
print(f"F1 Score: {rf_f1:.4f}")

# Save Random Forest Model
os.makedirs('./model', exist_ok=True)
with open('./model/student-predictor.pkl', 'wb') as f:
    pickle.dump(rf_model, f)
files.download('./model/student-predictor.pkl')
