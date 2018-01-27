# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 21:23:35 2018

@author: abhi
"""
import cv2
import time

x0 = 400
y0 = 200
height = 200
width = 200
isBgModeOn = 0
isAdaptiveThresholdMode = True
roi = None

def saveROI(roi,isBgModeOn):
    
        signname = input("Enter a sign name \n")
        if isBgModeOn == 0:
            path="./AdaptiveThresholdModeDataSet/"
        elif isBgModeOn == 1:
            path="./BackgroundRemovalModeDataSet/"
        else:
            path="./NoFilterModeDataSet/"
        ts = int(time.time())
        name = signname + str(ts)
        print ("creating image...")
        cv2.imwrite(path+name + ".png", roi)
        print ("created image: "+str(name)+" for word " + str(signname))
        time.sleep(0.04 )
        

    