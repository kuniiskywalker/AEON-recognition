from typing import List

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
from PIL import Image
import io
import json

from fastapi import FastAPI, File, UploadFile
from starlette.requests import Request
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory="/app/templates")

IMAGE_SIZE = 224 # 画像サイズ
MODEL_FILE_PATH = '/app/vgg16_transfer.h5' # モデルファイル

model = load_model(MODEL_FILE_PATH)

with open('/app/stores.json') as f:
    classes = json.load(f)

app = FastAPI()

@app.post("/predict/")
async def predict(file: bytes = File(...)):

    image = Image.open(io.BytesIO(file))
    image = image.convert("RGB")
    image = image.resize((IMAGE_SIZE, IMAGE_SIZE))
    data = np.asarray(image) / 255.0
    X = []
    X.append(data)
    X = np.array(X)

    result = model.predict([X])[0]
    predicted = result.argmax()
    percentage = int(result[predicted] * 100)

    return classes[predicted], percentage

@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
