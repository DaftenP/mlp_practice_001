import tensorflow as tf
from tensorflow import keras
import numpy as np


class MLPC():
    def __init__(self):
        self.model = self.new_model()

    def new_model(self):
        model = keras.Sequential([
            keras.layers.Dense(3000),
            keras.layers.Dense(1024, activation="relu"),
            keras.layers.Dropout(rate=0.5),
            keras.layers.Dense(1, activation='sigmoid')
        ])

        model.compile(optimizer="adam", metrics=["accuracy"],
                      loss="binary_crossentropy")
        return model
