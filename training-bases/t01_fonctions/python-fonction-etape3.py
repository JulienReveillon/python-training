#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 19:40:46 2022

@author: reveillo
"""

# librairie
import numpy as np
import matplotlib.pyplot as plt

# definition de fonction



# programme principal
if __name__ == "__main__":
    
    # axe x
    axeX = np.linspace(-10,10,200)
    
    # la fonction
    period = 4
    yFunc  = []
    for x in axeX:
        y = np.sin((2*np.pi/period)*x)
        yFunc.append(y)
        
    # tracer la fonction
    plt.figure(0)
    plt.plot(axeX,yFunc)
    plt.xlabel('x',fontsize=14)
    plt.ylabel('y',fontsize=14)
    plt.title('Fonction sinus')
    plt.grid(True) 
    plt.show()
    
    
    