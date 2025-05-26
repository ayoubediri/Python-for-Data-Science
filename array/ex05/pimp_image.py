import numpy as np
from PIL import Image


def ft_invert(array) -> np.ndarray:
    """
    Inverts the colors of the image array.
    """
    if isinstance(array, np.ndarray):
        raise TypeError("The type of the parameter is not numpy.ndarray")
    new_array = 255 - array.copy()
    image = Image.fromarray(new_array)
    image.show()
def ft_red(array) -> np.ndarray:
    """
    The red color of the image array.
    """
    if type(array) != np.ndarray:
        raise TypeError("The type of the parameter is not numpy.ndarray")
    new_array = array.copy()
    new_array[:, :, 1:] = 0 
    print(new_array)
    image = Image.fromarray(new_array)
    image.show()
    
def ft_green(array) -> np.ndarray:
    """
    The green color of the image array.
    """
    if type(array) != np.ndarray:
        raise TypeError("The type of the parameter is not numpy.ndarray")
    new_array = array.copy()
    new_array[:, :, 0] = 0
    new_array[:, :, 2] = 0
    print(new_array)
    image = Image.fromarray(new_array)
    image.show()

def ft_blue(array) -> np.ndarray:
    """
    The green color of the image array.
    """
    if type(array) != np.ndarray:
        raise TypeError("The type of the parameter is not numpy.ndarray")
    new_array = array.copy()
    new_array[:, :, :2] = 0
    print(new_array)
    image = Image.fromarray(new_array)
    image.show()
    
def ft_grey(array) -> np.ndarray:
    """
    The grey color of the image array.
    """
    if type(array) != np.ndarray:
        raise TypeError("The type of the parameter is not numpy.ndarray")
    new_array = array.copy()
    grey = new_array[:, :, 2]
    new_array[:, :, 0] = grey
    new_array[:, :, 1] = grey
    new_array[:, :, 2] = grey
    print(new_array)
    Image.fromarray(new_array).show()
    return new_array
