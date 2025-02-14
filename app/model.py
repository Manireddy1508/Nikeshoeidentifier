¿import os
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

# Define model path dynamically
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get current directory
MODEL_PATH = os.path.join(BASE_DIR, "nike_shoe_classifier.h5")  # Model in `app/` folder

# Load the trained model
model = load_model(MODEL_PATH)

def load_model_and_predict(image):
    """
    Preprocess image and make predictions using the model.
    """
    try:
        image = image.resize((224, 224))  # Resize to match training size
        image = np.array(image) / 255.0  # Normalize pixel values (0-1)
        
        print(f"✅ Image Shape Before Reshaping: {image.shape}")  # Debugging

        image = image.reshape(1, 224, 224, 3)  # Reshape for model input

        print(f"✅ Image Shape After Reshaping: {image.shape}")  # Debugging

        prediction = model.predict(image)[0][0]  # Get prediction

        print(f"✅ Model Prediction Output: {prediction}")  # Debugging

        return "Nike" if prediction < 0.5 else "Other"

    except Exception as e:
        return f"Error in prediction: {str(e)}"
