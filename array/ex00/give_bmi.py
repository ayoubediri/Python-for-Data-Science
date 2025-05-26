import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
    This function takes in two lists: height and weight,

    and returns a list of BMI values.

    The BMI is calculated using the formula: weight / (height ** 2)

    The height should be in meters and weight in kilograms.

    The function raises a ValueError if the

    height or weight is less than or equal to 0.

    The function raises a TypeError if the height or weight is not a number.

    The function raises a ValueError if the

    height and weight lists are not of the same length.

    Parameters:

    height (list[int | float]): A list of heights in meters.

    weight (list[int | float]): A list of weights in kilograms.

    Returns:

    list[int | float]: A list of BMI values.

    Raises:

    ValueError: If height or weight is less than or equal to 0.

    TypeError: If height or weight is not a number.

    valueError: If height and weight lists are not of the same length.

    Example:
    >>> give_bmi([1.75, 1.80], [70, 80])
    [22.86, 24.69]
    """
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of the same length.")
    for (h, w) in zip(height, weight):
        if h <= 0 or w <= 0:
            raise ValueError("Height and weight must be positive numbers.")
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError("Height and weight must be numbers.")
    height = np.array(height)
    weight = np.array(weight)
    return (weight / (height ** 2)).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    This function takes in a list of BMI values and a limit,

    and returns a list of booleans indicating

    whether each BMI value is less than the limit.

    The function raises a TypeError if the limit is not a number.

    The function raises a ValueError if the limit is less than or equal to 0.

    The function raises a TypeError if the BMI values are not numbers.

    Parameters:

    bmi (list[int | float]): A list of BMI values.

    limit (int): A limit value.

    Returns:

    list[bool]: A list of booleans indicating whether each BMI

    value is less than the limit.
    """
    if not isinstance(limit, (int, float)):
        raise TypeError("Limit must be a number.")
    if limit <= 0:
        raise ValueError("Limit must be a positive number.")
    if not all(isinstance(x, (int, float)) for x in bmi):
        raise TypeError("All BMI values must be numbers.")
    return np.vectorize(lambda x: x < limit)(bmi).tolist()
