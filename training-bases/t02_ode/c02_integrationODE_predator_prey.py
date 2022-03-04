#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 15:55:44 2022

@author: julienreveillon
"""

# librairie
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def PlotFonction(x,y,numfigure,xlabel='',ylabel='',titre='',nomcourbe='',nomfichier=''):
    #
    plt.figure(numfigure)
    plt.grid(True) 
    #
    if nomcourbe: # plot with label
        plt.plot(x,y,label=nomcourbe)
    else:     # plot without label
        plt.plot(x,y)
    #
    if xlabel:
        plt.xlabel(xlabel,fontsize=14)
    #
    if ylabel:
        plt.ylabel(ylabel,fontsize=14)
    #
    if nomcourbe:
        plt.legend(loc='best')
    #
    if titre:
        plt.title(titre)
    #
    if nomfichier:
        plt.savefig(nomfichier)
    plt.show() 
    
### systeme
def deriv_pred_prey(SYS, t, a, b, c, d):
    x, y = SYS
    dSYSdt = [
        a * x     - b * x * y, # dx/dt: Change in Rabbits
        c * x * y - d * y      # dy/dt: Change in Foxes
    ]    
    return dSYSdt


def resolution_pred_prey(t,x0,y0,a,b,c,d):
    SYS0     = [x0,y0]
    solution = odeint(deriv_pred_prey, SYS0, t, args = (a,b,c,d,) )
    return solution[:,0],solution[:,1]


# programme principal
if __name__ == "__main__":
    #
    # resolution systeme
    t = np.arange(0, 10, 0.01)   #de 0 a 10 jours
    #
    prey,pred   = resolution_pred_prey(t,5,2,2.22,0.92,1.09,0.72)
    
    PlotFonction(t,prey,0,xlabel='time',ylabel='population',titre='evolution population',nomcourbe='prey - a = 2.22')
    PlotFonction(t,pred,0,nomcourbe='pred -  a = 2.22')
    
    prey2,pred2   = resolution_pred_prey(t,5,2,4.22,0.92,1.09,0.72)

    PlotFonction(t,prey2,0,xlabel='time',ylabel='population',titre='evolution population',nomcourbe='prey -  a = 4.22')
    PlotFonction(t,pred2,0,nomcourbe='pred -  a = 4.22')    
    
    
    



    
