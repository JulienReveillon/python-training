#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 16:34:50 2022

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
    
    
### systeme a resoudre
def deriv_SIR(SYS, t, beta, gamma):
    S,I,R = SYS
    dSYSdt = [
       -S * I * beta,
        S * I * beta  - gamma * I ,
        gamma * I 
        ]
    return dSYSdt

def resolution_SIR(t,S0,I0,R0,beta,gamma):
    SYS0     = [S0,I0,R0]
    solution = odeint(deriv_SIR, SYS0, t, args = (beta,gamma,) )
    return solution[:,0],solution[:,1],solution[:,2]

# programme principal
if __name__ == '__main__':
    #
    t = np.arange(0, 30, 1)   #de 0 a 30 jours
    #
    S,I,R = resolution_SIR(t,0.8, 0.2,0,0.5,0.142)
    PlotFonction(t,S,0,xlabel='time',ylabel='percents',titre='S,I,R evolution',nomcourbe='Suceptible')
    PlotFonction(t,I,0,nomcourbe='Infectious')
    PlotFonction(t,R,0,nomcourbe='Recovered')
    



