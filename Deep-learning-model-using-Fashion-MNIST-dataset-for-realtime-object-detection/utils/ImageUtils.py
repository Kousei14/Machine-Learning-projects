import os
from PIL import Image
import numpy as np

def load_images_from_directory(directory, 
                               target_size = (28, 28)):
    images = []
    for filename in os.listdir(directory):
        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
            img_path = os.path.join(directory, filename)
            # Converts to grayscale
            img = Image.open(img_path).convert('L')
            # Resize to 28x28
            img = img.resize(target_size) 
            # Convert to an array
            img = np.array(img)
            # Scale the pixel values
            img = 255 - img 
            images.append(img)
            
    return np.array(images)