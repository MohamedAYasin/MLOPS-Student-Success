# Preprocessing

# Import Libraries
import os
import pickle
import joblib
import numpy as np
import pandas as pd
from sklearn import preprocessing
import seaborn as sns
import matplotlib.pyplot as plt
from google.colab import drive, files

# Connect to Google Drive
drive.mount('/content/drive')

# Load the dataset
file_path = '/content/drive/My Drive/student-data.csv'
df = pd.read_csv(file_path)

# check the new information to see if there is any missing values
df.isnull().sum()

# a description of the dataset
df.describe()

# Rounding all the float values present inside the dataset into its nearest number
df = df.round()

# Converting all the floating values to integers
df[['Admission grade', 'Previous qualification (grade)',
    'Curricular units 1st sem (grade)', 'Curricular units 2nd sem (grade)',
    'Unemployment rate', 'Inflation rate', 'GDP']] = df[[
    'Admission grade', 'Previous qualification (grade)',
    'Curricular units 1st sem (grade)', 'Curricular units 2nd sem (grade)',
    'Unemployment rate', 'Inflation rate', 'GDP']].astype(np.int64)

# Dropping all unneeded columns
df = df.drop(columns=['Application mode', 'Application order', 'International',
                      'Debtor', 'Marital status', 'Displaced', 'Nacionality',
                      'Father\'s qualification', 'Mother\'s qualification',
                      'Father\'s occupation', 'Mother\'s occupation',
                      'Unemployment rate', 'Inflation rate', 'GDP'], axis=1)

# Changing 'Dropout' to 0, 'Graduate' to 1, and 'Enrolled' to 2 in 'Target' column
df = df.replace({'Target': {'Dropout': 0, 'Graduate': 1, 'Enrolled': 2}})

# Visualizing the total number of students: dropout (0), graduate (1), enrolled (2)
sns.set(rc={'figure.figsize': (12, 6)})
sns.countplot(x=df['Target'], palette=['#FF5733', '#33FF57', '#3357FF'])
plt.title('Distribution of Target Variable')
plt.xlabel('Target (Dropout: 0, Graduate: 1, Enrolled: 2)')
plt.ylabel('Count')
plt.show()

# Save processed data to CSV
preprocessing = '/content/student_success_data.csv'
df.to_csv(preprocessing, index=False)
files.download(preprocessing)
