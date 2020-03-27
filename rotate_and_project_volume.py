import numpy as np
import SimpleITK as sitk
from scipy.ndimage import rotate
from matplotlib import pyplot as plt

"""
Example for loading a CT volume and rotating it around the longitudinal axis.

The code loads a CT volume, rotates it 0, 30, 60, ..., and 330 degrees
and displays the intermediate results as a slideshow. 

The images displayed are in order (left to right)
1. Volume projected onto 0th axis
2. Volume projected onto 1st axis
3. Volume prohected onto 2nd axis
"""

# note that this example is made with CT data
path = 'PATH/TO/VOLUME/HERE'

# use SimpleITK to load a CT stack
image = sitk.ReadImage(path)
image = sitk.GetArrayFromImage(image)

# shift the intensity values so that the background intensity is 0
image = image - np.min(image)

print(image.shape)

plt.ion()
plt.subplots(1, 3)
for deg in range(0, 360, 30):
    plt.clf() # this prevents the images from persisting in memory

    # rotate the volume along the longitudinal axis
    rotated_im = rotate(image, deg, axes=(1, 2), reshape=False, order=1)
    
    for i in range(3):
        plt.subplot(1, 3, i + 1)
        plt.imshow(np.mean(rotated_im, i), cmap='gray') 
        # Replace mean with max for maximum intensity projection

    plt.suptitle('Rotated {} degrees'.format(deg))
    plt.tight_layout()
    plt.pause(.1)
