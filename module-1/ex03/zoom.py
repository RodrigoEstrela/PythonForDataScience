import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def ft_zoom(image_array: np.array):
    """
    Function to zoom an image from it's pixels rgb content array.
    Display the zoomed image.
    """
    print(image_array)
    
    zoom_image_array = image_array[100:500, 460:860, :]

    grayscale_image = (np.sum(zoom_image_array, axis=2) / 765) * 255

    single_channel_array = grayscale_image[:, :, np.newaxis]

    image_size = Image.fromarray(zoom_image_array).size
    print(f"New shape after slicing: {single_channel_array.shape} or {image_size}")
    print(single_channel_array.astype(int))

    plt.imshow(single_channel_array, cmap="gray")
    plt.show()
