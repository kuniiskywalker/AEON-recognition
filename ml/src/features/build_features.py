from PIL import Image
import os, glob
import numpy as np
from sklearn import model_selection
import json

with open('configs/stores.json') as f:
	classes = json.load(f)
num_classes = len(classes)
image_size = 224


X = []
Y = []

for index, classlabel in enumerate(classes):
	photo_dir = "data/raw/" + classlabel
	files = glob.glob(photo_dir + "/*")
	for i, file in enumerate(files):
		try:
			image = Image.open(file)
			image = image.convert("RGB")
			print("file: " + file)
			print(image)
			image = image.resize((image_size, image_size))
			data = np.asarray(image)
			X.append(data)
			Y.append(index)
		except IOError:
			print("Error: " + file)

X = np.array(X)
Y = np.array(Y)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y)
xy = (X_train, X_test, y_train, y_test)

np.save("data/processed/imagefiles_224.npy", xy)
