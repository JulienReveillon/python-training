#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 19:32:37 2022

@author: reveillo
"""

# librairie
import numpy as np
import matplotlib.pyplot as plt

# definition des fonctions

def MinMaxMoy(data):
    #
    N    = len(data)
    dataMax = -1e30
    dataMin =  1e30
    dataMoy =  0
    for d in data:
        if d>dataMax:
            dataMax=d
        if d<dataMin:
            dataMin=d
        dataMoy = dataMoy + d
    dataMoy= dataMoy/N
    #
    return dataMin, dataMax, dataMoy
    
    

# programme principal
if __name__ == "__main__":
    
    echantillon = np.random.uniform(0,1,1000)
    eMin, eMax, eMoy = MinMaxMoy(echantillon)   
    print(eMin,eMax,eMoy)   
    
    
    echantillon2 = np.random.uniform(-1,1,1000)
    eMin2, eMax2, eMoy2 = MinMaxMoy(echantillon2)
    print(eMin2,eMax2,eMoy2)
    
    
    
    