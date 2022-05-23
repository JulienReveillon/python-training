#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 13 12:29:06 2022

@author: reveillo
"""

import numpy as np
import matplotlib.pyplot as plt
import aircurtain_parameters as acp


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
        
        

def C2K(TC):
    return TC+273.15

def K2C(TK):
    return TK-273.15

def initDimRoom():
    #
    L     = acp.larg
    P     = acp.prof
    H     = acp.haut
    wallU = acp.overallHT
    dL    = acp.doorLarg
    dH    = acp.doorHaut
    #
    roomDim     = [L,P,H]
    roomVol     =  L*P*H
    roomS       = 0  # surface with exchange with exterior (including ground minus door)
    # front and back
    roomS       = L*H*2+P*H*2+P*L*2
    doorDim     = [dL,dH]
    doorSurf    = dL*dH
    if doorSurf>0:
        doorOpen = True
        roomS   -= doorSurf   # substract door opening froma wall surface
    else:
        doorOpen = False
    #
    roomR = 1/(roomS*wallU)
    #
    return roomDim, roomVol, roomR, doorOpen, doorDim, doorSurf


def thermoRun(tempKroom,thermoFlag,thermoTempKAim,thermoTemp_dT):
    ind_lastTemp = len(tempKroom)-1
    if thermoFlag:
        if ind_lastTemp<=0:
            thermoRunFLag = True
        else:
            lastTemp     = tempKroom[ind_lastTemp]
            if lastTemp>thermoTempKAim:
                thermoRunFLag = False
            else:
                lastdT = tempKroom[ind_lastTemp]-tempKroom[ind_lastTemp-1]
                if lastdT>=0:
                    thermoRunFLag = True
                else:
                    if (thermoTempKAim-lastTemp)<thermoTemp_dT:
                        thermoRunFLag = False
                    else:
                        thermoRunFLag = True   
    else:
        thermoRunFLag = True 
    
    return thermoRunFLag