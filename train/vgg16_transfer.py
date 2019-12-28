import numpy as np
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.optimizers import SGD, Adam
from tensorflow.python.keras.utils import np_utils
from tensorflow.python.keras.applications import VGG16

classes = ["toda", "ushiku"]
num_classes = len(classes)
image_size = 224

# データ読み込み
X_train, X_test, y_train, y_test = np.load("/data/imagefiles_224.npy", allow_pickle=True)

y_train = np_utils.to_categorical(y_train, num_classes)
y_test = np_utils.to_categorical(y_test, num_classes)
X_train = X_train.astype("float") / 255.0
X_test = X_test.astype("float") / 255.0

# モデル定義
model = VGG16(weights="imagenet", include_top=False, input_shape=(image_size, image_size, 3))

top_model = Sequential()
top_model.add(Flatten(input_shape=(model.output_shape[1:])))
top_model.add(Dense(256, activation='relu'))
top_model.add(Dropout(0.5))
top_model.add(Dense(num_classes, activation='softmax'))

model = Model(inputs=model.input, outputs=top_model(model.output))

# 学習のフリーズ
for layer in model.layers[:15]:
	print(layer)
	layer.trainable = False

# opt = SGD(lr=0.01) # rmsprop, adam
opt = Adam()
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=["accuracy"])

model.fit(X_train, y_train, batch_size=32, epochs=20)

score = model.evaluate(X_test, y_test, batch_size=32)

