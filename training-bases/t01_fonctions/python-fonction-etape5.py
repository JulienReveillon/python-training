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


def PlotFonction(x,y,numfigure,xlabel,ylabel,titre,nomcourbe='',nomfichier=''):
    plt.figure(numfigure)
    plt.plot(x,y,label=nomcourbe)
    plt.xlabel(xlabel,fontsize=14)
    plt.ylabel(ylabel,fontsize=14)
    if nomcourbe:
        plt.legend(loc='best')
    plt.title(titre)
    plt.grid(True) 
    if nomfichier:
        plt.savefig(nomfichier)
  


# programme principal
if __name__ == "__main__":
    
    # axe x
    axeX = np.linspace(-10,10,200)
    
    # la fonction
    yPeriod4 = MonSinus(axeX,4)
    yPeriod8 = MonSinus(axeX,8)
    

        
    # tracer la fonction
    PlotFonction(axeX,yPeriod4,0,'x','y(x)','fonction sinus',nomcourbe='period 4',nomfichier='sinx.pdf')    
    PlotFonction(axeX,yPeriod8,0,'x','y(x)','fonction sinus',nomcourbe='period 8',nomfichier='sinx.pdf')
    plt.show()      
    
    
    
    
    