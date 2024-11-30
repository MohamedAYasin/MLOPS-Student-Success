import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load the scaler parameters
scaler_params = pd.read_csv('scaler.csv')  # Ensure this file has 'feature', 'mean', and 'std' columns
feature_means = scaler_params['mean'].values
feature_stds = scaler_params['std'].values

# Load the trained Random Forest model
model = joblib.load('student-predictor.pkl')

# Streamlit app title
st.title("Student Dropout Prediction")
st.write(
    """
    Predict the likelihood of a student dropping out, continuing their studies, or graduating based on academic, demographic, and socio-economic factors.
    """
)

# Input fields
st.header("Enter Student Features:")
features = {
    "Course": st.number_input("Course (ID)", min_value=1),
    "Daytime/evening attendance": st.selectbox("Daytime or Evening Attendance", [0, 1]),
    "Previous qualification": st.selectbox("Previous Qualification (0 = None, 1 = Yes)", [0, 1]),
    "Previous qualification (grade)": st.number_input("Previous Qualification Grade", min_value=0.0),
    "Admission grade": st.number_input("Admission Grade", min_value=0.0),
    "Educational special needs": st.selectbox("Educational Special Needs (0 = No, 1 = Yes)", [0, 1]),
    "Tuition fees up to date": st.selectbox("Tuition Fees Up-to-Date (0 = No, 1 = Yes)", [0, 1]),
    "Gender": st.selectbox("Gender (0 = Female, 1 = Male)", [0, 1]),
    "Scholarship holder": st.selectbox("Scholarship Holder (0 = No, 1 = Yes)", [0, 1]),
    "Age at enrollment": st.number_input("Age at Enrollment", min_value=15, max_value=100),
    "Curricular units 1st sem (credited)": st.number_input("Curricular Units 1st Semester (Credited)", min_value=0),
    "Curricular units 1st sem (enrolled)": st.number_input("Curricular Units 1st Semester (Enrolled)", min_value=0),
    "Curricular units 1st sem (evaluations)": st.number_input("Curricular Units 1st Semester (Evaluations)", min_value=0),
    "Curricular units 1st sem (approved)": st.number_input("Curricular Units 1st Semester (Approved)", min_value=0),
    "Curricular units 1st sem (grade)": st.number_input("Curricular Units 1st Semester (Grade)", min_value=0.0),
    "Curricular units 1st sem (without evaluations)": st.number_input("Curricular Units 1st Semester (Without Evaluations)", min_value=0),
    "Curricular units 2nd sem (credited)": st.number_input("Curricular Units 2nd Semester (Credited)", min_value=0),
    "Curricular units 2nd sem (enrolled)": st.number_input("Curricular Units 2nd Semester (Enrolled)", min_value=0),
    "Curricular units 2nd sem (evaluations)": st.number_input("Curricular Units 2nd Semester (Evaluations)", min_value=0),
    "Curricular units 2nd sem (approved)": st.number_input("Curricular Units 2nd Semester (Approved)", min_value=0),
    "Curricular units 2nd sem (grade)": st.number_input("Curricular Units 2nd Semester (Grade)", min_value=0.0),
    "Curricular units 2nd sem (without evaluations)": st.number_input("Curricular Units 2nd Semester (Without Evaluations)", min_value=0),
}

# Predict button
if st.button("Predict"):
    try:
        # Convert inputs into a numpy array
        input_data = np.array(list(features.values())).reshape(1, -1)
        
        # Standardize the inputs using scaler parameters
        standardized_data = (input_data - feature_means) / feature_stds
        
        # Make a prediction using the trained model
        prediction = model.predict(standardized_data)
        prediction_label = {0: "Dropout", 1: "Graduate", 2: "Enrolled"}
        
        # Display the result
        st.subheader("Prediction Result:")
        st.write(f"Student Status: **{prediction_label[prediction[0]]}**")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")