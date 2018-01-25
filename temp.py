# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 01:09:23 2018

@author: abhi
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:55:41 2018

@author: abhi
"""

import cv2
import cnnPredict
import cnnFilters
import cnnTrain
import cnnModel
import cnnCreateDataSet
import time
import os

x0 = 400
y0 = 200
height = 200
width = 200
isBgModeOn = 0
isAdaptiveThresholdMode = True
roi = None
isPredictionMode = False
model= None
menu = "\n c-Change Filter\n p-Predict Sign\n n-Save ROI in data set \n q-Close ROI Window \n w-Move ROI Upside\n s-Move ROI Downside\n a-Move ROI Rightside\n d-Move ROI Leftside\n ESC-exit\n"

#remove background

def Main():
    global isAdaptiveThresholdMode, isBgModeOn,x0,y0,roi,isPredictionMode,model,menu
    isQuit=0
    cap = cv2.VideoCapture(0)
    ret = cap.set(3,640)
    ret = cap.set(4,480)
    i=0
    j=0
    signnamearray = ["Aboard", "Baby", "Bowl","Friend"," House" ,"IorMe","Money","Opposite","Prisoner","You"]
    cv2.namedWindow('Original', cv2.WINDOW_NORMAL)    
    while(True):
        ret, frame = cap.read()
        #invert frame
        frame = cv2.flip(frame, 3)

        roi1 = cnnFilters.adaptiveThresholdMode(frame, x0, y0, width, height)
        roi2 = cnnFilters.backgroundremovalMode(frame, x0, y0, width, height)
        roi3 = cnnFilters.noFilterMode(frame, x0, y0, width, height)
        cv2.imshow('Sign Language Detactor',frame)

        if not isQuit:
            cv2.imshow('ROI1', roi1)
            cv2.imshow('ROI2', roi2)
            cv2.imshow('ROI3', roi3)



        key = cv2.waitKey(10) & 0xff

        if key == ord('n'):
            '''
            signname = input("Enter a sign name \n")
            '''
            signname = signnamearray[i]
            path1="./AdaptiveThresholdModeDataSet/"
            path2="./BackgroundRemovalModeDataSet/"
            path3="./NoFilterModeDataSet/"
            ts = int(time.time())
            name = signname + str(ts)
            print ("creating image...")
            cv2.imwrite(path1+name + str(j) + "1.png", roi1)
            cv2.imwrite(path2+name + str(j) + "2.png", roi2)
            cv2.imwrite(path3+name + str(j) + "3.png", roi3)
            print ("created image: "+str(signname)+ " " + str(j) + " for word " + str(signname))
            j=j+1
            if(j==10):
              i=i+1
              j=0
              duration = 1  # second
              freq = 440  # Hz
              os.system('spd-say "Change The Gesture"')
              if(i==10):
                  break
            time.sleep(0.04 )
        elif key == ord('q'):
             isQuit = not isQuit
        elif key == ord('w'):
            y0 = y0 - 5
        elif key == ord('s'):
            y0 = y0 + 5
        elif key == ord('a'):
            x0 = x0 - 5
        elif key == ord('d'):
            x0 = x0 + 5
        elif key == 27:
            break;
    cap.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    Main()
    
    """
    path = './AdaptiveThresholdModeDataSet'
    listing = os.listdir(path)
    dataset = []
    for name in listing:
        from scipy.ndimage import imread
        image2 = imread(path+"/"+name)
        #image2.reshape(200,200,1)
        x,y = image2.shape
        if(x!=200 or y!=200):
            print(name)
            if(name[0]=='A'):
                print(name)
                os.remove(path+"/"+name)
                newf=path+"/" + "Aboard151686741401.png"
                gray_image = imread(newf)
                cv2.imwrite(path+"/"+name, gray_image)
                print(name)
            if(name[0]=="F"):
                print(name)
                os.remove(path+"/"+name)
                newf=path+"/" + "Friend151686753831.png"
                gray_image = imread(newf)
                cv2.imwrite(path+"/"+name, gray_image)
                print(name)
            if(name[0]==" "):
                print(name)
                os.remove(path+"/"+name)
                newf=path+"/" + " House151686755801.png"
                gray_image = imread(newf)
                cv2.imwrite(path+"/"+name, gray_image)
                print(name)
            if(name[0]=="M"):
                print(name)
                os.remove(path+"/"+name)
                newf=path+"/" + "Money151686597951.png"
                gray_image = imread(newf)
                cv2.imwrite(path+"/"+name, gray_image)
                print(name)
            if(name[0]=="I"):
                print(name)
                os.remove(path+"/"+name)
                newf=path+"/" + "IorMe151686592121.png"
                gray_image = imread(newf)
                cv2.imwrite(path+"/"+name, gray_image)
                print(name)
            if(name[0]=="O"):
                print(name)
                os.remove(path+"/"+name)
                newf=path+"/" + "Opposite151686766701.png"
                gray_image = imread(newf)
                cv2.imwrite(path+"/"+name, gray_image)
                print(name)
            if(name[0]=="P"):
                print(name)
                os.remove(path+"/"+name)
                newf=path+"/" + "Prisoner151686693531.png"
                gray_image = imread(newf)
                cv2.imwrite(path+"/"+name, gray_image)
                print(name)
            if(name[0]=="Y"):
                print(name)
                os.remove(path+"/"+name)
                newf=path+"/" + "You151686179261.png"
                gray_image = imread(newf)
                cv2.imwrite(path+"/"+name, gray_image)
                print(name)
            if(name[0]=="B" and name[1]=="o"):
                print(name)
                os.remove(path+"/"+name)
                newf=path+"/" + "Bowl151686572011.png"
                gray_image = imread(newf)
                cv2.imwrite(path+"/"+name, gray_image)
                print(name)
            if(name[0]=="B" and name[1]== "a"):
                print(name)
                os.remove(path+"/"+name)
                newf=path+"/" + "Baby151686747081.png"
                gray_image = imread(newf)
                cv2.imwrite(path+"/"+name, gray_image)
                print(name)
                "'"


