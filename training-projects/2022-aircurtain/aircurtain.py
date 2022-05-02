#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:14:46 2022

@author: julienreveillon
"""

import numpy as np
import matplotlib.pyplot as plt


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

def initWallRoom(roomDim):
        
    # wall definition
    wallRoom = []
    #format : 'name',surface,mode,R (resistance to heat transfer)
    wallR = 1.599e-6  # resitance to heat transfer  : here poor resistance
    #wallR = 10.
    surfPH = roomDim[1]*roomDim[2]
    surfPL = roomDim[0]*roomDim[1]
    surfHL = roomDim[0]*roomDim[2]
    # surf*wallR = wall conductance : Thermal conductance of room walls. Equivalent to U-value [W/K]
    
    wall = ['front',surfHL,wallR,surfHL/wallR]
    wallRoom.append(wall)
    wall = ['back',surfHL,wallR,surfHL/wallR]
    wallRoom.append(wall)
    wall = ['side1',surfPH,wallR,surfPH/wallR]
    wallRoom.append(wall)
    wall = ['side2',surfPH,wallR,surfPH/wallR]
    wallRoom.append(wall)
    wall = ['top',surfPL,wallR,surfPL/wallR]
    wallRoom.append(wall)
    wall = ['bottom',surfPL,0,0]  # sol adiabatique
    wallRoom.append(wall)
    
    # Thermal conductance is the time rate of steady state heat flow through a 
    # unit area of a material or construction induced by a unit temperature 
    # difference between the body surfaces, in W/m2⋅K.
    
    return wallRoom

def initDimRoom(L,P,H):
    roomDim = [L,P,H]
    roomVol =  L*P*H
    return roomDim, roomVol


def lossWallRoom(Tin,Text,wallRoom):
    #
    QWallLoss = 0
    for i in range(len(wallRoom)):
        QWallLoss += (Text-Tin)*wallRoom[i][3]   
    #
    return QWallLoss


def roomHeatingBase():
    """
    Compute the temperature evolution in a room with heating device + cold external atmosphere
    """
    # dimension of the room (LxPxHxVol)
    roomDim, roomVol  = initDimRoom(4.,6.,3.)
    wallRoom          = initWallRoom(roomDim)
    
    tempCout  = 10     # [C]
    tempCinit = 15     # [C]
    rhoAir    = 1.2    # [Kg/m^3]
    cvAir     = 1005   # [J/kg.K]
    Qheat     = 20   # [J/s]
    timeStep  = 0.1     # heure
    timeEnd   = 10000      # heure
    time      = np.arange(0,timeEnd,timeStep)
    nIter     = len(time)
    tempCroom    = np.zeros(nIter)
    tempCroom[0] = tempCinit
    for i in range(1,nIter):
        tempC        = tempCroom[i-1]
        QWallLoss0   = lossWallRoom(tempC,tempCout,wallRoom)
        RHS0         = (Qheat+QWallLoss0)/(roomVol*rhoAir*cvAir)
        tempC1       = tempC+0.5*timeStep*RHS0
        QWallLoss1   = lossWallRoom(tempC1,tempCout,wallRoom)
        RHS1         = (Qheat+QWallLoss1)/(roomVol*rhoAir*cvAir)
        tempCroom[i] = tempC + timeStep*RHS1
        
    PlotFonction(time,tempCroom,0,xlabel='time',ylabel='temperature',titre='room temperature')
       
        
        
        
        
    #https://github.com/Denzo77/room_heating_model/blob/master/room_model.py
    #https://www.mathworks.com/help/simulink/ug/model-a-house-heating-system.html








if __name__ == "__main__":
    roomHeatingBase()

