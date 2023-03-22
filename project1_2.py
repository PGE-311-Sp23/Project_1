# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:01:09 2023

@author: bchan
"""


# Data structures and analysis
import numpy as np

# Visualization
# import matplotlib.pyplot as plt
# import pyvista as pv


# This line reads information from the file into a 3D numpy array called img.
# The dimensions of the entire volume are stated below and used in reshape function call.
nz = 111
ny = 100
nx = 100

img = np.fromfile('fracture.raw', dtype=np.uint8)
img = img.reshape(nz,ny,nx)





#%%
####################################
# Your image in 3D is a stack in z-direction of 2D images ((x,y) plane).  For every (x,y) coordinate
# there is a column of nz values in img and those that are belonging to fracture (0s) have certain height
# that is called an aperture.
# Create a function called 'create_aperture' that takes 3D img array as an input and returns aperture field a.

#####################################

aperture = np.zeros((img.shape[1], img.shape[2]))

for j in range(img.shape[1]):
    for i in range(img.shape[2]):
        aperture[j, i] = np.count_nonzero(img[:, j, i] == 0)
        

#%%
#####################################
# Problem 3:
# Define a function called "aperture_statistics" 
# that computes and returns the Minimum, Maximum of any aperture field.
# Execute this function using above aperture field a.
####################################
def aperture_statistics(field):
    return np.amin(field), np.amax(field)


#%%
####################################
# Problem 4:
# Define a function called "aperture_mean" 
# that calculates and returns the mechanical aperture (eq. 1 from paper in repo)
# Execute this function using above aperture field a.
###################################

def aperture_mean(field):
    aperture_size = field.shape[0] * field.shape[1]
    
    aperture_sum = 0
    for j in range(field.shape[1]):
        for i in range(field.shape[0]):
            aperture_sum += field[i, j]
            
    aperture_mean = aperture_sum / aperture_size
    return aperture_mean


#%%
####################################
# Problem 5:
# Define a function called "roughness_coeff" 
# that calculates and returns the roughness coefficient (eq. 2 from paper in repo)
# Execute this function using above aperture field a.
###################################

def roughness_coeff(field):
    roughness_sum = 0
    for j in range(field.shape[1] - 1):
        for i in range(field.shape[0]):
            roughness_sum += (field[i, j+1] - field[i, j]) ** 2
            
    aperture_size = field.shape[0] * field.shape[1]        
    roughness_coeff = np.sqrt(roughness_sum / aperture_size)
    return roughness_coeff


#%%
####################################
# Problem 6:
# Define a function called "tortuosity" 
# that calculates and returns the tortuosity (eq. 3 from paper in repo)
# Execute this function using above aperture field a.
###################################
def tortuosity(field):
    tortuosity_sum = 0
    tmp = np.zeros(field.shape[0])
    
    for i in range(field.shape[0]):
        tmp[i] = 0
        for j in range(field.shape[1] - 1):
            tmp[i] += np.sqrt((field[i,j+1]-field[i,j]) ** 2 + 1) 
            
        tortuosity_sum += tmp[i] / field.shape[0]
    tortuosity = tortuosity_sum / field.shape[1]
    return tortuosity

#%%
####################################
# Problem 7:
# Define a function called "perm" that calculates and returns permeability k
# Refer to volumetric flux estimate using cubic formula (ref. Problem 2B.3c in BSL, see readme file)
# where 2*B is equal to mean aperture calculated in Problem 4.
# Further, compare volumetric flux to Darcy's law to calculate permeability k of the "parallel plate" fracture with the
# same aperture as the mean (calculated in Problem 4)

###################################
def perm(field):
    B = aperture_mean(field) /2
    
    perm = (B ** 2)/ 3
    return perm

