from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
import tensorflow as tf


def load_dataset(path, shuffle=True):
    generator = ImageDataGenerator(rescale=1. / 255, validation_split=0)
    return generator.flow_from_directory(
        directory=path,
        target_size=(img_width, img_height),
        batch_size=bat_size,
        class_mode="categorical",
        shuffle=shuffle
    )


img_width, img_height = 75, 75
inp_shape = (img_width, img_height, 1)
epochs = 70
bat_size = 30
outputs = 10

train_dataset = load_dataset("datasets/train")
test_dataset = load_dataset("datasets/train", shuffle=False)
valid_dataset = load_dataset("datasets/train")

model = Sequential([tf.keras.layers.Flatten(input_shape=inp_shape),
    tf.keras.layers.Dense(120, activation='relu'), tf.keras.layers.Dense(120, activation='relu'),
    tf.keras.layers.Dense(outputs, activation='softmax')
])
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit_generator(
    train_dataset,
    steps_per_epoch=train_dataset.samples // bat_size,
    epochs=epochs,
    validation_data=valid_dataset,
    validation_steps=valid_dataset.samples // bat_size
)
model.save(f"model_inpsz={img_width}x{img_width}_epochs={epochs}_btchsize={bat_size}")
