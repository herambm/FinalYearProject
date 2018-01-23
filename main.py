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

x0 = 400
y0 = 200
height = 200
width = 200
isBgModeOn = 0
isAdaptiveThresholdMode = True
roi = None
isPredictionMode = False
model= None

#remove background

def Main():
    global isAdaptiveThresholdMode, isBgModeOn,x0,y0,roi,isPredictionMode,model
    isQuit=0
    cap = cv2.VideoCapture(0)
    ret = cap.set(3,640)
    ret = cap.set(4,480)
    switch_case = input("\nWhat would you like to do ? \n 1) Train the model \n 2) predict Sign \n")
    if(switch_case==1):
        a=1
    elif(switch_case==2):
      while(True):
        ret, frame = cap.read()
        #invert frame
        frame = cv2.flip(frame, 3)

        if ret == True:
            if isAdaptiveThresholdMode == True:
                roi = cnnFilters.adaptiveThresholdMode(frame, x0, y0, width, height)
            else:
                roi = cnnFilters.backgroundremovalMode(frame, x0, y0, width, height)
            if isPredictionMode :
                cnnPredict.predictSign(roi,model)

        cv2.imshow('Sign Language Detactor',frame)

        if not isQuit:
            cv2.imshow('ROI', roi)

        key = cv2.waitKey(10) & 0xff

        if key == ord('c'):
            isAdaptiveThresholdMode = not isAdaptiveThresholdMode
            if isAdaptiveThresholdMode:
                print ("Adaptive Threshold Mode active")
                isBgModeOn = 0
            else:
                print ("Background Removal Mode active")
                isBgModeOn = 1
            if isPredictionMode:
                   model=cnnModel.createCNNModel(isBgModeOn)
        elif key == ord('p'):
               isPredictionMode = not isPredictionMode
               if isPredictionMode:
                   model=cnnModel.createCNNModel(isBgModeOn)
               print ("Prediction Mode - {}".format(isPredictionMode))
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
      
    else:
        print ("Please book an appointment with ophthalmologist!")



if __name__ == "__main__":
    Main()


