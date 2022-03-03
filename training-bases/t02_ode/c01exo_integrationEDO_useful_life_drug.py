#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 09:07:21 2022

@author: reveillo
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def main(useful_life, intake_mg, intake_interval, intake_number, hours):

    def function(y, t):
        return - (np.log(2) / useful_life) * y # dy/dt: Change of mg

    intake_hours = [intake_interval * i for i in range(intake_number - 1)]
    initial_condition = intake_mg
    times = []
    solutions = []

    for intake_time in intake_hours:
        time = np.arange(intake_time, intake_time + intake_interval, 0.1)
        solution = odeint(function, initial_condition, time)

        initial_condition = solution[-1] + intake_mg

        times.extend(time)
        solutions.extend(solution)


    intake_time = intake_hours[-1] + intake_interval
    time = np.arange(intake_time, intake_time + 10 * intake_interval, 0.1)
    solution = odeint(function, initial_condition, time)
    times.extend(time)
    solutions.extend(solution)

    #Graphic details
    fig, ax = plt.subplots(figsize=(15, 10))

    plt.plot(times, solutions, label='Concentration in the Body(t)')

    if hours <= 60:
        step = 1
        rotation = "horizontal"
    elif hours <= 300:
        step = 5
        rotation = "vertical"
    else:
        step = 10
        rotation = "vertical"

    ax.set_xticklabels(np.arange(0, hours + 1, step, dtype=np.int), rotation=rotation)
    ax.set_xticks(np.arange(0, hours + 1, step))

    ax.set_xlim([0, hours])
    ax.set_ylim([0, max(solutions) * 1.05])
    ax.set_xlabel('Hours')
    ax.set_ylabel('Concentration')
    ax.legend(loc='best')
    ax.grid()

    plt.show()
    
    
main(3,1000,4,3,36)