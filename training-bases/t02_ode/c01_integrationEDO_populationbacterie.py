#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 15:27:52 2022

@author: julienreveillon
"""

# librairie
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

### ETAPE 1


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

# population bacterie
def deriv_popBacteria(POP, t, G):
  dPOPdt = np.log(2)/G * POP
  return dPOPdt


# programme principal
if __name__ == "__main__":
    #
    # Conditins de calculs
    POP_0 = 100
    G     = 4
    #
    t = np.arange(0, 101, 1)
    #
    # Résolution de l'équation différentielle avec ode 
    POP  = odeint(deriv_popBacteria, POP_0, t, args = (G,) )
    #
    #
    G2   = 3.5
    POP2 = odeint(deriv_popBacteria, POP_0, t, args = (G2,) )
    
    
    #
    PlotFonction(t,POP,0,xlabel='time',ylabel='number of bacteries',titre='bacteries population',nomcourbe='G = 4')
    PlotFonction(t,POP2,0,nomcourbe='G = 3.5')
    
    


