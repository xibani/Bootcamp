# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tensorflow as tf
tf.__version__
import numpy as np
import datetime
from tensorflow.keras.datasets import fashion_mnist
import matplotlib.pyplot as plt

#Cargar el dataset Fashion Mnist
fashion_mnist = tf.keras.datasets.fashion_mnist
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

# Visualizar la primera imagen del dataset de entrenamiento
plt.figure()
plt.imshow(X_train[0])
plt.colorbar()
plt.grid(False)

X_train = X_train / 255.0
y_train = y_train / 255.0

# Visualizar la primera imagen del dataset de entrenamiento
plt.figure()
plt.imshow(X_train[0])
plt.colorbar()
plt.grid(False)

X_train = X_train.reshape(-1, 28*28)
X_test = X_test.reshape(-1, 28*28)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(units=128, activation='relu', input_shape=(784,)))
model.add(tf.keras.layers.Dense(units=10, activation='softmax'))
opt = tf.keras.optimizers.Adam(learning_rate=0.1)
model.compile(optimizer=opt, loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()

model.fit(X_train, y_train, epochs=5, batch_size=1)


"""
Archivo de ejemplo
"""
import numpy as np
import datetime
import tensorflow as tf
from tensorflow.keras.datasets import fashion_mnist

tf.__version__

#Cargar el dataset Fashion Mnist 
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

X_train = X_train / 255.0
X_test = X_test / 255.0

#Como cada imagen tiene 28x28 píxeles, usamos la función reshape en todo el dataset de entrenamiento para convertirlo 
# en vectores de tamaño [-1 (todos los elementos), anchura * altura]
X_train = X_train.reshape(-1, 28*28)
X_train.shape
#Redimensionamos el conjunto de testing del mismo modo
X_test = X_test.reshape(-1, 28*28)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(units=128, activation='relu', input_shape=(784, )))
model.add(tf.keras.layers.Dropout(0.2))
model.add(tf.keras.layers.Dense(units=10, activation='softmax'))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['sparse_categorical_accuracy'])
model.summary()

model.fit(X_train, y_train, epochs=5)

test_loss, test_accuracy = model.evaluate(X_test, y_test)
print("Test accuracy: {}".format(test_accuracy))























