#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:14:46 2022

@author: julienreveillon
"""
import sys
import numpy as np
import aircurtain_parameters as acp
import aircurtain_functions as acf


"""
# Déclaration des equations differentielles 
def deriv(y, t, Text, rhoair, Cpair, V,Rthmur, qmassair, Theater):
    QLoss, Qac, T = y
    
    rhoIn    = computeRhoGP(T)
    deltaRho = rhoIn-rhoOut
    meanRho  = (rhoIn+rhoOut)/2 
    QTotal = compute_TotalAirFlow(W, H, Cd, deltaP, deltaRho, meanRho, Cv, vitessevent)
    
    # Description des 2 equations differentielles 
    dQlossdt = (T-Text)/Rthmur
    dQacdt = qmassair*Cpair*(Theater-T) + compute_puissanceventilateur(rhoair,qmassair,deltaPventilateur)
    dTdt =(1/(rhoair*Cpair*V))* (dQacdt- dQlossdt+compute_puissanceventilateur(rhoair,qmassair,deltaPventilateur))   
    
    # systeme
    dydt = [dQlossdt, dQacdt ,dTdt] 
    return dydt 
"""

"""
def dSYSdT(SYS, t, QConstantHeating_t, ACMassFlow_t, ):
    # system :
    # 1- dTKin/dt  # K/s
    # 2- dQac/dt   # energy aircurtain to air
    TKin, Qac      = SYS
    #

    
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

    tempKOut          = acf.C2K(acp.tempCOut)     # [K]
    tempKInit         = acf.C2K(acp.tempCInit)    # [K]    
    # dimension of the room (LxPxHxVol)
    roomDim, roomVol, roomR, doorOpen, doorDim, doorSurf  = acf.initDimRoom()
    # unit conversion
    tempKACOut        = acf.C2K(acp.tempCACOut)   # [K]
    thermoTempKAim    = acf.C2K(acp.thermoTempCAim)

    
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
        # Thermostat on or off ?
        #
        thermoRunFLag = acf.thermoRun(tempKroom[:i-1],acp.thermoFlag,thermoTempKAim,acp.thermoTemp_dT)
        #
        if thermoRunFLag:
            QConstantHeating_t = acp.QConstantHeating
            ACMassFlow_t       = acp.ACMassFlow
        else: # shut down heating system
            QConstantHeating_t = 0
            ACMassFlow_t       = 0           
        #
        # air temperature equation
        QWallLoss0     = (tempKOut-tempK0)/roomR    
        QBalance0      = QConstantHeating_t+QWallLoss0+QACgain0
        RHS0           = QBalance0/(roomVol*acp.rhoAir*acp.cvAir) 
        tempK1         = tempK0+0.5*timeStep*RHS0
        #
        # air curtain equation
        if ACMassFlow_t>0 : #air curtain is ON
            if acp.ACmode=='constant_dT':
                RHS_AC0 = ACMassFlow_t*acp.cpAir*acp.ACTemp_dT
            elif acp.ACmode=='constant_Tout':
                RHS_AC0 = ACMassFlow_t*acp.cpAir*(tempKACOut-tempK0)
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
        RHS1           = QBalance1/(roomVol*acp.rhoAir*acp.cvAir) 
        tempKroom[i]   = tempK0 + timeStep*RHS1
        # air curtain equation
        if ACMassFlow_t>0 : #air curtain is ON
            if acp.ACmode=='constant_dT':
                RHS_AC1    = ACMassFlow_t*acp.cpAir*acp.ACTemp_dT
            elif acp.ACmode=='constant_Tout':
                RHS_AC1    = ACMassFlow_t*acp.cpAir*(tempKACOut-tempK1)
            else:  
                print('Error ACmode')
                sys.exit()
            QACgain[i] = QACgain1+timeStep*RHS_AC1
        else:
            QACgain[i] = 0     


        
    acf.PlotFonction(time/3600,acf.K2C(tempKroom),0,xlabel='time [h]',ylabel='temperature',titre='room temperature')
    acf.PlotFonction(time/3600,QACgain,1,xlabel='time [h]',ylabel='Q Air Curtain',titre='Aircurtain delivered heat')
       
        
      
    #https://github.com/Denzo77/room_heating_model/blob/master/room_model.py
    #https://www.mathworks.com/help/simulink/ug/model-a-house-heating-system.html
    #https://www.engineeringtoolbox.com/air-curtains-d_129.html
    




if __name__ == "__main__":
    
    # Conditions d'utilisation ACU (Air Curtain Units : Eurovent)
    # P03_calculations-Eurovent REC 16-1 - Recommendation for Air Curtain unit - First Edition - 2016 - EN
    # 
    #
    #    
    
    
    roomThermaModeling()
    
    


