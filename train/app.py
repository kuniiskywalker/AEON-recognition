import numpy as np
# from tensorflow.python import keras
# from tensorflow.python.keras.models import Sequential
# from tensorflow.python.keras.layers import Dense, Dropout, Flatten
# from tensorflow.python.keras.layers import Conv2D, MaxPooling2D
# from tensorflow.python.keras.optimizers import SGD
# from tensorflow.python.keras.utils import np_utils
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.optimizers import SGD
from tensorflow.python.keras.utils import np_utils


classes = ["toda", "ushiku"]
num_classes = len(classes)
image_size = 150

X_train, X_test, y_train, y_test = np.load("/data/imagefiles.npy")

y_train = np_utils.to_categorical(y_train, num_classes)
y_test = np_utils.to_categorical(y_test, num_classes)

model = Sequential()
model.add(Conv2D(32,(3,3), activation='relu', input_shape=(image_size, image_size, 3)))
model.add(Conv2D(32,(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Conv2D(64,(3,3), activation='relu'))
model.add(Conv2D(64,(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

# 全結合層
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(num_classes, activation='softmax'))


opt = SGD(lr=0.01) # rmsprop, adam
model.compile(loss='categorical_crossentropy', optimizer=opt)

print(X_train)
print(y_train)

model.fit(X_train, y_train, batch_size=32, epochs=10)
