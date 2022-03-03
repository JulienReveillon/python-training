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
def MonSinus(axeX,period):
    yFunc  = []
    for x in axeX:
        y = np.sin((2*np.pi/period)*x)
        yFunc.append(y)    
    #    
    return yFunc


# programme principal
if __name__ == "__main__":
    
    # axe x
    axeX = np.linspace(-10,10,200)
    
    # la fonction
    yPeriod4 = MonSinus(axeX,4)
    yPeriod8 = MonSinus(axeX,8)
    

        
    # tracer la fonction
    plt.figure(0)
    plt.plot(axeX,yPeriod4)
    plt.plot(axeX,yPeriod8)
    plt.xlabel('x',fontsize=14)
    plt.ylabel('y',fontsize=14)
    plt.title('Fonction sinus')
    plt.grid(True) 
    plt.show()
    
    
    