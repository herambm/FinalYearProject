import numpy as np
import cv2
from matplotlib import pyplot as plt
import time

images=['baby (1).png','baby (2).png','aboard (1).png','aboard (2).png','five (1).png','five (2).png','four (1).png','four (2).png','gone (1).png','gone (2).png','seven (1).png','seven (2).png','seven (3).png']


# Initiate SURF detector
surf = cv2.xfeatures2d.SURF_create()
# BFMatcher with default params
bf = cv2.BFMatcher()

# Perform thresholding for detecting hand
def thresholding(image):
    #resized_image = cv2.resize(image, (500, 500))
    # convert to grayscale
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # applying gaussian blur
    value = (35, 35)
    blurred = cv2.GaussianBlur(grey, value, 0)
    # thresholding: Otsu's Binarization method
    _, thresh1 = cv2.threshold(blurred, 127, 255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    return thresh1

# Descriptors for db images
db=[]
for image in images:
        img2 = cv2.imread(image,1)          
        thresh_img2=thresholding(img2)
        kp2, des2 = surf.detectAndCompute(thresh_img2,None)
        db.append((des2,image))

print("Descriptors have been calculated for database images")
print("Opening WebCam")

#timg='15.png'
#img1 = cv2.imread(timg,1)

count=100
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
        # read image
        ret, img = cap.read()
        
        if ret == True:
                # get hand data from the rectangle sub window on the screen
                cv2.rectangle(img, (400,400), (100,200), (0,255,0),0)
                cv2.imshow('input',img)
                crop_img = img[100:400, 200:400]
                thresh_img1=thresholding(crop_img)
                # find the keypoints and descriptors with SIFT
                kp1, des1 = surf.detectAndCompute(thresh_img1,None)
                # initialization
                matched_kp=0
                matched_img=""
                for a,b in db:
                    matches = bf.knnMatch(des1,a, k=2)
                    # Apply ratio test
                    good = []
                    for m,n in matches:
                        if m.distance < 0.75*n.distance:
                            good.append([m])
                    if matched_kp < len(good):
                        matched_kp=len(good)
                        #img3=img2
                        matched_img=b
                    #print("matched keypoints for {0} are {1}".format(b,len(good)))
        front,end=matched_img.split()                
        if count == 0:
            print(front)
            count=100
        if cv2.waitKey(1) & 0xff == ord('q'):
                break
        count=count-1
        
cap.release()
cv2.destroyAllWindows()
# cv2.drawMatchesKnn expects list of lists as matches.
#img4 = cv2.drawMatchesKnn(img1,kp1,img3,kp2,good,None,flags=2)
#plt.imshow(img4),plt.show()
