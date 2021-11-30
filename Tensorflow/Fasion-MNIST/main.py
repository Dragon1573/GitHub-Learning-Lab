#!/usr/bin/env python3
# encoding: UTF-8

# %% Step 4: Importing Conda Packages

import numpy
import tensorflow as tf
from matplotlib import pyplot as plt
from tensorflow import keras

# %% Step 5: Testing image data

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()

# %% Step 6: Preprocess dataset

train_images = train_images / 255.0
test_images = test_images / 255.0

# %% Step 7: Model Generation

model = keras.Sequential(
    [keras.layers.Flatten(input_shape=(28, 28)),
     keras.layers.Dense(128, activation=tf.nn.relu),
     keras.layers.Dense(10, activation=tf.nn.softmax)]
)

# %% Step 8: Training Model

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=5)

# %% Step 9: Evaluating Model

test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f'Accuracy of test datasets: {test_acc:.4f}')
predictions = model.predict(test_images)
print('Probabilities of each labels:', predictions[0], sep='\n')
print('Predicted label: ', numpy.argmax(predictions[0]))
print('Actual label: ', test_labels[0])
