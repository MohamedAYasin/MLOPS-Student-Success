# 🎓 Student Status Prediction Model  

![studyhard](https://github.com/user-attachments/assets/5bf4310a-5f3f-4f67-8e6e-56b6cee55f3e)


## 📝 Project Overview

Student dropout and academic underperformance are critical challenges in higher education, affecting both students' futures and institutional effectiveness. Early identification of at-risk students is essential for implementing timely interventions and support systems.

This project tackles these challenges by building a machine learning model to predict student dropout probability and academic performance. The model analyzes a range of demographic, social, economic, and academic factors to deliver accurate predictions.

Using historical student data and advanced analytics, institutions can proactively identify students who may require additional support, enabling targeted interventions before academic issues escalate.

The solution involves training a model to predict students' study status—whether they are likely to drop out or continue their studies until graduation. It considers multiple factors such as enrollment data, academic performance, socio-economic indicators, and previous educational background to provide comprehensive insights into student success patterns.

---

## 📂 Project Structure  

```
Student-Success/  
│  
│── README.md  
│── notebook/  
│   └── student_success.ipynb  
│── src/  
│   ├── preprocessing.py  
│   ├── model.py  
│   └── prediction.py  
│── data/  
│   ├── train/  
│   └── test/  
└── models/  
    ├── scaler.pkl

```  

---

## ✨ Features  

The model uses the following input features:  
- Course  
- Daytime/evening attendance  
- Previous qualification  
- Previous qualification (grade)  
- Admission grade  
- Educational special needs  
- Tuition fees up to date  
- Gender  
- Scholarship holder  
- Age at enrollment  
- Curricular units (credited, enrolled, evaluations, approved, grades, without evaluations) for the 1st and 2nd semesters.

 ---
 
  ## 📊  Model Visualizations  

- Dropout = 0
- Graduate = 1
- Enrolled = 2
  
### Visualization of the total number of students dropout, graduate and enrolled w.r.t Course

![plot-visual](https://github.com/user-attachments/assets/87c90a7a-ee31-44e7-86d5-df0018227d06)

### Visualization of the total number of students dropout, graduated and enrolled

![plotting](https://github.com/user-attachments/assets/d9c5ddf1-4164-43c0-a37c-b7af7322b100)

### Confusion Matrix of the Trained Model

![confusionmatrix](https://github.com/user-attachments/assets/a0200ab4-3bbb-4a74-87d2-ae04d1c26c20)

---

## 🚀 Setup Instructions  

1. Ensure Python 3.9+ is installed in your system.  
2. Clone this repository:

```bash  
git clone https://github.com/mohamedayasin/student-success.git  
   cd student-success
``` 

---
    
## 🛠️ Preprocessing  

The src/preprocessing.py file contains the following main functions:

- load_and_preprocess_data(file_path): Loads the CSV file, splits features and target, scales the features using StandardScaler, and saves the scaler.
- load_scaler(): Loads the saved StandardScaler object.
To run preprocessing:

```bash  
python src/preprocessing.py  
```  

---

## 🧠 Model Training  

The src/model.py file contains the following main functions:

- create_model(): Creates and compiles the neural network model.
- train_model(X_train, y_train, epochs=80, batch_size=128): Trains the model with early stopping.
- evaluate_model(model, X_test, y_test): Evaluates the trained model on test data.
- plot_training_history(history): Plots the training and validation accuracy/loss.
  
To train the model:

```bash  
python src/model.py  
```  

---

## 🔮 Model Predictions  

Contains Pickle (.pkl) file:

`Location: models/model.pkl`

Purpose: Stores the fitted StandardScaler object for feature scaling.

```bash  
python models/student-predictor.pkl  
```  

---

## ⚡ Load Testing with Locust  

To simulate high traffic, install and run Locust:  

1. Install Locust:  
   ```bash  
   pip install locust  
   ```  
2. Run Locust:  
   ```bash  
   locust -f locustfile.py --host=https://student-success-model.onrender.com  
   ```  


---  

## 📖 Notebook  

For an interactive exploration of the project, open the Jupyter/Google Colab notebook:  
```bash  
jupyter notebook  
```  

## 📝 The notebook includes:  

- Data exploration  
- Preprocessing steps  
- Model training
- Retraining set up
- Evaluation and visualizations  

--- 

## 📱 Flutter App  

I developed a Flutter application that provides a user-friendly interface for interacting with the **Student Status Prediction Model**. The app consists of three main pages:

1. **Homepage**  
   - Displays various visualizations from the model, such as student status distributions and confusion matrices.
   - Helps users understand key insights and patterns from the data.

   ![home](https://github.com/user-attachments/assets/794ea46f-3d93-4cae-b220-e1997519e367)

2. **Predict Page**  
   - Allows users to input features like course attendance, age, and admission grade to predict a student's status (Dropout, Graduate, or Enrolled).
   - Integrates with the machine learning API to fetch predictions.

   ![predict](https://github.com/user-attachments/assets/bc2dfdbc-c239-4f79-b52f-4c395e4f7a06)

3. **Retrain Page**  
   - Facilitates model retraining by allowing users to upload updated datasets.
   - Once retrained, users can download the newly trained model for further usage.

   ![retrain](https://github.com/user-attachments/assets/8b12ddc6-0f81-4646-a4f4-2ce153bdcbb0)

### Key Features of the App:  
- **Intuitive Design**: Simple navigation to ensure seamless user experience.  
- **API Integration**: Communicates with the backend for predictions and retraining processes.  
- **Dynamic Updates**: Supports adding new data and retraining models on the fly.  
- **Visualization Tools**: Displays model outputs and metrics for better understanding.  

By leveraging this app, institutions can make data-driven decisions, monitor student performance trends, and deploy targeted interventions to enhance educational outcomes. 😊

---

## 🌐 Project Links to Explore

-  **Requirements**: [summative requirements](https://github.com/MohamedAYasin/MLOPS-Student-Success/blob/main/Machine_Learning_Pipeline%20-%20Summative_Assignment.pdf)

-  **Dataset Source**: [Dataset](https://www.kaggle.com/datasets/thedevastator/higher-education-predictors-of-student-retention/data)
  
- **API Link**: [https://student-status-check-model.onrender.com/docs]
  
-  **YouTube Demo Video**: [https://youtu.be/miRypThOdD4)

---

                                                   `Mohamed Ahmed Yasin` 😊
