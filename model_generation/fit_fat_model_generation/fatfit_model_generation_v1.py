# -*- coding: utf-8 -*-
"""FatFit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xpTK0XXc5ESd0kov31RTrZRK-u7f1tVq
"""

# !unzip fat

# os.remove('fit_man/.DS_Store')

# os.remove('fat_man/.DS_Store')

# os.remove('fat_woman/.DS_Store')

# os.remove('fit_woman/.DS_Store')

# import shutil

# shutil.rmtree('__MACOSX')

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from keras.utils import to_categorical 
import os
from keras.layers import Activation, Conv2D, Dense, Flatten, MaxPool2D, BatchNormalization, Dropout
from keras.models import Sequential
from sklearn.model_selection import train_test_split
from keras.optimizers import Adam
import cv2


def corp_to_square_than_resize(img, new_width=None, new_height=None):
  width, height = img.size    # Get dimensions
  
  if new_width is None:
      new_width = min(width, height)
  if new_height is None:
      new_height = min(width, height)
  
  left = np.ceil((width - new_width) / 2)
  right = width - np.floor((width - new_width) / 2)

  top = int(np.ceil((height - new_height) / 2))
  bottom = height - np.floor((height - new_height) / 2)

  center_cropped_img = img.crop((left, top, right, bottom))

  return center_cropped_img

X = []  # images
Y = []  # categories

name_encode = {"fat_man":0, "fit_man":1, "fat_woman":2, "fit_woman":3}
num_classes = len(name_encode)


def images_to_array(folder):
  for image_name in os.listdir(folder):
    loaded_image = Image.open(os.path.join(folder, image_name))
    croped_image = corp_to_square_than_resize(loaded_image)
    resized_image = Image.Image.resize(croped_image, [200,200])
    image_array = np.array(resized_image)
    X.append(image_array)
    Y.append(name_encode[folder])

    image_flipped = cv2.flip(image_array, 1)
    X.append(image_flipped)
    Y.append(name_encode[folder])

    image_blurred = cv2.blur(image_array, (2,2))
    X.append(image_blurred)
    Y.append(name_encode[folder])

    image_flipped_blurred = cv2.blur(image_flipped, (2,2))
    X.append(image_flipped_blurred)
    Y.append(name_encode[folder])


def show_image(index):
  plt.imshow(X[index])
  plt.show()
  print(Y[index])


images_to_array('fat_man')
images_to_array('fit_man')
images_to_array('fat_woman')
images_to_array('fit_woman')

Y = to_categorical(Y, num_classes=num_classes)
# normalayzing X data
X = (np.array(X) - 127.5) / 127.5
# show_image(47)

model = Sequential()
model.add(Conv2D(32, (5,5), padding='same', activation='relu', input_shape=(200,200,3)))
model.add(BatchNormalization())
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Conv2D(400, (5,5), padding='same', activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(rate=0.2))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Conv2D(400, (5,5), padding='same', activation='relu'))
model.add(BatchNormalization()) 
model.add(Dropout(rate=0.2))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Conv2D(400, (5,5), padding='same', activation='relu'))
model.add(BatchNormalization())
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(300))
model.add(Activation('relu'))
model.add(Dense(num_classes))
model.add(Activation('softmax'))
model.summary()

X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size=0.2)

optimizer = Adam(lr=0.001)
model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
h = model.fit(X_train, y_train, batch_size=10, epochs=35, validation_data = (X_test, y_test))
model.save('fit_fat_CNN_V2.h5')

# plt.plot(h.history['accuracy'])
# plt.plot(h.history['val_accuracy'])
# plt.title("CNN accuracy: Train and test")
# plt.xlabel('Epoch number')
# plt.ylabel('Accuracy')
# plt.legend(loc='lower right')

from keras.models import load_model


model = load_model('fit_fat_CNN.h5')

def fatness_prediction(index_number):
  # img = (np.array(X[index_number]) - 127.5) / 127,5
  reshaped_img = X[index_number].reshape(1,200,200,3)
  prediction = model.predict_classes(reshaped_img)
  show_image(index_number)
  for key, value in name_encode.items():
    if value == prediction:
      print(key)
  


fatness_prediction(1900)

fatness_prediction(1000)

# model_generation = load_model('fit_fat_CNN.h5')

# def fatness_prediction_load(image_path):
#   image_loaded = Image.open(image_path)
#   croped_image = corp_to_square_than_resize(image_loaded)
#   resized_image = Image.Image.resize(croped_image, (200,200))
#   image_normalized = (np.array(resized_image) - 127.5) / 127.5
#   reshaped_img = image_normalized.reshape(1,200,200,3)
#   prediction = model_generation.predict_classes(reshaped_img)
#   plt.imshow(resized_image)
#   plt.show()
#   print(prediction)
#   for key, value in name_encode.items():
#     if value == prediction:
#       print(key)
  

# fatness_prediction_load('fm4.jpeg')

# fatness_prediction_load('w3.jpg')

