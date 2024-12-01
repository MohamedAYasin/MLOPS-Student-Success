import os
import pickle
import pandas as pd
from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.responses import FileResponse
from pydantic import BaseModel, create_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from starlette.middleware.cors import CORSMiddleware

# Define FastAPI app
app = FastAPI()

# Allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Paths to model and encoder files
MODEL_PATH = "student-predictor.pkl"
ENCODER_PATH = "label-encoder.pkl"
TRAIN_CSV_PATH = "X_train_standardized.csv"
TEST_CSV_PATH = "X_test_standardized.csv"

# Global variables for the model and label encoder
global model, label_encoder

# Load the model and label encoder
def load_model_and_encoder():
    try:
        with open(MODEL_PATH, "rb") as model_file:
            loaded_model = pickle.load(model_file)
        with open(ENCODER_PATH, "rb") as encoder_file:
            loaded_encoder = pickle.load(encoder_file)
        return loaded_model, loaded_encoder
    except FileNotFoundError:
        raise RuntimeError(f"Model or encoder file not found at {MODEL_PATH} or {ENCODER_PATH}.")

model, label_encoder = load_model_and_encoder()

# Load standardized training data to get feature names
try:
    standardized_train_data = pd.read_csv(TRAIN_CSV_PATH)
    feature_columns = standardized_train_data.columns.tolist()
except FileNotFoundError:
    raise RuntimeError(f"Standardized train CSV file not found at {TRAIN_CSV_PATH}.")

# Dynamically create Pydantic model for the input data
StudentData = create_model(
    "StudentData",
    **{col: (float, ...) for col in feature_columns}  # All fields are required and of type float
)

@app.post("/predict/")
def predict_student_status(data: StudentData):
    """Predict student status using the trained model."""
    try:
        # Convert input data to DataFrame
        input_data = pd.DataFrame([data.dict()])
        input_data = input_data.reindex(columns=feature_columns, fill_value=0)

        # Make prediction
        prediction = model.predict(input_data)
        predicted_status = label_encoder.inverse_transform(prediction)

        return {"predicted_status": predicted_status[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

@app.post("/retrain/")
def retrain_model(file: UploadFile = File(...)):
    """Retrain the model with new data."""
    global model, label_encoder
    try:
        # Load new dataset
        new_data = pd.read_csv(file.file)
        if "Target" not in new_data.columns:
            raise HTTPException(status_code=400, detail="Dataset must include 'Target' column.")

        # Separate features and target
        X = new_data.drop("Target", axis=1)
        y = new_data["Target"]

        # Align features with the model
        X = X.reindex(columns=feature_columns, fill_value=0)

        # Encode target labels
        y_encoded = label_encoder.transform(y)

        # Split data into train and test sets
        trainX, testX, trainY, testY = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

        # Retrain the model
        model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight="balanced")
        model.fit(trainX, trainY)

        # Evaluate the model
        accuracy = accuracy_score(testY, model.predict(testX))
        report = classification_report(testY, model.predict(testX), target_names=label_encoder.classes_)

        # Save the retrained model
        with open(MODEL_PATH, "wb") as model_file:
            pickle.dump(model, model_file)

        return {"message": "Asante! Model retrained successfully", "accuracy": accuracy, "classification_report": report}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Sorry! Retraining failed: {str(e)}")

@app.get("/download_model/")
def download_model():
    """Download the retrained model."""
    if not os.path.exists(MODEL_PATH):
        raise HTTPException(status_code=404, detail="Model file not found.")
    return FileResponse(MODEL_PATH, media_type="application/octet-stream", filename="student-predictor.pkl")

@app.get("/")
def root():
    """Root endpoint."""
    return {"message": "Karibu! Welcome to the Student Dropout and Success Prediction API"}
