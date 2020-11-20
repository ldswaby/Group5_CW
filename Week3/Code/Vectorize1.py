#!/usr/bin/env python3

""" Groupwork: to do vectorize1 using Python """
# Script Name: Vectorize1.py
# Author: Jingkai Sun (ks3020@ic.ac.uk)

import numpy as np
import time

M = np.random.rand(1000, 1000)
# M = np.array(M)
# Dimensions = np.shape(M)

def SumALLElements(M):
    Tot = 0
    Dimensions = np.shape(M)
    for i in range(0, Dimensions[0]):
        for j in range(0, Dimensions[1]):
            Tot += M[i, j]
    return Tot

start1 = time.time()
SumALLElements(M)
print("SumALLElements takes %f s to run" % (time.time() - start1))

start2 = time.time()
# print(np.sum(M))
np.sum(M)
print("np.sum takes %f s to run" % (time.time() - start2))
