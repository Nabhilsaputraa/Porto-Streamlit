from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel, conint, confloat
from typing import List
from dotenv import load_dotenv 
import joblib
import pandas as pd
import numpy as np
import os

# !API
load_dotenv()
API_KEY = os.getenv("API_KEY")
PREDICT_URL = "https://python-powered-mlops-from-frameworks-to-model-mo-production.up.railway.app/predict"

# Load model & preprocessor
model = joblib.load("model.pkl")
preprocessor = joblib.load("preprocessor.pkl")

# Request schema
class HouseFeatures(BaseModel):
    OverallQual: conint(ge=1, le=10)
    GrLivArea: confloat(gt=0)
    GarageCars: conint(ge=0)
    GarageArea: confloat(ge=0)
    TotalBsmtSF: confloat(ge=0)
    FirstFlrSF: confloat(ge=0)
    FullBath: conint(ge=0)
    TotRmsAbvGrd: conint(ge=0)
    YearBuilt: conint(ge=1800)

@app.post("/predict")
def predict_batch(features: List[HouseFeatures], x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid API Key")

    try:
        df = pd.DataFrame([f.dict() for f in features])
        
        #? Rename
        if "1stFlrSF" in preprocessor.feature_names_in_:
            df.rename(columns={"FirstFlrSF": "1stFlrSF"}, inplace=True)

        X = preprocessor.transform(df)
        preds = model.predict(X)

        return {"prediction": preds.tolist()}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
