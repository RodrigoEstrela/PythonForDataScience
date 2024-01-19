import numpy as np
from numpy import array
import matplotlib.pyplot as plt


def ft_invert(array) -> array:
    """
    Inverts the color of the image received
    """
    inverted_array = 255 - array
    plt.imshow(inverted_array)
    plt.show()
    return inverted_array


def ft_red(array) -> array:
    """
    Turns the color to red
    """
    red_array = array * [1, 0, 0]
    plt.imshow(red_array)
    plt.show()
    return red_array


def ft_green(array) -> array:
    """
    Turns the color to green
    """
    green_array = array - [255, 0, 255]
    plt.imshow(green_array)
    plt.show()
    return green_array


def ft_blue(array) -> array:
    """
    Turns the color to blue
    """
    blue_array = array.copy()
    blue_array[:, :, 0] = 0
    blue_array[:, :, 1] = 0
    plt.imshow(blue_array)
    plt.show()
    return blue_array


def ft_grey(array) -> array:
    """
    Turns the color to grey
    """
    grey_array = (np.sum(array, axis=2) / 765) / 0.0039215686
    plt.imshow(grey_array, cmap="gray")
    plt.show()
    return grey_array
