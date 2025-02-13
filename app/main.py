from fastapi import FastAPI, UploadFile, File, HTTPException
from app.model import load_model_and_predict
from app.utils import is_image_valid
import io
from PIL import Image
import os
import uvicorn  # Import uvicorn to run the app
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.gzip import GZipMiddleware


# Initialize FastAPI app
app = FastAPI(title="Nike Shoe Classifier API")

# Add Middleware to handle large requests
app.add_middleware(GZipMiddleware, minimum_size=1000)  # Compress responses
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])  # Allow all hosts


@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    """
    Upload an image and get a prediction from the model.
    """
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
    """
    Root endpoint - Health check.
    """
    return {"message": "Welcome to the Nike Shoe Classifier API!"}

# Detect Render-assigned PORT dynamically

if __name__ == "__main__":
    port = os.environ.get("PORT")  # Get Render's assigned port
    print(f"🔥 Render Assigned PORT: {port}")  # Print it to logs

    if not port:
        port = 8000  # Default to 8000 if $PORT is not found
        print("⚠️ Warning: No $PORT found, defaulting to 8000")

    uvicorn.run(app, host="0.0.0.0", port=int(port))
