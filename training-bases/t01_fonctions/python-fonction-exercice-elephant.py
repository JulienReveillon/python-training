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

# ecrire ici  vos fonctions

def CroissanceElephant(time,N0=100,r=0.15,K=7500):
    popElephants  = []
    for t in time:
        pop = K/(N0+np.exp(-r*t)*(K-N0))
        popElephants.append(pop)    
    #    
    return popElephants

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


# programme principal
if __name__ == "__main__":
    
# ecrire ici  votre programme principal
# axe x
    time = np.linspace(0,100,500)
    pop  = CroissanceElephant(time)
    pop2 = CroissanceElephant(time,N0=100,r=0.05,K=6500)
    pop3 = CroissanceElephant(time,N0=100,r=0.01,K=3000)
    PlotFonction(time,pop,0,xlabel='years',ylabel='population',titre='Elephant population evolution',nomcourbe='r=0.15 - K=7500')
    PlotFonction(time,pop2,0,nomcourbe='r=0.1 - K=6500')
    PlotFonction(time,pop3,0,nomcourbe='r=0.05 - K=3000',nomfichier='elephants_niveau1.pdf')

# derniere ligne
    plt.show() #affichage ecran graphes
    
    
    
    
    