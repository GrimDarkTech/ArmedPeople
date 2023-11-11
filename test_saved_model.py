from tensorflow import keras
import tensorflow as tf
import numpy as np

img_width, img_height = 100, 100
model_loaded = keras.models.load_model("model_inpsz=100x100_epochs=55_btchsize=50")
image = tf.keras.preprocessing.image.load_img("C:\\nonsystemic\downloads\datasets\watches\\from web\\rado.jpg",
                                              target_size=(img_width, img_height, 3))
input_img = tf.keras.preprocessing.image.img_to_array(image)
input_array = np.array(input_img)
input_array = input_array / 255
checked = model_loaded.predict(input_array.reshape(-1, img_width, img_height, 3))[0]
print(checked)
