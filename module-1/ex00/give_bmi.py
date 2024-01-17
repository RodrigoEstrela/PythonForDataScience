import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Receives two lists of either ints or floats.
    First represents the height and the second the weight.
    Returns a list of bmi values for each pair of the input lists.
    BMI = kg/m2
    """
    height_array = np.array(height)
    weight_array = np.array(weight)

    result_array = weight_array / (height_array**2)
    result_list = result_array.tolist()
    return result_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Receives a list of either ints or floats.
    Returns a list with True (above the limit)
    or False (within the limit) for each received value
    """

    return [True if value > limit else False for value in bmi]
