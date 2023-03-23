# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:01:09 2023

@author: bchan
"""


# Data structures and analysis
import numpy as np

# Visualization
import matplotlib.pyplot as plt
import pyvista as pv


# This line reads information from the file into a 3D numpy array called img.
# The dimensions of the entire volume are stated below and used in reshape function call.
nz = 111
ny = 100
nx = 100

img = np.fromfile('fracture.raw', dtype=np.uint8)
img = img.reshape(nz,ny,nx)




#%%
###################################
# Problem 1:
# Create a 3D plot of the fracture surface using surface plotting from pyvista package.
# Choose a color of the surface of your choice.
# Play with the orientation of the plot to get a good view of the fracture - learn from the reference on camera position
# etc described here: https://docs.pyvista.org/api/core/camera.html or pyvista reference in general.
# Let the function save image in .png format using the specific choice of color and orientation.
# Bonus: figure out how to save enough .png frames to create a video (animation of the frames)
###################################
pl = pv.Plotter()
pl.set_background(color='w')

vtk_pore = pv.wrap(img)
pore_contours = vtk_pore.contour(isosurfaces=[0.5])

pl.add_mesh(pore_contours, opacity=0.9, color=(0/255, 0.25, 252/255))

pl.show()
        

#%%
####################################
# Problem 2:
# Your image in 3D is a stack in z-direction of 2D images ((x,y) plane).  For every (x,y) coordinate
# there is a column of nz values in img and those that are belonging to fracture (0s) have certain height
# that is called an aperture.
# Create a function called 'calculate_aperture' that takes 3D img array as an input and returns aperture field a.
# The function should also take "plot_a' input that can have 'y' and 'n' as input, and it plots
# histogram and 2D colorplot of aperture field (imshow) if plot_a = 'y').
#####################################

aperature = np.zeros((img.shape[1], img.shape[2]))

for j in range(img.shape[1]):
    for i in range(img.shape[2]):
        aperature[j, i] = np.count_nonzero(img[:, j, i] == 0)
        
plt.hist(aperature.flatten())

plt.figure(dpi=500)
plt.imshow(aperature)
plt.colorbar()

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
    aperature_size = field.shape[0] * field.shape[1]
    
    aperature_sum = 0
    for j in range(field.shape[1]):
        for i in range(field.shape[0]):
            aperature_sum += field[i, j]
            
    aperature_mean = aperature_sum / aperature_size
    return aperature_mean


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
            
    aperature_size = field.shape[0] * field.shape[1]        
    roughness_coeff = np.sqrt(roughness_sum / aperature_size)
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

