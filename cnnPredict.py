# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 23:17:33 2018

@author: abhi
"""

import cnnModel

def loadCNN(isBgModeOn):
    model = cnnModel.createCNNModel()
    model.summary()
    return model 
       
    
