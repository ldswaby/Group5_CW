#!/usr/bin/env python3

""" Groupwork: to do vectorize1 using Python """

## Variables ##

__author__ = 'Luke Swaby (lds20@ic.ac.uk), ' \
             'Jinkai Sun (jingkai.sun20@imperial.ac.uk), ' \
             'Acacia Tang (t.tang20@imperial.ac.uk), ' \
             'Dengku Tang (dengkui.tang20@imperial.ac.uk)'
__version__ = '0.0.1'

## Imports ##

import numpy as np
import time

## Main ##

M = np.random.rand(1000, 1000)

def SumALLElements(M):
    """ sum all elements of a matrix """
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
