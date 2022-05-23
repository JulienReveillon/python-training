#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  3 17:52:30 2022

@author: julienreveillon
"""


# Conditions d'utilisation ACU (Air Curtain Units : Eurovent)
# P03_calculations-Eurovent REC 16-1 - Recommendation for Air Curtain unit - First Edition - 2016 - EN
# 
#

  

# temperature data
tempCOut       = 10 # [C] outside constant temperature
tempCInit      = 12 # [C] initial initide temperature

# Aircurtain properties
# Air curtain mode :
#     'constant_dT'   : exiting air temperature  Tout = inlet air Tin + ACTemp_dT
#     'constant_Tout' : exiting air temperature  Tout = cte = tempCACOut
ACmode            = 'constant_Tout'
#
tempCACOut  = 40   # [C] temperature of exiting heated air (mode v)
ACTemp_dT   = 5    # [C] 
ACMassFlow  = 1    # [kg/s] of air/sec (= 0 if no Air Curtain)
 
#------------------------------------------------------------------------------   
#Room / door dimension et prop
#------------------------------------------------------------------------------
prof        = 6     # [m]
haut        = 4     # [m]       
larg        = 5     # [m]
overallHT   = 0.3   # [W/m2⋅K]
# Door opening
doorHaut    = 0     # [m] hauteur de porte
doorLarg    = 0     # [m] largeur de porte
#------------------------------------------------------------------------------

# Use of a thermostat
thermoFlag     = True
thermoTempCAim = 18   # [C] temperature aim then stopp heating
thermoTemp_dT  = 5    # [C] delta T before running heating devices again




    

# constant heating (electric coil), =0 if none
QConstantHeating  = 0   # [W] constantHeating : constant heating device, no air circulation

 

#
# Air
#
rhoAir      = 1.2    # [Kg/m^3]
cvAir       = 718    # [J/kg.K]
cpAir       = 1005   # [J/kg.K]