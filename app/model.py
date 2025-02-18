import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "nikeshoeornotshoe.h5")

# Load the trained model
model = load_model(MODEL_PATH)

# Class labels
class_labels = ["Nike", "Other", "Non-Shoe"]

def load_model_and_predict(image):
    """
    Preprocess image and make predictions using the model.
    """
    try:
        image = image.resize((224, 224))  # Resize to match training size
        image = np.array(image)  # Convert to numpy array
        image = np.expand_dims(image, axis=0)  # Add batch dimension
        image = preprocess_input(image)  # Apply MobileNetV2 preprocessing
        
        prediction = model.predict(image)[0]  # Get predictions
        predicted_class = np.argmax(prediction)  # Get class with highest confidence
        confidence_scores = prediction.tolist()  # Convert predictions to list
        
        return {
            "predicted_class": class_labels[predicted_class],
            "confidence_scores": confidence_scores
        }

    except Exception as e:
        return {"error": str(e)}

