# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



# librairie
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def deriv(y, t, beta, gamma):
  S,I,R = y 
  # Description des 3 equations differentielles 
  dSdt = -S * I  * beta 
  dIdt = S * I  * beta  - gamma * I 
  dRdt = gamma * I 
  # systeme
  dydt = [dSdt, dIdt, dRdt]
  #
  return dydt 


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
if __name__ == '__main__':
    # Au temps t0,  70% sains, 30% infécté, 0 guéri 
    y0 = [0.7, 0.3, 0]

    # Evolution sur 28 jours 
    t = np.linspace(0, 28)

    # Paramètres du modèle 
    beta    = 0.5
    gamma   =  0.1

    # Resolution des équations differentielles 
    solution = odeint(deriv, y0, t, args = (beta, gamma))
    S        = solution[:,0]
    I        = solution[:,1]
    R        = solution[:,2]

    PlotFonction(t,S,0,xlabel='time',ylabel='Population proportion',titre='SIR with beta = 0.5 , gamma = 0.1',nomcourbe='Susceptible')
    plt.axis([0, max(t), 0, 1])
    PlotFonction(t,I,0,nomcourbe='Susceptible')
    PlotFonction(t,R,0,nomcourbe='Recovered',nomfichier='epidemieSIR.pdf')
