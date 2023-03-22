# Project_1

### Introduction: fractures in subsurface and their importance
Fractures are ubiquitous in subsurface and represent the “agents of change”: fracturing in itself is a multiscale process, and whether it happens naturally or not, it fundamentally changes the mechanical (solid and flow) properties of the medium.  Fractures span length scales from micrometer to millimeter cracks to kilometer faults. In addition, many fracture surfaces are permeable and represent connection to pathways of different length scale: those in a rock matrix or neighboring soil. The current understanding of the (multiphase) fluid flow in fractured systems, as well as its role in closing and opening fractures is limited because of multiple length scales of observation as well as modeling necessary to tackle the problem.

Just like fractured porous media themselves, the practical applications involving them span a multitude of engineering disciplines and scales of interest: from environmental remediation, geothermal energy exploitation to hydrocarbon recovery. From the subsurface engineer perspective, hydraulic fracturing is the most common method of stimulation of hydrocarbon reservoirs with aim of opening more surfaces for collection of fluids. Proppants (e.g. sand whose grains are up to 10 times larger than the host rock grains) are placed to keep them open during production. These opened fractures often connect to the fractures already present in the subsurface. Production from tight reservoirs (those of unusually small porosity and permeability), for instance, hinges on connectivity/permeability of natural fractures and the way they interact with the hydraulic fractures. While fractures play a key role in geomechanical stability of engineering infrastructure, for the purpose of this introduction we show some natural fractures we encounter in unconventional reservoirs (Figure 1) as well as interplay of hydraulic fractures and such formations (Figure 2).

![image](/images/image1.png)

*Figure 1. Rough fracture examples on small scales. (left) Barnett shale sample with partially mineralized natural fracture  – mineralization within fracture is visible in white. Partially mineralized fractures have potential of being open at very large depth as they are propped open by cements. Photo from Dr. Julia Gale, BEG, UT Austin. (right) Natural fracture in Mesaverde sandstone, Piceance basin, courtesy of P. Eichhubl, BEG, UT Austin. The fracture is partially cemented with quartz creating a restricted but open pore network within the fracture.*


 ![image](/images/Image2.png)
 
*Figure 2. a) and b) Example of hydraulically fractured core from HTFS1 site (Gale, Elliot and Laubach 2018) with proppant sand shown filling some of the fractures.*


Last motivational example outside of the oil and gas applications in  development of geothermal reservoirs called enhanced geothermal reservoirs directly depends on developing an open fracture network in hot dry rock (typically granite, does not have a lot of porosity beyond fractures) through which the working fluid is continually circulated.  The schematic in Figure 3 shows such a network.



 ![image](/images/Image3.png)
 
*Figure 3: Schematic of an enhanced geothermal reservoir with injection (yellow) and production well.*




### Definitions for this project
Fracture geometry is the key property that influences its flow properties, and aperture (defined below) is one of the most common ones. You will model fractures often as parallel plates (for instance in your Transport Phenomena in Geosystems or Geomechanics classes), but they are often rough, and not so simple as the figures above show. Here we will exercise at statistical fracture description and will analyze it based on image. This could be an X-ray image coming from a scanner imaging experiment (Dr. Espinoza has one in the basement in CPE, and Dr. DiCarlo has another, of different spatial resolution in the basement of GLT).
In this project we will work with an image of a fracture data from Digital Rocks Portal(https://www.digitalrocksportal.org/projects/372/origin_data/2132/) that has dimensions Nx=100 by Ny=100 by Nz=111. Let’s call that image (numpy array) ‘img’.  For every image location (k,j,i) in numpy 3D array notation corresponds to z-location k, y-location j and x-location i. The image value, img(k,j,i) is 0 where the fracture (open space is), and 1 where solid space is. The location of fracture surfaces is then defined by implicit value of 0.5 that is sitting right in between those values of 0 and 1. Schematic of example top and bottom fracture surfaces is shown in Figure 4.
 ![image](/images/Image4.png)
 
*Figure 4. A schematic of a fracture enclosed by two surfaces (shown in gray).(left) The aperture a(j,i) for our purposes is defined as a vertical (z-direction) distance between two planes at the location (j,i). In our discretized world, then, we will define aperture at every point (i,j) of the fracture image. Parallel plate model (often used for fractures) from the Transport Phenomena textbook by Bird, Stewart and Lightfoot textbook used in PGE 322K.(right) Here the aperture is the same everywhere and equal 2B.*


- (10 points)Problem 1: Create a 3D plot of the fracture surface and upload either an image or an animation(5 bonus points) into your repo.
- (20 points)Problem 2: Create aperture field called a based on a 3D array called img, upload a histogram plot and a 2D colorplot of this aperture field a into your repo.
- (14 points)Problem 3: Calculate the Minimum, Maximum of aperture field a.
- (14 points)Problem 4: Calculate the Mean aperture of aperture field a. (eq. 1 from paper in repo)
- (14 points)Problem 5: Calculate the roughness coefficient of aperture field a. (eq. 2 from paper in repo)
- (14 points)Problem 6: Calculate the tortuosity of aperture field a. (eq. 3 from paper in repo)
- (14 points)Problem 7: Estimate the permeability $k$ by comparing volumetric flux equation from parallel plate model with Darcy's law.

Volumetric flux equation:

$$
Q = W\int_{-B}^{B} v_z dx = \frac{2W(P_0-P_L)B^3}{3\mu L}
$$

$$
q = \frac{Q}{A}= \frac{Q}{2BW}
$$

Darcy's law:

$$
q = -\frac{k \Delta P}{\mu L}
$$
