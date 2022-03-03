# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# librairie
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint



### ETAPE 1

# population bacterie
def deriv_equaDiff(POP, t, G):
  dPOPdt = np.log(2)/G * POP
  return dPOPdt

# programme principal
if __name__ == "__main__":
    #
    #

    POP_0 = 100
    G = 4
    t = np.arange(0, 100, 1)

    # Résolution de l'équation différentielle avec ode 
    y = odeint(deriv_equaDiff, POP_0, t, args = (G,) )

    plt.figure(0)
    plt.xlabel("Time - hours",fontsize=14)
    plt.ylabel("Population",fontsize=14)
    plt.plot(t, y)
    plt.title('Bacteries population with G=4')
    
"""
### ETAPE 2

# population bacterie
# https://dridk.me/equation-differentielle.html
def deriv_equaDiff(POP, t, G):
  dPOPdt = np.log(2)/G * POP
  return dPOPdt


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

# programme principal
if __name__ == "__main__":
    #
    #

    POP_0   = 100
    G       = 4
    t       = np.arange(0, 100, 1)

    # Résolution de l'équation différentielle avec ode 
    y = odeint(deriv_equaDiff, POP_0, t, args = (G,) )

    PlotFonction(t,y,0,xlabel='time',ylabel='number of bacteries',titre='bacteries population with G=4')
"""
