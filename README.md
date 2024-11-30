# 🎓 Student Success Prediction Model  

![studyhard](https://github.com/user-attachments/assets/5bf4310a-5f3f-4f67-8e6e-56b6cee55f3e)


## 📝 Project Brief  
This project leverages machine learning to predict student success or dropout risk based on academic and demographic data. The model helps educational institutions identify students at risk and implement timely interventions to improve retention and outcomes.  

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
- Curricular units (credited, enrolled, evaluations, approved, grades, without evaluations) for the 1st and 2nd semesters

 ---
 
  ## 📊 Visualizations  



---


---

## 🚀 Setup Instructions  

1. Ensure Python 3.9+ is installed.  
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
python model/model.pkl  
```  

---

## 🌐 Links to Explore  

- **YouTube Demo Video**: [Demo Video](https://example.com)  
- **API Link**: [Fastapi Link](https://example.com)
-  **Rquirements**: [Summative Requirements](https://github.com/MohamedAYasin/MLOPS-Student-Success/blob/main/Machine_Learning_Pipeline%20-%20Summative_Assignment.pdf)
- **Dataset Source**: [Dataset Link](https://example.com)
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

## 📝 Additional Notes  



---  

## 📖 Notebook  

For an interactive exploration of the project, open the Jupyter/Google Colab notebook:  
```bash  
jupyter notebook  
```  

The notebook includes:  
- Data exploration  
- Preprocessing steps  
- Model training
- Retraining set up
- Evaluation and visualizations  

---  

 Mohamed Ahmed Yasin 😊
