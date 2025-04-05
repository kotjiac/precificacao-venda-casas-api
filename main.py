from fastapi import FastAPI
from pydantic import BaseModel
from utils import load_model, preprocess_input

app = FastAPI()
model = load_model()

class InputData(BaseModel):
    bedrooms: float
    bathrooms: float
    sqft_living: float
    sqft_lot: float
    floors: float
    waterfront: int
    view: int
    condition: int
    grade: int
    sqft_above: float
    sqft_basement: float
    yr_built: int
    yr_renovated: int
    zipcode: str
    lat: float
    long: float
    sqft_living15: float
    sqft_lot15: float

@app.post("/predict")
def predict(data: InputData):
    features = preprocess_input(data)
    prediction = model.predict([features])
    return {"predicted_price": prediction[0]}