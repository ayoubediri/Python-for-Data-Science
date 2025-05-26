import numpy as np


def check_uneven_lists(arr: list) -> bool:
    lengths = [len(sublist) for sublist in arr]
    return len(set(lengths)) > 1


def slice_me(family: list, start: int, end: int) -> list:
    if (isinstance(family, list) or
            isinstance(start, int) or
            isinstance(end, int)):
        raise TypeError("family must be a list. start and end must be ints")
    if check_uneven_lists(family):
        raise ValueError("All sublists must have the same length")
    arr = np.array(family)
    print(f"My shape is : {arr.shape}")
    arr = arr[start:end]
    print(f"My new shape is : {arr.shape}")
    return arr.tolist()
