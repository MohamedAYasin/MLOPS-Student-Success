# 🎓 Student Success Prediction Model  

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

## 🚀 Setup Instructions  

1. Ensure Python 3.9+ is installed.  
2. Clone this repository:  
   ```bash  
   git clone https://github.com/mohamedayasin/student-success.git  
   cd student-success 
   
   ```  

---

## 🛠️ Preprocessing  

To preprocess the data, run:  
```bash  
python src/preprocessing.py  
```  

---

## 🧠 Model Training  

To train the model, use:  
```bash  
python src/model.py  
```  

---

## 🔮 Predictions  

Make predictions with the trained model:  
```bash  
python src/prediction.py  
```  

---

## 📊 Visualizations  



---

## 🌐 Links  

- **YouTube Demo Video**: [Model API on Render](https://example.com)  
- **API Link**: [Watch the Demo](https://example.com)  
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
- Evaluation and visualizations  

---  

 Mohamed Ahmed Yasin 😊
