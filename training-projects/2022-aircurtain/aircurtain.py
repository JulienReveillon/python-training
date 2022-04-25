#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:14:46 2022

@author: julienreveillon
"""

import numpy as np

def C2K(TC):
    return TC+273.15

def K2C(TK):
    return TK-273.15

def initWallRoom(roomDim):
        
    # wall definition
    wallRoom = []
    #format : 'name',surface,mode,R (resistance to heat transfer)
    wallR = 1.25   # resitance to heat transfer  : here poor resistance
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
    roomDim.append(L*P*H)
    return roomDim


def roomHeatingBase():
    """
    Compute the temperature evolution in a room with heating device + cold external atmosphere
    """
    # dimension of the room (LxPxHxVol)
    roomDim  = initDimRoom(4.,6.,3.)
    wallRoom = initWallRoom(roomDim)
    
    tempCout  = 10     # [C]
    tempCinit = 15     # [C]
    rhoAir    = 1.2    # [Kg/m^3]
    cpAir     = 1005.0 # [J/kg.K]
    print(wallRoom)
    timeStep = 0.1     # heure
    timeEnd  = 10      # heure
    time     = np.arrange(0,timeEnd,timeStep)
    nIter    = len(time)
    tempCroom=[tempCinit]
    for t in time:
        
        
    #https://github.com/Denzo77/room_heating_model/blob/master/room_model.py
    #https://www.mathworks.com/help/simulink/ug/model-a-house-heating-system.html








if __name__ == "__main__":
    roomHeatingBase()

