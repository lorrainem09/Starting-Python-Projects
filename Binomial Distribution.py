#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#Attempt at binomial coin flip simulator and graphing all possible outcomes

@author: lorrainemarcelin
"""
import numpy as np
import matplotlib.pyplot as plt
from math import factorial as fac
from numpy import random
import seaborn as sns


#binomial distribution of:
# n = number of coin flips
# x = the value you are trying to get a probability of
# p = probability of specified option

def binomial_prob(n, x, p):
    return round( ( fac(n) / ( fac(x) * fac(n-x) ) ) * (p**x) * (1-p)**(n-x) , 5)

N=int(input("How many trials would you like to conduct?\n"))
X= int(input("You want the probability of getting what value of this outcome?\n"))
P= float(input("What is the probability of this occurence?\n"))
print(" The probability of your selected event occuring ", X ,"times ")
print("over the course of ", N," trials is:")
print((binomial_prob(N,X,P)))
print("")
print("The following is the binomial distribution of all possible outcomes\n")


sns.distplot(random.binomial(N, P, N), hist=False, label='binomial')   

plt.ylabel('Probability')
plt.xlabel('Number of Trials')
plt.show() 


