import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Image 11.JPG',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)

plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
plt.title(titles[i])
plt.xticks([]),plt.yticks([])

plt.show()


