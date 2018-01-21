# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:55:41 2018

@author: abhi
"""

import cv2
import numpy as np
import os
import time
import convolutionalNeuralNetwork as cnn

minValue = 70

x0 = 400
y0 = 200
height = 200
width = 200
bgModel = None
isBgModeOn = 0
isAdaptiveThresholdMode = True 
roi = None
isPredictionMode = False
mod= None

#remove background
def removeBG(frame):
    fgmask = bgModel.apply(frame)
    res = cv2.bitwise_and(frame, frame, mask=fgmask)
    return res
    
#binary mask is borrowed from     
def adaptiveThresholdMode(frame, x0, y0, width, height ):
    
    #global guessGesture, visualize, mod, lastgesture, saveImg
    cv2.rectangle(frame, (x0,y0),(x0+width,y0+height),(0,255,0),1)
    roi = frame[y0:y0+height, x0:x0+width]
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)  
    blur = cv2.GaussianBlur(gray,(5,5),2)
    res = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
    return res    
    
def backgroundremovalMode(frame, x0, y0, width, height ):
    #global guessGesture, visualize, mod, lastgesture, saveImg   
    cv2.rectangle(frame, (x0,y0),(x0+width,y0+height),(0,255,0),1)
    roi = frame[y0:y0+height, x0:x0+width]
    #remove background
    roi = removeBG(roi)
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),2)
    res = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
    return res
    
def Main():
    global isAdaptiveThresholdMode, isBgModeOn, bgModel,x0,y0,roi,isPredictionMode,mod
    isQuit=0
    cap = cv2.VideoCapture(0)
    ret = cap.set(3,640)
    ret = cap.set(4,480)
    while(True):
        ret, frame = cap.read()
        #invert frame
        frame = cv2.flip(frame, 3)
        
        if ret == True:
            if isAdaptiveThresholdMode == True:
                roi = adaptiveThresholdMode(frame, x0, y0, width, height)
            else:
                roi = backgroundremovalMode(frame, x0, y0, width, height)
            if isPredictionMode : 
               cnn.guessGesture(mod, roi)
               
               
        cv2.imshow('Original',frame) 
        if not isQuit:
            cv2.imshow('ROI', roi)  
            
        key = cv2.waitKey(10) & 0xff  
        if key == ord('c'):
            isAdaptiveThresholdMode = not isAdaptiveThresholdMode
            if isAdaptiveThresholdMode:
                print ("Adaptive Threshold Mode active")
                bgModel= None
                isBgModeOn = 0
            else:
                print ("Background Removal Mode active")
                bgModel = cv2.createBackgroundSubtractorMOG2()
                isBgModeOn = 1
            if isPredictionMode:    
               mod = cnn.loadCNN(isBgModeOn)
        elif key == ord('p'):
               isPredictionMode = not isPredictionMode
               if isPredictionMode:
                    mod = cnn.loadCNN(isBgModeOn)
               print ("Prediction Mode - {}".format(isPredictionMode))
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
         
    
