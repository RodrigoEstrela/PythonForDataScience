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
