#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 09:14:28 2022

@author: reveillo
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def main(rabbits_birthrate, rabbits_deathrate, foxes_birthrate, foxes_deathrate, initial_rabbits, initial_foxes, days):

    def function(s, t):
        x, y = s
        dydt = [
            rabbits_birthrate * x     - rabbits_deathrate * x * y, # dx/dy: Change in Rabbits
            foxes_birthrate   * x * y - foxes_deathrate   * y      # dy/dt: Change in Foxes
        ]

        return dydt

    time = np.arange(0, days, 0.01)
    initial_conditions = [initial_rabbits, initial_foxes]
    solution = odeint(function, initial_conditions, time)

    #Graphic details
    fig, axes = plt.subplots(1, 2, figsize=(15, 10))

    ax = axes[0]

    ax.plot(time, solution[:, 0], label='Prey(t)')
    ax.plot(time, solution[:, 1], label='Predator(t)')

    if days <= 30:
        step = 1
        rotation = "horizontal"
    elif days <= 150:
        step = 5
        rotation = "vertical"
    else:
        step = 10
        rotation = "vertical"

    ax.set_xticklabels(np.arange(0, days + 1, step, dtype=np.int), rotation=rotation)
    ax.set_xticks(np.arange(0, days + 1, step))

    ax.set_xlim([0, days])
    ax.set_ylim([0, max(max(solution[:, 0]), max(solution[:, 1])) * 1.05])
    ax.set_xlabel('Time')
    ax.set_ylabel('Population')
    ax.legend(loc='best')
    ax.grid()


    ax = axes[1]

    ax.plot(solution[:, 0], solution[:, 1], label='Predator vs Prey')

    ax.set_xlim([0, max(solution[:, 0]) * 1.05])
    ax.set_ylim([0, max(solution[:, 1]) * 1.05])
    ax.set_xlabel('Preys')
    ax.set_ylabel('Predators')
    ax.legend(loc='best')
    ax.grid()

    plt.tight_layout()
    plt.show()

main(2.22,0.92,1.09,0.72,5,2,10)