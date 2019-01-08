#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 16:06:46 2019

@author: chenna
"""

import matplotlib.pyplot as plt
import numpy as np
f=input("Enter the input frequency:")
p=input("Enter the phase angle:")
b=np.linspace(0,10,1000)
x=np.sin((2*np.pi*b*f))
y=np.sin((2*np.pi*b*f)+p)
fig=plt.figure()
ax1=fig.add_subplot(2,1,1)
ax3=fig.add_subplot(2,1,2)
ax1.plot(b,x)
ax3.set_title("Shifted sine wave")
ax3.plot(b,y)