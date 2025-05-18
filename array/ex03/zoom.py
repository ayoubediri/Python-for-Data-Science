from load_image import ft_load
from PIL import Image
import numpy as np

def ft_zoom(path : str) :
    img = ft_load(path)
    print(f"The shape of image is: {img.shape}")
    print(img)
    img = img[-600:-200, -500:-100]
    image = Image.fromarray(img)
    image = image.convert('L')
    print(image.mode)
    img_array = np.array(image)
    img_array = np.expand_dims(img_array, axis=-1)
    print(f"New shape after slicing: {img_array.shape}")
    print(img_array)
    image.show()

if __name__ == "__main__":
    ft_zoom("animal.jpeg")