import numpy as np
import cv2
from PIL import Image, UnidentifiedImageError

def is_image_valid(image: Image.Image, min_resolution=(50, 50), blur_threshold=100):
    """
    Validate an image before processing.
    - Checks resolution (min 50x50)
    - Checks blurriness (Laplace variance threshold)
    - Ensures image is correctly formatted
    """
    try:
        # Convert image to RGB format
        image = image.convert("RGB")

        # Check resolution
        if image.width < min_resolution[0] or image.height < min_resolution[1]:
            return False, f"Resolution too low ({image.width}x{image.height})"

        # Convert to grayscale for blurriness detection
        gray = image.convert("L")
        laplacian_var = cv2.Laplacian(np.array(gray), cv2.CV_64F).var()

        if laplacian_var < blur_threshold:
            return False, f"Too blurry (Variance: {laplacian_var:.2f})"

        return True, "Valid image"
    
    except UnidentifiedImageError:
        return False, "Unidentified image format"
    
    except Exception as e:
        return False, f"Error: {e}"
