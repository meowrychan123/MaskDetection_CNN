# -*- coding: utf-8 -*-
"""Week4_CNN.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mA27YuFVjooZa68k2fWITRaT0da5ypvE
"""

import os
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

with_mask_files = os.listdir('/content/drive/MyDrive/CNN_imageprocWeek4/with_mask')
print(with_mask_files[0:5])
print(with_mask_files[-5:])

without_mask_files = os.listdir('/content/drive/MyDrive/CNN_imageprocWeek4/without_mask')
print(without_mask_files[0:5])
print(without_mask_files[-5:])

print('Number of with mask images:', len(with_mask_files))
print('Number of without mask images:', len(without_mask_files))

"""**Creating Labels for the two class of Images**

with mask --> 1

without mask --> 0
"""

with_mask_labels = [1]*500

without_mask_labels = [0]*500

print(with_mask_labels[0:5])

print(without_mask_labels[0:5])

print(len(with_mask_labels))
print(len(without_mask_labels))

labels = with_mask_labels + without_mask_labels

print(len(labels))
print(labels[0:5])
print(labels[-5:])

"""**Displaying the Images**"""

# with mask image
img = mpimg.imread('/content/drive/MyDrive/CNN_imageprocWeek4/with_mask/with_mask_10.jpg')
imgplot = plt.imshow(img)
plt.show()

# without mask image
img = mpimg.imread('/content/drive/MyDrive/CNN_imageprocWeek4/without_mask/without_mask_1088.jpg')
imgplot = plt.imshow(img)
plt.show()

"""**Image Processing**

1. Resize the Images
2. Convert the images to numpy arrays
"""

# convert images to numpy arrays

from PIL import Image

with_mask_path = '/content/drive/MyDrive/CNN_imageprocWeek4/with_mask/'

data = []

for img_file in with_mask_files:

  image = Image.open(with_mask_path + img_file)
  image = image.resize((128,128))
  image = image.convert('RGB')
  image = np.array(image)
  data.append(image)

without_mask_path = '/content/drive/MyDrive/CNN_imageprocWeek4/without_mask/'

for img_file in without_mask_files:

  image = Image.open(without_mask_path + img_file)
  image = image.resize((128,128))
  image = image.convert('RGB')
  image = np.array(image)
  data.append(image)

type(data)

len(data)

data[0]

type(data[0])

data[0].shape

# converting image list and label list to numpy arrays

X = np.array(data)
Y = np.array(labels)

type(X)

type(Y)

print(X.shape)
print(Y.shape)

print(Y)

"""**Train Test Split**"""

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

# scaling the data

X_train_scaled = X_train/255

X_test_scaled = X_test/255

X_train[0]

X_train_scaled[0]

