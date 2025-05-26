from load_image import ft_load
from PIL import Image
import numpy as np


def ft_rotate(path: str):
    img = ft_load(path)
    img = img[-600:-200, -500:-100]
    image = Image.fromarray(img)
    image = image.convert('L')
    img_array = np.array(image)
    img_array = np.expand_dims(img_array, axis=-1)
    print(f"The shape of image is: {img_array.shape}")
    print(img_array)
    image = image.transpose(Image.ROTATE_90)
    image_array = np.array(image)
    print(f"New shape after Transpose: {image_array.shape}")
    print(image_array)
    image.show()


if __name__ == "__main__":
    ft_rotate("animal.jpeg")
