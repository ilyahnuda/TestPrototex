import keras.losses
import numpy as np
from keras import models, datasets
from keras.layers import Conv2D, MaxPool2D, Flatten, Dense
import tensorflow as tf


def prepare_data(train_images: list = None, train_labels: list = None, test_images: list = None,
                 test_labels: list = None, input_shape=(28, 28, 1)):
    if None in [train_images, train_labels, test_images, test_labels]:
        (train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data(
            path='mnist.npz'
        )

    train_images = train_images.reshape(train_images.shape[0], input_shape[0], input_shape[1], input_shape[2])
    test_images = test_images.reshape(test_images.shape[0], input_shape[0], input_shape[1], input_shape[2])

    train_images = train_images / 255.0
    test_images = test_images / 255.0

    train_labels = tf.one_hot(train_labels.astype(np.int32), depth=10)
    test_labels = tf.one_hot(test_labels.astype(np.int32), depth=10)

    return train_images, train_labels, test_images, test_labels


def create_model(num_classes, input_shape=(28, 28, 1)):
    model = models.Sequential()

    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
    model.add(MaxPool2D((2, 2)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(Flatten())
    model.add(Dense(64, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))

    model.compile(optimizer='adam',
                  loss=keras.losses.CategoricalCrossentropy(), metrics=keras.metrics.F1Score())

    return model


def train_model(num_classes: int, num_epochs: int, validation_split: float, batch_size: int):
    train_images, train_labels, test_images, test_labels = prepare_data()

    model = create_model(num_classes)

    history = model.fit(train_images, train_labels, epochs=num_epochs, validation_split=validation_split,
                        batch_size=batch_size)

    loss, score = model.evaluate(test_images, test_labels)
    metric = np.average(score)

    return history, (loss, metric)


def main():
    num_epochs = 5
    validation_split = 0.1
    batch_size = 32
    num_classes = 10

    train_model(num_classes=num_classes, num_epochs=num_epochs, validation_split=validation_split,
                batch_size=batch_size)


if __name__ == '__main__':
    main()
