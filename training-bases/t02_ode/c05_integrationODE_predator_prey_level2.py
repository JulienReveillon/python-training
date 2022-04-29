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
    
### systeme
def deriv_prey_pred(SYS, t, a, b, c, d):
    # 
    #    a: Taux de reproduction des proies.
    #    b: Taux de deces des prois (tues par les predateurs)
    #    c: Taux de reproduction des predateurs.
    #    d: Taux de deces des predateurs
    #
    x, y = SYS
    dSYSdt = [
        a * x     - b * x * y, # dx/dt: Change in Prey
        c * x * y - d * y      # dy/dt: Change in Pred
    ]    
    return dSYSdt


### systeme
def deriv_prey_pred_biotique(SYS, t, a, b, c, d, K):
    #    http://www.normalesup.org/~doulcier/teaching/mathematics/03_equationsDifferentielles.html
    # 
    #    a: Taux de reproduction des proies.
    #    b: Taux de deces des prois (tues par les predateurs)
    #    c: Taux de reproduction des predateurs.
    #    d: Taux de deces des predateurs
    #    K: capacité biothique des proies
    x, y = SYS
    dSYSdt = [
        a * x *(1-x/K)    - b * x * y, # dx/dt: Change in Prey
        c * x * y - d * y      # dy/dt: Change in Pred
    ]    
    return dSYSdt




def resolution_prey_pred(t,x0,y0,a,b,c,d):
    SYS0     = [x0,y0]
    solution = odeint(deriv_prey_pred, SYS0, t, args = (a,b,c,d,) )
    return solution[:,0],solution[:,1]


def resolution_prey_pred_biotique(t,x0,y0,a,b,c,d,K):
    SYS0     = [x0,y0]
    solution = odeint(deriv_prey_pred_biotique, SYS0, t, args = (a,b,c,d,K,) )
    return solution[:,0],solution[:,1]


# programme principal
if __name__ == "__main__":
    #
    # resolution systeme
    t = np.linspace(0, 2000, 3000)   #de 0 a 10 jours
    #
    prey,pred   = resolution_prey_pred(t,3.6,2.1,0.02,0.01,0.01,0.02)
    
    PlotFonction(t,prey,0,xlabel='time',ylabel='population',titre='evolution population',nomcourbe='prey - a = 2.22')
    PlotFonction(t,pred,0,nomcourbe='pred -  a = 2.22')
    
    prey2,pred2   = resolution_prey_pred(t,1.8,4,0.01,0.01,0.01,0.06)

    PlotFonction(t,prey2,0,xlabel='time',ylabel='population',titre='evolution population',nomcourbe='prey -  a = 4.22')
    PlotFonction(t,pred2,0,nomcourbe='pred -  a = 4.22')    
    
    preybiot,predbiot     = resolution_prey_pred_biotique(t,3.6,2.1,0.02,0.01,0.01,0.02,10)
    preybiot2,predbiot2   = resolution_prey_pred_biotique(t,1.8,4,0.01,0.01,0.01,0.06,10)
    
    PlotFonction(prey,pred,1,xlabel='prey',ylabel='pred',titre='Diagramme de phase',nomcourbe='trajectoire 1')
    PlotFonction(preybiot,predbiot,1,nomcourbe='trajectoire 1 - biot')
    PlotFonction(prey2,pred2,1,nomcourbe='trajectoire 2')
    PlotFonction(preybiot2,predbiot2,1,nomcourbe='trajectoire 2 - biot')
    
    plt.show()
    
    



    
