import os
import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    """
    Function to print an image's pixel's rgb content
    """
    try:
        valid_extensions = {'.jpg', '.jpeg'}
        _, file_extension = os.path.splitext(path.lower())
        
        if file_extension not in valid_extensions:
            raise ValueError("Invalid extension. Supported: .jpg .jpeg")

        image = Image.open(path)
        image_array = np.array(image)

        print(f"The shape of image is: {image_array.shape}")    
        return image_array
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
