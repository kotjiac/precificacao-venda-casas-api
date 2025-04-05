from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from utils import load_model

app = FastAPI()
model = load_model()

class InputData(BaseModel):
    zipcode: str
    sqft_living: float
    grade: int
    sqft_above: float
    sqft_living15: float
    bathrooms: float

@app.post("/predict")
def predict(data: InputData):
    features = pd.DataFrame([{
        "zipcode": data.zipcode,
        "sqft_living": data.sqft_living,
        "grade": data.grade,
        "sqft_above": data.sqft_above,
        "sqft_living15": data.sqft_living15,
        "bathrooms": data.bathrooms
    }])
    prediction = model.predict(features)
    return {"predicted_price": prediction[0]}
