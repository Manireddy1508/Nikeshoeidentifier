import numpy as np
import cv2
from PIL import Image, UnidentifiedImageError

def is_image_valid(image, min_resolution=(100, 100), blur_threshold=50):
    """
    Validate the uploaded image for resolution and blurriness.
    """
    try:
        # Ensure image is RGB
        image = image.convert("RGB")

        # Check resolution
        if image.width < min_resolution[0] or image.height < min_resolution[1]:
            return False, f"Resolution too low ({image.width}x{image.height})."

        # Convert to grayscale for blurriness detection
        gray = image.convert("L")
        laplacian_var = cv2.Laplacian(np.array(gray), cv2.CV_64F).var()

        if laplacian_var < blur_threshold:
            return False, f"Too blurry (Variance: {laplacian_var:.2f})."

        return True, "Valid image."

    except UnidentifiedImageError:
        return False, "Unidentified image format."
    except Exception as e:
        return False, f"Error: {e}"
