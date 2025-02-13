import tensorflow as tf
import os

MODEL_PATH = "app/nike_shoe_classifier.h5"

def load_model_and_predict(image):
    """Load model and make a prediction"""
    model = tf.keras.models.load_model(MODEL_PATH)
    
    # Preprocess image
    img = image.resize((224, 224))
    img = tf.keras.preprocessing.image.img_to_array(img) / 255.0
    img = tf.expand_dims(img, axis=0)

    # Get prediction
    prediction = model.predict(img)
    
    return "Nike" if prediction[0][0] < 0.5 else "Other"