"""**Building a Convolutional Neural Networks (CNN)**"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, LeakyReLU

"""**Experiment 1**"""

model = Sequential()

num_of_classes = 2

model.add(Conv2D(32, (3, 3), activation='relu', padding='valid', input_shape=(128, 128, 3)))
model.add(MaxPooling2D(pool_size=(2, 2), padding='valid'))

model.add(Conv2D(64, (3, 3), activation='relu', padding='valid'))
model.add(MaxPooling2D(pool_size=(2, 2), padding='valid'))

model.add(Conv2D(128, (3, 3), activation='relu', padding='valid'))
model.add(MaxPooling2D(pool_size=(2, 2), padding='valid'))

model.add(Flatten())

model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))


model.add(Dense(num_of_classes, activation='sigmoid'))  # Output layer for binary classification

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['acc'])

model.summary()

history = model.fit( X_train_scaled, Y_train, validation_split=0.1, epochs=10)

"""**Model Evaluation**"""

loss, accuracy = model.evaluate(X_test_scaled, Y_test)
print('Test Accuracy =', accuracy)

import matplotlib.pyplot as plt

h = history

# ploting loss value
plt.plot(h.history['loss'], label='train loss')
plt.plot(h.history['val_loss'], label='validation loss')
plt.legend()
plt.show()

# ploting accuracy value
plt.plot(h.history['acc'], label='train accuracy')
plt.plot(h.history['val_acc'], label='validation accuracy')
plt.legend()
plt.show()

"""**Experiment 2**"""

model_2 = Sequential()
model_2.add(Conv2D(32,kernel_size=(3,3), padding='same', activation='relu', input_shape=(128,128,3) ))
model_2.add(Conv2D(32,kernel_size=(3,3), padding='same',activation='relu'))
model_2.add(Conv2D(32,kernel_size=(3,3), padding='same',activation='relu'))
model_2.add(Flatten())
model_2.add(Dense(128,activation='relu'))
model_2.add(Dense(10,activation='relu'))

model_2.add(Dense(1, activation='sigmoid'))

model_2.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])

model_2.summary()

history = model.fit( X_train_scaled, Y_train, validation_split=0.1, epochs=10)

"""**Model 2 Evaluation**"""

loss, accuracy = model_2.evaluate(X_test_scaled, Y_test)
print('Test Accuracy =', accuracy)

h2 = history

# ploting loss value
plt.plot(h2.history['loss'], label='train loss')
plt.plot(h2.history['val_loss'], label='validation loss')
plt.legend()
plt.show()

# ploting accuracy value
plt.plot(h2.history['acc'], label='train accuracy')
plt.plot(h2.history['val_acc'], label='validation accuracy')
plt.legend()
plt.show()

"""**Experiment 3**"""

model_3 = Sequential()

num_of_classes = 2

model_3.add(Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(128, 128, 3)))
model_3.add(MaxPooling2D(pool_size=(2, 2), padding='same'))

model_3.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
model_3.add(MaxPooling2D(pool_size=(2, 2), padding='same'))

model_3.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
model_3.add(MaxPooling2D(pool_size=(2, 2), padding='same'))

model_3.add(Flatten())

model_3.add(Dense(128, activation='relu'))
model_3.add(Dropout(0.2))

model_3.add(Dense(64, activation='relu'))
model_3.add(Dropout(0.2))


model_3.add(Dense(num_of_classes, activation='sigmoid'))

model_3.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['acc'])

history = model_3.fit( X_train_scaled, Y_train, validation_split=0.1, epochs=20)

"""**Model 3 Evaluation**"""

loss, accuracy = model_3.evaluate(X_test_scaled, Y_test)
print('Test Accuracy =', accuracy)

h3 = history

# ploting loss value
plt.plot(h3.history['loss'], label='train loss')
plt.plot(h3.history['val_loss'], label='validation loss')
plt.legend()
plt.show()

# ploting accuracy value
plt.plot(h3.history['acc'], label='train accuracy')
plt.plot(h3.history['val_acc'], label='validation accuracy')
plt.legend()
plt.show()

"""**Experiment 4**"""

model_4 = Sequential()

num_of_classes = 2

model_4.add(Conv2D(32, (3, 3), padding='valid', input_shape=(128, 128, 3)))
model_4.add(LeakyReLU(alpha=0.01))
model_4.add(MaxPooling2D(pool_size=(2, 2), padding='valid'))

model_4.add(Conv2D(64, (3, 3), padding='valid', input_shape=(128, 128, 3)))
model_4.add(LeakyReLU(alpha=0.01))
model_4.add(MaxPooling2D(pool_size=(2, 2), padding='valid'))

model_4.add(Conv2D(128, (3, 3), padding='valid', input_shape=(128, 128, 3)))
model_4.add(LeakyReLU(alpha=0.01))
model_4.add(MaxPooling2D(pool_size=(2, 2), padding='valid'))

model_4.add(Flatten())

model_4.add(Dense(128))
model_4.add(LeakyReLU(alpha=0.01))
model_4.add(Dropout(0.5))

model_4.add(Dense(64))
model_4.add(LeakyReLU(alpha=0.01))
model_4.add(Dropout(0.5))

model_4.add(Dense(num_of_classes, activation='sigmoid'))

model_4.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['acc'])

history = model_4.fit( X_train_scaled, Y_train, validation_split=0.1, epochs=10)

"""**Model 4 Evaluation**"""

loss, accuracy = model_4.evaluate(X_test_scaled, Y_test)
print('Test Accuracy =', accuracy)

h4 = history

# ploting loss value
plt.plot(h4.history['loss'], label='train loss')
plt.plot(h4.history['val_loss'], label='validation loss')
plt.legend()
plt.show()

# ploting accuracy value
plt.plot(h4.history['acc'], label='train accuracy')
plt.plot(h4.history['val_acc'], label='validation accuracy')
plt.legend()
plt.show()

"""**Experiment 5**"""

model_5 = Sequential()

num_of_classes = 2

model_5.add(Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(128, 128, 3)))
model_5.add(MaxPooling2D(pool_size=(2, 2), padding='same'))

model_5.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
model_5.add(MaxPooling2D(pool_size=(2, 2), padding='same'))


model_5.add(Flatten())

model_5.add(Dense(128, activation='relu'))
model_5.add(Dropout(0.5))

model_5.add(Dense(64, activation='relu'))
model_5.add(Dropout(0.5))


model_5.add(Dense(num_of_classes, activation='sigmoid'))

model_5.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['acc'])

model_5.summary()

history = model_5.fit(X_train_scaled, Y_train, validation_split=0.1, epochs=5)

"""**Model 5 Evaluation**"""

loss, accuracy = model_5.evaluate(X_test_scaled, Y_test)
print('Test Accuracy =', accuracy)

h5 = history

# ploting loss value
plt.plot(h5.history['loss'], label='train loss')
plt.plot(h5.history['val_loss'], label='validation loss')
plt.legend()
plt.show()

# ploting accuracy value
plt.plot(h5.history['acc'], label='train accuracy')
plt.plot(h5.history['val_acc'], label='validation accuracy')
plt.legend()
plt.show()