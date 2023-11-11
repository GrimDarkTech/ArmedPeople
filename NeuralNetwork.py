from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
import tensorflow as tf
import numpy as np

class NeuralNetwork:
    def init(self, epochs=70):
        self.__img_wight, self.__img_height = 150, 150
        self.__input_shape = (self.__img_wight, self.__img_height, 1)
        self.__epochs = epochs
        self.__batch_size = 35
        self.__init_dataset()
        self.__study()
        self.__model.save('model_4')


    def __init_dataset(self):
        datagen = ImageDataGenerator(rescale=1. / 255, validation_split=0)

        self.__train_dataset = datagen.flow_from_directory(
            directory="datasets/train",
            target_size=(self.__img_wight, self.__img_height),
            batch_size=self.__batch_size,
            class_mode="categorical"
        )
        self.__test_dataset = datagen.flow_from_directory(
            directory="datasets/test",
            target_size=(self.__img_wight, self.__img_height),
            batch_size=self.__batch_size,
            shuffle=False,
            class_mode="categorical"
        )
        self.__valid_dataset = datagen.flow_from_directory(
            directory="datasets/valid",
            target_size=(self.__img_wight, self.__img_height),
            batch_size=self.__batch_size,
            class_mode="categorical"
        )

    def __study(self):
        self.__model = Sequential([
            tf.keras.layers.Flatten(input_shape=self.__input_shape),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(35, activation='softmax')
        ])

        self.__model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

        self.__model.fit_generator(
            self.__train_dataset,
            steps_per_epoch=self.__train_dataset.samples // self.__batch_size,
            epochs=self.__epochs,
            validation_data=self.__valid_dataset,
            validation_steps=self.__valid_dataset.samples // self.__batch_size
        )

    def network_quality_assessment(self) -> str:
        scores = self.__model.evaluate_generator(self.__test_dataset, len(self.__test_dataset))
        scores = scores[1] * 100
        return f"актуальность данных {round(scores, 2)}%"

    def predict(self, path):
        image = tf.keras.preprocessing.image.load_img(path, target_size=self.__input_shape)
        input_img = tf.keras.preprocessing.image.img_to_array(image)
        input_array = np.array(input_img)
        input_array = input_array / 255
        return self.__model.predict(input_array.reshape(-1, self.__img_wight, self.__img_height, 3))[0]

