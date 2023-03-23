# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:01:09 2023

@author: bchan
"""

# IO
from hdf5storage import loadmat

# Data structures and analysis
import numpy as np

# Visualization
import matplotlib.pyplot as plt
import pyvista as pv


img = loadmat('./374_02_04_256.mat')['bin']

img = img[75:186, 100:200, 100:200]

# img.tofile('fracture.raw')




###################################
# Problem 1:
# Read in image and create a 3D plot of the fracture surface
###################################
pl = pv.Plotter()
pl.set_background(color='w')

vtk_pore = pv.wrap(img)
pore_contours = vtk_pore.contour(isosurfaces=[0.5])

pl.add_mesh(pore_contours, opacity=0.9, color=(0/255, 0.25, 252/255))

pl.show()
        


####################################
# Problem 2:
# Loop through each (x,y) index and compute the aperature (number of zeros)
#####################################

aperature = np.zeros((img.shape[1], img.shape[2]))

for j in range(img.shape[1]):
    for i in range(img.shape[2]):
        aperature[j, i] = np.count_nonzero(img[:, j, i] == 0)
        
plt.hist(aperature.flatten())

plt.figure(dpi=500)
plt.imshow(aperature)
plt.colorbar()


#####################################
# Problem 3:
# Min, Max, Avg. of aperature field
####################################

aperature_min = np.amin(aperature)
aperature_max = np.amax(aperature)
aperature_mean = np.mean(aperature)

####################################
# Problem 4a:
# Calculate the mechanical aperature (eq. 1 from paper)
###################################
aperature_size = aperature.shape[0] * aperature.shape[1]

aperature_sum = 0
for j in range(aperature.shape[1]):
    for i in range(aperature.shape[0]):
        aperature_sum += aperature[i, j]
        
aperature_mean = aperature_sum / aperature_size

####################################
# Problem 4b:
# Calculate the roughness coefficient (eq. 2 from paper)
###################################

roughness_sum = 0
for j in range(aperature.shape[1] - 1):
    for i in range(aperature.shape[0]):
        roughness_sum += (aperature[i, j+1] - aperature[i, j]) ** 2
        
        
roughness_coeff = np.sqrt(roughness_sum / aperature_size)

####################################
# Problem 4b:
# Calculate the tortuosity (eq. 3 from paper)
###################################

# roughness_sum = 0
# for j in range(aperature.shape[1]):
#     for i in range(aperature.shape[0]):
#         roughness_sum += (aperature[i, j+1] - aperature[i, j]) ** 2
        
        
# roughness_coeff = np.sqrt(roughness_sum / aperature_size)


