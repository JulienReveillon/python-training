#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:14:46 2022

@author: julienreveillon
"""
import sys
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

def initWallRoom(roomDim,wallU=0.4):
    # wallU overall heat loss coefficient u : W/(m^2*K)
    # wall definition
    wallRoom = []
    #format : 'name',surface,mode,U (resistance to heat transfer)
    #wallR = 10.
    surfPH = roomDim[1]*roomDim[2]
    surfPL = roomDim[0]*roomDim[1]
    surfHL = roomDim[0]*roomDim[2]
    # surf*wallR = wall conductance : Thermal conductance of room walls. Equivalent to U-value [W/K]
    
    wall = ['front',surfHL,wallU,surfHL*wallU]
    wallRoom.append(wall)
    wall = ['back',surfHL,wallU,surfHL*wallU]
    wallRoom.append(wall)
    wall = ['side1',surfPH,wallU,surfPH*wallU]
    wallRoom.append(wall)
    wall = ['side2',surfPH,wallU,surfPH*wallU]
    wallRoom.append(wall)
    wall = ['top',surfPL,wallU,surfPL*wallU]
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


def roomHeatingBase():
    """
    Compute the temperature evolution in a room with heating device + cold external atmosphere
    """
    #
    # Constant data
    #
    rhoAir      = 1.2    # [Kg/m^3]
    cvAir       = 718   # [J/kg.K]
    cpAir       = 1005
    #
    # Physical data
    # 
    ###################################################
    # temperature : outside and inital temp
    tempCOut    = 10     # [C]
    tempCInit   = 12     # [C]
    tempKOut    = C2K(tempCOut)     # [K]
    tempKInit   = C2K(tempCInit)    # [K]    
    # dimension of the room (LxPxHxVol)
    roomDim, roomVol  = initDimRoom(4.,6.,3.)
    wallRoom          = initWallRoom(roomDim,wallU=0.5)
    # heating devices
    # constant heating (electric coil), =0 if none
    QConstantHeating  = 0   # [W] constantHeating : constant heating device, no air circulation
    #
    tempCACOut        = 25  
    tempKACOut        = C2K(tempCACOut)   # [K]
    ACTemp_dT         = 5
    ACMassFlow        = 1 # kg of air/sec = 0 if no Air Curtain
    #ACmode            = 'constant_dT'
    ACmode            = 'constant_Tout'
    #
    #
    thermoFlag        = True
    thermoTempCAim    = 18
    thermoTemp_dT     = 5
    thermoTempKAim    = C2K(thermoTempCAim)
    #
    
    ###################################################
    #
    # Numerical data
    # 
    timeStep    = 0.1     # heure
    timeEnd     = 10000      # heure
    time        = np.arange(0,timeEnd,timeStep)
    nIter       = len(time)
    tempKroom   = np.zeros(nIter)
    QACgain     = np.zeros(nIter)
    #
    # Initialization
    # 
    tempKroom[0]= tempKInit 
    #
    for i in range(1,nIter):
        #
        # first stage RK2
        tempK0         = tempKroom[i-1]
        QACgain0       = QACgain[0]
        #
        # THermostat on or off ?
        #
        thermoRunFLag = thermoRun(tempKroom[:i-1],thermoFlag,thermoTempKAim,thermoTemp_dT)
        #
        if thermoRunFLag:
            QConstantHeating_t = QConstantHeating
            ACMassFlow_t       = ACMassFlow
        else: # shut down heating system
            QConstantHeating_t = 0
            ACMassFlow_t       = 0           
        #
        # air temperature equation
        QWallLoss0     = lossWallRoom(tempK0,tempKOut,wallRoom)     # tempCOut constant
        QBalance0      = QConstantHeating_t+QWallLoss0+QACgain0
        RHS0           = QBalance0/(roomVol*rhoAir*cvAir) 
        tempK1         = tempK0+0.5*timeStep*RHS0
        #
        # air curtain equation
        if ACMassFlow_t>0 : #air curtain is ON
            if ACmode=='constant_dT':
                RHS_AC0 = ACMassFlow_t*cpAir*ACTemp_dT
            elif ACmode=='constant_Tout':
                RHS_AC0 = ACMassFlow_t*cpAir*(tempKACOut-tempK0)
            else:
                print('Error ACmode')
                sys.exit()
            QACgain1   = QACgain0+0.5*timeStep*RHS_AC0
        else:
            RHS_AC0    = 0     
            QACgain1   = 0
        # 
        # second stage RK2
        # air temperature equation
        QWallLoss1     = lossWallRoom(tempK1,tempKOut,wallRoom)
        QBalance1      = QConstantHeating_t+QWallLoss1+QACgain1
        RHS1           = QBalance1/(roomVol*rhoAir*cvAir) 
        tempKroom[i]   = tempK0 + timeStep*RHS1
        # air curtain equation
        if ACMassFlow_t>0 : #air curtain is ON
            if ACmode=='constant_dT':
                RHS_AC1    = ACMassFlow_t*cpAir*ACTemp_dT
            elif ACmode=='constant_Tout':
                RHS_AC1    = ACMassFlow_t*cpAir*(tempKACOut-tempK1)
            else:
                print('Error ACmode')
                sys.exit()
            QACgain[i] = QACgain1+timeStep*RHS_AC1
        else:
            QACgain[i] = 0     


        
    PlotFonction(time/3600,K2C(tempKroom),0,xlabel='time [h]',ylabel='temperature',titre='room temperature')
    PlotFonction(time/3600,QACgain,1,xlabel='time [h]',ylabel='Q Air Curtain',titre='Aircurtain delivered heat')
       
        
      
        
        
    #https://github.com/Denzo77/room_heating_model/blob/master/room_model.py
    #https://www.mathworks.com/help/simulink/ug/model-a-house-heating-system.html
    #https://www.engineeringtoolbox.com/air-curtains-d_129.html








if __name__ == "__main__":
    roomHeatingBase()

