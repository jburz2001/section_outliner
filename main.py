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

def extractColor(img,x,y):
    px = img[int(x),int(y)]
    img[img != px] = 0
    
    return img

def extractColorToBinary(img,x,y):
    px = img[int(x),int(y)]
    img[img == px] = 255
    img[img != px] = 0
    
    return img

def openImg(img,kernalRs,kernalCs,iterations):
    kernel = np.ones((kernalRs,kernalCs),np.uint8)
    
    erosion = cv2.erode(img,kernel,iterations=iterations)
    opening = cv2.dilate(erosion,kernel,iterations=iterations)
    
    return opening

def closeImg(img,kernalRs,kernalCs,iterations):
    kernel = np.ones((kernalRs,kernalCs),np.uint8)
    
    dilation = cv2.dilate(img,kernel,iterations=iterations)
    closure = cv2.erode(dilation,kernel,iterations=iterations)
    
    return closure

def detectEdges(img,binary):
    if not binary:
        img = cv2.GaussianBlur(img,(3,3),sigmaX=0,sigmaY=0)
        
    sobel = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=7)
    
    thresh = 10
    canny = cv2.Canny(img,threshold1=thresh,threshold2=thresh)

    
    return sobel,canny

def edges(img,type):
    if type == "canny":
        locations =  np.where(img == 255.00)
    elif type == "sobel":
        locations = np.where(img == 255.00)
    
    coordinates = list(zip(locations[0], locations[1]))
    
    return coordinates

img = imgFromPath("afm.png")
plt.imshow(img)
plt.show()

ks = [2]
for k in ks:
    seg_img = segmentImg(img,k)
    # plt.imshow(seg_img)
    # plt.show()

x, y = 200, 200  
# x = input("x coordinate of pixel to represent outlined section(s)")
# y = input("y coordinate of pixel to represent outlined section(s)")

des_color = extractColor(seg_img,x,y)
# plt.imshow(des_color)
# plt.show()

des_binary = extractColorToBinary(seg_img,x,y)
# des_binary = cv2.cvtColor(des_binary,0)
# plt.imshow(des_binary)
# plt.show()

opened_img = openImg(des_binary,5,5,1)
# plt.imshow(opened_img)
# plt.show()


opened_closed_img = closeImg(opened_img,5,5,1)
plt.imshow(opened_closed_img)
plt.show()

sobel_img, canny_img = detectEdges(opened_closed_img,binary=True)
# plt.imshow(sobel_img)
# plt.show()

plt.imshow(canny_img)
plt.show()


edge_coords = edges(canny_img, "canny")
#print(edge_coords)

outlinedImg = img
for coord in edge_coords:
    outlinedImg[coord] = [33,248,246]

plt.imshow(outlinedImg)
plt.show()