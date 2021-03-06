

import tensorflow as tf
from tensorflow import keras
from PIL import Image, ImageOps
import numpy as np


def seecraft_classification(img, weights_file):
    # Load the model
    model = tf.keras.models.load_model(weights_file)

    # Create the array of the right shape to feed into the keras model
    data = np.ndarray(shape=(1, 100, 100, 3), dtype=np.float32)
    image = img
    #image sizing
    size = (100, 100)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)
    
    # # Normalize the image
    # normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = image_array

    # run the inference
    prediction = model.predict(data)
    return np.argmax(prediction) # return position of the highest probability
