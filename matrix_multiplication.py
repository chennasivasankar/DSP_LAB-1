#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 16:25:09 2019

@author: chenna
"""

import numpy as np
a=input("Enter the matrix A as [[a,b],[c,d]]:")
b=input("Enter the matrix B as [[a,b],[c,d]]:")
x=np.matmul(a,b)
print x