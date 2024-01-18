import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    """
    Function to print an image's pixel's rgb content
    """
    image = Image.open(path)
    image_array = np.array(image)

    print(f"The shape of image is: {image_array.shape}")    
    return image_array
