from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

from .models import Predictions, Request
from .workflow import make_prediction


app = FastAPI()


@app.post('/predict', response_model=Predictions)
async def predict(request: Request):
    data = request.data
    predictions = make_prediction(jsonable_encoder(data))
    return Predictions(**predictions)