#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: lorrainemarcelin

Fitting model to experimental data of the HIV viral load in a person over the course
of 10 days

"""

import numpy as np
import matplotlib.pyplot as plt

#Creating model of HIV data
time = np.linspace(0, 10, 101)
B=0
A=150000
alpha=0.5
beta = 50
viral_load_model = A * np.exp(-alpha*time) + B * np.exp(-beta*time)
#importing HIVseries.npz and separating data into two arrays
home_dir = "/Users/lorrainemarcelin/"
data_dir = home_dir + "Downloads/PMLSdata/01HIVseries/"
data_set = np.load(data_dir + "HIVseries.npz")
concentration = data_set['viral_load']
time_data = data_set['time_in_days']
#Fitting model to experimental data
plt.plot(time_data,concentration,label = "Experimental Data" )
plt.plot(time,viral_load_model,label='Model')
plt.xlabel("Time in Days")
plt.ylabel("Concentration of Viral Load")
plt.title("Time vs Concentration Fitting Experimental Data", size=24 , weight='bold')
plt.legend(loc="upper right")
plt.show()

