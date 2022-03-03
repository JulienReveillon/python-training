#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 19:10:47 2022

@author: reveillo
"""

# librairie
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    
    # Etape 1
    echantillon = np.random.uniform(0,1,1000)
    
    # Etape 2 - calcul min, max, moy
    N    = len(echantillon)
    eMax = -1e30
    eMin =  1e30
    eMoy =  0
    for e in echantillon:
        if e>eMax:
            eMax=e
        if e<eMin:
            eMin=e
        eMoy = eMoy + e
    eMoy= eMoy/N
    
    #Sortie Informations
    print(eMin,eMax,eMoy)     


    
    