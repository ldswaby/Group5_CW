#!/usr/bin/env python3

""" Groupwork: to do vectorize2 using Python """

## Variables ##

__author__ = 'Luke Swaby (lds20@ic.ac.uk), ' \
             'Jinkai Sun (jingkai.sun20@imperial.ac.uk), ' \
             'Acacia Tang (t.tang20@imperial.ac.uk), ' \
             'Dengku Tang (dengkui.tang20@imperial.ac.uk)'
__version__ = '0.0.1'

## Imports ##

import random as rd
import numpy as np
import math as mt
import time

## Functions ##

def stochrick(p0=[rd.uniform(0.5, 1.5) for i in range(0, 1000)], r=1.2, K=1, sigma=0.2, numyears=100):
    """ Computing euqation using loop """
    #initialize
    nought = [0 for i in range(0, 1000)]
    N = [nought for x in range(0, 100)]
    N.insert(0, p0)

    for pop in range(0, len(p0)):
        for yr in range(1, numyears):
            N[yr][pop] = N[yr - 1][pop] * mt.exp(r * (1 - N[yr - 1][pop] / K) + rd.normalvariate(0, sigma))

    return N


start1 = time.time()
stochrick()
print("stockrick takes %f s to run" % (time.time() - start1))

def stockrickvect1(p0=np.random.uniform(0.5, 1.5, 1000), r=1.2, K=1, sigma=0.2, numyears=100):
    """ Vectorization """
    N = np.zeros(shape=(100, 1000))
    N = np.insert(N, 0, p0, axis=0)
    for yr in range(1, numyears):
        N[yr] = N[yr - 1] * \
            np.exp(r * (1 - N[yr - 1] / K) + np.random.normal(0, sigma, 1))
    return N

start2 = time.time()
stockrickvect1()
print("Vectorization1 using numpy takes %f s to run" % (time.time() - start2))