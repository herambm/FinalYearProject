# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 23:27:18 2018

@author: abhi
"""
import cv2

removeBGModel = cv2.createBackgroundSubtractorMOG2()
#remove background
def removeBG(frame):
    
    global removeBGModel
    fgmask = removeBGModel.apply(frame)
    res = cv2.bitwise_and(frame, frame, mask=fgmask)
    return res
    
#binary mask is borrowed from     
def adaptiveThresholdMode(frame, x0, y0, width, height ):
    
    cv2.rectangle(frame, (x0,y0),(x0+width,y0+height),(0,255,0),1)
    roi = frame[y0:y0+height, x0:x0+width]
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)  
    blur = cv2.GaussianBlur(gray,(5,5),2)
    res = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
    return res    
    
def backgroundremovalMode(frame, x0, y0, width, height ):
     
    cv2.rectangle(frame, (x0,y0),(x0+width,y0+height),(0,255,0),1)
    roi = frame[y0:y0+height, x0:x0+width]
    #remove background
    roi = removeBG(roi)
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),2)
    res = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
    return res