import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def ft_zoom(image_array: np.array) -> np.array:
    """
    Function to zoom an image from it's pixels rgb content array.
    Display the zoomed image.
    """

    zoom_image_array = image_array[100:500, 460:860, :]

    grayscale_image = (np.sum(zoom_image_array, axis=2) / 765) * 255

    one_ch_array = grayscale_image[:, :, np.newaxis]

    image_size = Image.fromarray(zoom_image_array).size
    print(f"The shape of image is: {one_ch_array.shape} or {image_size}")
    print(one_ch_array.astype(int))

    return one_ch_array.astype(int)


def manual_transpose(array):
    rows, cols, trash = array.shape
    transposed_array = np.empty((cols, rows), dtype=array.dtype)

    for i in range(cols):
        for j in range(rows):
            transposed_array[i, j] = array[j, i]
            trash += 1

    return transposed_array


def ft_rotate(image_array: np.array):
    """
    Function to rotate (transpose) the image.
    Display the rotated image.
    """

    transposed_array = ft_zoom(image_array)
    transposed_array_m = manual_transpose(transposed_array)
    transposed_array_m = np.squeeze(transposed_array_m)

    print(f"New shape after Transpose: {transposed_array_m.shape}")
    print(transposed_array_m)

    plt.imshow(transposed_array_m, cmap="gray")
    plt.show()
