from fastapi import FastAPI, File, UploadFile
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import shutil
import uvicorn

# Load the trained model
MODEL_PATH = "nike_final_model.keras"
model = tf.keras.models.load_model(MODEL_PATH)

# Class labels
class_labels = ['Nike', 'Other', 'Non-Shoe']

# Initialize FastAPI
app = FastAPI(title="Nike Shoe Classifier", description="Upload an image to classify it as Nike, Other, or Non-Shoe.")

def predict_image(img_path):
    """Predict the class of an input image."""
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    predictions = model.predict(img_array)
    class_idx = np.argmax(predictions)

    return class_labels[class_idx], predictions.tolist()

@app.get("/", tags=["General"])
async def home():
    """Check API status."""
    return {"message": "Nike Classifier API is running. Go to /docs to test image uploads."}

@app.post("/predict", tags=["Prediction"])
async def predict(file: UploadFile = File(...)):
    """Upload an image and get a classification result."""
    file_path = f"temp_{file.filename}"
    
    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Get prediction
    predicted_class, confidence = predict_image(file_path)

    return {"class": predicted_class, "confidence": confidence}

# Run FastAPI with Uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
