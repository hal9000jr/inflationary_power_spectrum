import numpy as np
import scipy as sp

'''
Here we will write the general for of the potential.
It should be numba 
'''

def V(phi):
  pot = m**2/2 * phi**2
  return pot

def dV(phi):
  dpot = m**2 * phi
  return dpot

def ddV(phi):
  ddpot = m**2
  return ddpot
  
