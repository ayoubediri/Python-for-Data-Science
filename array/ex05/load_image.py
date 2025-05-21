import numpy as np
from PIL import Image
def ft_load(path: str) -> np.ndarray:
    try:
        img = Image.open(path)
        if (img.mode != 'RGB'):
            img = img.convert('RGB')
        img_array = np.array(img)
        print(img_array)
        return img_array
    except FileNotFoundError:
        print("Error: Image file not found. Please check the path.")
    except Exception as e:
        print(f"An error occurred: {e}")