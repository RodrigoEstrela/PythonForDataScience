import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Function to return a slice of the input 2d array
    """
    try:
        if not isinstance(family, list):
            raise ValueError("Input must be a list")

        if not all(isinstance(sublist, list) for sublist in family):
            raise ValueError("All input list elements must be lists.")

        sublists_sizes = set(len(sublist) for sublist in family)
        if len(sublists_sizes) != 1:
            raise ValueError("All sublists must have the same size")

        array2d = np.array(family)
        print(f"My shape is: {array2d.shape}")

        sliced_array2d = array2d[start:end]
        print(f"My new shape is: {sliced_array2d.shape}")

        return sliced_array2d.tolist()

    except ValueError as e:
        print(f"Error: {e}")
