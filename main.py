#https://medium.com/nerd-for-tech/dominant-color-extraction-for-img-segmentation-2f30e9590889
#https://www.thepythoncode.com/article/kmeans-for-img-segmentation-opencv-python

import cv2
import numpy as np
import matplotlib.pyplot as plt

def imgFromPath(path):
    img = cv2.imread(path,1)
    orig_shape = img.shape
    print(orig_shape)

    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    return img
    
def segmentImg(img,k):
    # convert image to linear array
    pixel_values = np.float32(img.reshape((-1,3)))

    # define stopping criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

    _, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # convert back to 8 bit values
    centers = np.uint8(centers)

    # flatten the labels array
    labels = labels.flatten()

    # convert all pixels to the color of the centroids
    seg_img = centers[labels.flatten()]

    # reshape back to the original img dimension
    seg_img = seg_img.reshape(img.shape)
    
    return seg_img


path = "afm.png"
img = imgFromPath(path)
plt.imshow(img)
plt.show()

ks = [2]
for k in ks:
    seg_img = segmentImg(img,k)
    plt.imshow(seg_img)
    plt.show()