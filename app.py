import os
import pandas as pd
import numpy as np
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sklearn.ensemble import RandomForestClassifier

## fastapi
app = FastAPI();

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

## dataset 
data_set_file = "diabetes_dataset.csv"

if not os.path.exists(data_set_file):
    df = pd.DataFrame({
        "Pregnancies": [1, 0],
        "Glucose": [80, 90],
        "BloodPressure": [72, 80],
        "SkinThickness": [19, 25],
        "Insulin": [200, 150],
        "BMI": [25.6, 28.1],
        "DiabetesPedigreeFunction": [0.5, 0.7],
        "Age": [30, 35],
        "Outcome": [1, 0]
    })
    df.to_csv(data_set_file, index=False)

## treniranje modela

data = pd.read_csv(data_set_file)

X = data.iloc[:,:-1]
y = data.iloc[:,-1]

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

## request models

class PredictRequest(BaseModel):
    pregnancies: float
    glucose: float
    bloodPressure: float
    skinThickness: float
    insulin: float
    bmi: float
    diabetesPedigreeFunction: float
    age: float


class AddDataRequest(PredictRequest):
    outcome: int

## endpoints

## predikcija
@app.post("/predict")
async def predict(data: PredictRequest):
    try:
        features = np.array([[data.pregnancies, data.glucose, data.bloodPressure, data.skinThickness,
                              data.insulin, data.bmi, data.diabetesPedigreeFunction, data.age]])
        prediction = model.predict(features)[0]
        return {"prediction": int(prediction)}
    except Exception as e:
        raise HTTPException(detail=f"Greška pri predikciji: {str(e)}")

## dodajvanje podataka
@app.post("/add_data")
async def add_data(data: AddDataRequest):
    try:
        new_data = {
            "Pregnancies": data.pregnancies,
            "Glucose": data.glucose,
            "BloodPressure": data.bloodPressure,
            "SkinThickness": data.skinThickness,
            "Insulin": data.insulin,
            "BMI": data.bmi,
            "DiabetesPedigreeFunction": data.diabetesPedigreeFunction,
            "Age": data.age,
            "Outcome": data.outcome
        }
        df = pd.DataFrame([new_data])
        df.to_csv(data_set_file, mode='a', header=False, index=False)

        updated_data = pd.read_csv(data_set_file)
        X_updated = updated_data.iloc[:,:-1]
        y_updated = updated_data.iloc[:,-1]
        model.fit(X_updated, y_updated)

        return {"message": "Dodati su novi podaci i model je ponovo podučen!."}
    except Exception as e:
        raise HTTPException(detail=f"Error pri predikciji: {str(e)}")
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)
    
