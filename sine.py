#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 14:55:00 2019

@author: chenna
"""

import matplotlib.pyplot as plt
import numpy as np
f1=input("Enter the fist sinusoid frequency")
f2=input("Enter the second sinusoid frequency")
a=np.linspace(0,10,200)
fig=plt.figure()
ax1=fig.add_subplot(3,1,1)
ax2=fig.add_subplot(3,1,2)
ax3=fig.add_subplot(3,1,3)

x=np.sin(2*np.pi*a*(f1))
y=np.sin(2*np.pi*a*(f2))
z=x+y
ax3.set_title("Addition")
ax1.plot(a,x)
ax2.plot(a,y)
ax3.plot(a,z)