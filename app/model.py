import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import os

# Correct model path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get current directory
MODEL_PATH = os.path.join(BASE_DIR, "../Model/nike_shoe_classifier.h5")  # Go one level up

# Load model
model = load_model(MODEL_PATH)

def preprocess_image(image: Image.Image):
    """
    Preprocess an image for model prediction.
    - Resize to (224, 224)
    - Normalize pixel values
    - Expand dimensions for batch format
    """
    image = image.resize((224, 224))  # Resize to model input size
    image = np.array(image) / 255.0   # Normalize pixel values
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

def load_model_and_predict(image: Image.Image):
    """
    Process the image and run model inference.
    Returns "Nike" if prediction is < 0.5, otherwise "Other".
    """
    image = preprocess_image(image)
    prediction = model.predict(image)

    return "Nike" if prediction[0] < 0.5 else "Other"
