#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:14:46 2022

@author: julienreveillon
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
import aircurtain_parameters as ac


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

def initDimRoom(L,P,H,wallU=0.4):
    roomDim     = [L,P,H]
    roomVol     =  L*P*H
    roomS       = 0  # surface with exchange with exterior (including ground minus door)
    # front and back
    roomS = L*H*2+P*H*2+P*L*2
    roomR = 1/(roomS*wallU)
    
    return roomDim, roomVol, roomR


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

"""
def dSYSdT(SYS, t, QConstantHeating_t, ACMassFlow_t):
    # system :
    # 1- dTin/dt
    # 2- dQac/dt
    Tin, Qac = SYS
    #
    QWallLoss0     = (tempKOut-Tin)/roomR    
    QBalance0      = QConstantHeating_t+QWallLoss0+QACgain0
    RHS0           = QBalance0/(roomVol*ac.rhoAir*ac.cvAir)
    
    return SYS
"""




def roomThermaModeling():
    """
    Compute the temperature evolution in a room with heating device + cold external atmosphere
    """

    #
    # Physical data
    # 
    ###################################################
    # temperature : outside and inital temp

    tempKOut          = C2K(ac.tempCOut)     # [K]
    tempKInit         = C2K(ac.tempCInit)    # [K]    
    # dimension of the room (LxPxHxVol)
    roomDim, roomVol,roomR  = initDimRoom(ac.larg,ac.prof,ac.haut,ac.overallRT)

    # unit conversion
    tempKACOut        = C2K(ac.tempCACOut)   # [K]
    thermoTempKAim    = C2K(ac.thermoTempCAim)

    
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
        thermoRunFLag = thermoRun(tempKroom[:i-1],ac.thermoFlag,thermoTempKAim,ac.thermoTemp_dT)
        #
        if thermoRunFLag:
            QConstantHeating_t = ac.QConstantHeating
            ACMassFlow_t       = ac.ACMassFlow
        else: # shut down heating system
            QConstantHeating_t = 0
            ACMassFlow_t       = 0           
        #
        # air temperature equation
        QWallLoss0     = (tempKOut-tempK0)/roomR    
        QBalance0      = QConstantHeating_t+QWallLoss0+QACgain0
        RHS0           = QBalance0/(roomVol*ac.rhoAir*ac.cvAir) 
        tempK1         = tempK0+0.5*timeStep*RHS0
        #
        # air curtain equation
        if ACMassFlow_t>0 : #air curtain is ON
            if ac.ACmode=='constant_dT':
                RHS_AC0 = ACMassFlow_t*ac.cpAir*ac.ACTemp_dT
            elif ac.ACmode=='constant_Tout':
                RHS_AC0 = ACMassFlow_t*ac.cpAir*(tempKACOut-tempK0)
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
        QWallLoss1     = (tempKOut-tempK1)/roomR
        QBalance1      = QConstantHeating_t+QWallLoss1+QACgain1
        RHS1           = QBalance1/(roomVol*ac.rhoAir*ac.cvAir) 
        tempKroom[i]   = tempK0 + timeStep*RHS1
        # air curtain equation
        if ACMassFlow_t>0 : #air curtain is ON
            if ac.ACmode=='constant_dT':
                RHS_AC1    = ACMassFlow_t*ac.cpAir*ac.ACTemp_dT
            elif ac.ACmode=='constant_Tout':
                RHS_AC1    = ACMassFlow_t*ac.cpAir*(tempKACOut-tempK1)
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
    roomThermaModeling()

