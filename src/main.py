from fastapi import FastAPI, UploadFile
from app.preprocessing import preprocess_data
from app.model import train_model, save_model, load_model
from app.prediction import predict

app = FastAPI()

# Load the model on startup
model = load_model("models/student_dropout_model.pkl")

@app.post("/predict")
async def predict_endpoint(features: dict):
    # Preprocess features and make a prediction
    processed_features = preprocess_data(features)
    prediction = predict(model, processed_features)
    return {"prediction": prediction}

@app.post("/upload")
async def upload_data(file: UploadFile):
    # Save the uploaded file
    with open("data/new_data.csv", "wb") as f:
        f.write(await file.read())
    return {"message": "New data uploaded successfully!"}

@app.post("/retrain")
async def retrain_model():
    # Load new data and retrain the model
    new_data = preprocess_data("data/new_data.csv")
    train_model(new_data, "models/student_dropout_model.pkl")
    return {"message": "Model retrained successfully!"}