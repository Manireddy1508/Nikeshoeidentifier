import os
import uvicorn
from fastapi import FastAPI, UploadFile, File, HTTPException
from app.model import load_model_and_predict
from app.utils import is_image_valid
import io
from PIL import Image

# Initialize FastAPI app
app = FastAPI(title="Nike Shoe Classifier API")

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
        return {"prediction": prediction}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def home():
    """Root endpoint - Health check."""
    return {"message": "Welcome to the Nike Shoe Classifier API!"}

# Cloud Run expects the app to listen on PORT=8080
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Default to 8080
    print(f" Running on port {port}")  # Debugging line
    uvicorn.run(app, host="0.0.0.0", port=port)

