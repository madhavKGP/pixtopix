import numpy as np
from PIL import Image

# Resize and normalize image
def preprocess_image(image: Image.Image) -> np.ndarray:
    image = image.resize((256, 256))
    img = np.asarray(image)
    img = (img - 127.5) / 127.5           # between -1 to +1  for tanh activation
    img = np.expand_dims(img, axis=0)
    return img

# Convert output back to image
def postprocess_image(output_array: np.ndarray) -> Image.Image:
    output_array = (output_array + 1) / 2.0
    img = (output_array[0] * 255).astype(np.uint8)
    return Image.fromarray(img)
