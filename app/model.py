import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# Load the trained model
MODEL_PATH = "nike_final_model.keras"
model = tf.keras.models.load_model(MODEL_PATH)

# Class Labels
class_labels = ['Nike', 'Other', 'Non-Shoe']

def predict_image(img_path):
    """Predict the class of an input image."""
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    predictions = model.predict(img_array)
    class_idx = np.argmax(predictions)

    return class_labels[class_idx], predictions.tolist()


