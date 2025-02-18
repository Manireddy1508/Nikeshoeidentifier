import os
import uvicorn
from fastapi import FastAPI, UploadFile, File, HTTPException
from model import load_model_and_predict
from utils import is_image_valid
import io
from PIL import Image

# Initialize FastAPI app
app = FastAPI()

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    """Upload an image and get a prediction from the model."""
    try:
        # Read uploaded image
        image = Image.open(io.BytesIO(await file.read()))

        # Validate image before processing
        is_valid, message = is_image_valid(image)
        if not is_valid:
            raise HTTPException(status_code=400, detail=f"Invalid image: {message}")

        # Get model prediction
        prediction = load_model_and_predict(image)
        return {"filename": file.filename, "prediction": prediction}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def home():
    """Root endpoint - Health check."""
    return {"message": "Welcome to the Sneaker Classification API!"}

# Cloud Run expects the app to listen on PORT=8080
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Use Cloud Run PORT
    uvicorn.run(app, host="0.0.0.0", port=port)
