import numpy as np
import cv2
from matplotlib import pyplot as plt

images=['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png','10.png','11.png','12.png','13.png','14.png','16.png','17.png','18.png','19.png']

# Perform thresholding for detecting hand
def thresholding(image):
    #resized_image = cv2.resize(image, (500, 500))
    # applying gaussian blur
    value = (35, 35)
    blurred = cv2.GaussianBlur(image, value, 0)
    # thresholding: Otsu's Binarization method
    _, thresh1 = cv2.threshold(blurred, 127, 255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    return thresh1

timg='15.png'
img1 = cv2.imread(timg,0)          
thresh_img1=thresholding(img1)

# Initiate SURF detector
sift = cv2.xfeatures2d.SURF_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(thresh_img1,None)

# BFMatcher with default params
bf = cv2.BFMatcher()

# initialization
matched_kp=0
matched_img=""
for image in images:
    img2 = cv2.imread(image,0)          
    thresh_img2=thresholding(img2)
    kp2, des2 = sift.detectAndCompute(thresh_img2,None)

    matches = bf.knnMatch(des1,des2, k=2)
    
    # Apply ratio test
    good = []
    for m,n in matches:
        if m.distance < 0.75*n.distance:
            good.append([m])
    if matched_kp < len(good):
        matched_kp=len(good)
        img3=img2
        matched_img=image
    print("matched keypoints for {0} are {1}".format(image,len(good)))
print("Image {0} has been matched with {1}".format(timg,matched_img))
# cv2.drawMatchesKnn expects list of lists as matches.
img4 = cv2.drawMatchesKnn(img1,kp1,img3,kp2,good,None,flags=2)
plt.imshow(img4),plt.show()
