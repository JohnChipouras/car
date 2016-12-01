#!/Users/jchipouras15/anaconda2/bin/python

%matplotlib notebook
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import math
#


#reading in an image
image = mpimg.imread('test_images/solidWhiteRight.jpg')
#printing out some stats and plotting
print('This image is:', type(image), 'with dimesions:', image.shape)
plt.imshow(image)  #call as plt.imshow(gray, cmap='gray') to show a grayscaled image
plt.show() #this actually gets the matplotlib to launch the viewer to see if the image changed... make sure you're running this in the correct env. and using python 3
