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
    
    
### systeme a resoudre
def deriv_SIR(SYS, t, beta, gamma):
    S,I,R = SYS
    dSYSdt = [
       -S * I * beta,
        S * I * beta  - gamma * I ,
        gamma * I 
        ]
    return dSYSdt

### systeme a resoudre
def deriv_SIR_looseIm(SYS, t, beta, gamma, nu):
    S,I,R = SYS
    dSYSdt = [
       -S * I * beta  + nu * R,
        S * I * beta  - gamma * I ,
        gamma * I     - nu * R
        ]
    return dSYSdt

### systeme a resoudre
def deriv_SIRV(SYS, t, beta, gamma, nu, p):
    S,I,R,V = SYS
    dSYSdt = [
       -S * I * beta  + nu * R - p * S,
        S * I * beta  - gamma * I ,
        gamma * I     - nu * R,
        p * S
        ]
    return dSYSdt


### systeme a resoudre
def deriv_SIRV(SYS, t, beta, gamma, nu, p):
    S,I,R,V = SYS
    dSYSdt = [
       -S * I * beta  + nu * R - p * S,
        S * I * beta  - gamma * I ,
        gamma * I     - nu * R,
        p * S
        ]
    return dSYSdt### systeme a resoudre

def deriv_SIZD(SYS, t, sigma, beta, deltaS, deltaL, alpha, rho, xi):
        S,I,Z,D = SYS
        dSYSdt = [
            sigma - beta*S*Z - deltaS*S + xi*S*Z ,
            beta*S*Z - rho*I - deltaL*I,
            rho*I     - alpha*S*Z - xi*S*Z,
            deltaS*S  + deltaL*I + alpha*S*Z
            ]
        return dSYSdt


def resolution_SIR(t,S0,I0,R0,beta,gamma):
    SYS0     = [S0,I0,R0]
    solution = odeint(deriv_SIR, SYS0, t, args = (beta,gamma,) )
    return solution[:,0],solution[:,1],solution[:,2]


def resolution_SIR_looseIm(t,S0,I0,R0,beta,gamma,nu):
    SYS0     = [S0,I0,R0]
    solution = odeint(deriv_SIR_looseIm, SYS0, t, args = (beta,gamma,nu,) )
    return solution[:,0],solution[:,1],solution[:,2]


def resolution_SIRV(t,S0,I0,R0,V0,beta,gamma,nu,p):
    SYS0     = [S0,I0,R0,V0]
    solution = odeint(deriv_SIRV, SYS0, t, args = (beta,gamma,nu,p,) )
    return solution[:,0],solution[:,1],solution[:,2],solution[:,3]

def resolution_SIZD(t,S0,I0,Z0,D0,sigma,beta,deltaS,deltaL,alpha,rho,xi):
    SYS0     = [S0,I0,Z0,D0]
    solution = odeint(deriv_SIZD, SYS0, t, args = (sigma,beta,deltaS,deltaL,alpha,rho,xi,) )
    return solution[:,0],solution[:,1],solution[:,2],solution[:,3]

# programme principal
if __name__ == '__main__':
    #
    t = np.arange(0, 800, 0.1)   #de 0 a 800 heures, toutes ls 6 miniutes (1/10 heures)
    #
    S,I,R = resolution_SIR(t,50,1,0,0.0013,0.008333)
    PlotFonction(t,S,0,xlabel='time',ylabel='Pop',titre='S,I,R evolution',nomcourbe='Suceptible')
    PlotFonction(t,I,0,nomcourbe='Infectious')
    PlotFonction(t,R,0,nomcourbe='Recovered')
    
    t = np.arange(0, 4000, 0.1)  
    S,I,R = resolution_SIR_looseIm(t,50,1,0,0.0013,0.008333, 0.0004)
    PlotFonction(t,S,1,xlabel='time',ylabel='Pop',titre='S,I,R evolution',nomcourbe='Suceptible')
    PlotFonction(t,I,1,nomcourbe='Infectious')
    PlotFonction(t,R,1,nomcourbe='Recovered')
    
    
    t = np.arange(0, 4000, 0.1)    
    S,I,R,V = resolution_SIRV(t,50,1,0,0,0.0013,0.008333, 0.0004, 0.005)
    PlotFonction(t,S,2,xlabel='time',ylabel='Pop',titre='S,I,R evolution',nomcourbe='Suceptible')
    PlotFonction(t,I,2,nomcourbe='Infectious')
    PlotFonction(t,R,2,nomcourbe='Recovered')
    PlotFonction(t,V,2,nomcourbe='Vaccinated')
    
    t = np.arange(0, 6, 0.1)   
    S,I,Z,D = resolution_SIZD(t,50,0,1,0,0.3,0.42,0.001,0.03,0.08,1.3,0)
    PlotFonction(t,S,3,xlabel='time',ylabel='Pop',titre='S,I,Z,D evolution',nomcourbe='Suceptible')
    PlotFonction(t,I,3,nomcourbe='Infectious')
    PlotFonction(t,Z,3,nomcourbe='Zombies')
    PlotFonction(t,D,3,nomcourbe='Dead')
    
    plt.show()



