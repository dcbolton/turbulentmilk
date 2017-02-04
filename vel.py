import sys
from spectral_cube import SpectralCube
import matplotlib.pyplot as plt
import random
import numpy as np
from random import randint
from numpy import array

#Create a function for which cloud name will be used to create s cube and name plots
def func(cloud):
	s = SpectralCube.read(cloud)
#Create the moment to the 1st order on the 0th (velocity) axis
	vbar = s.moment(1,0)

#Convert NaNs into zeros
	from numpy import *
	conv = isnan(vbar)
	vbar[conv] = 0

#Get the maximum index values for the randomizer
	dim = s.shape

#Initialize delta v and delta r arrays
	v1=0; v2=0;
	deltav = np.zeros((int(sys.argv[1])))
	deltar = np.zeros((int(sys.argv[1])))

#Pull the first random velocity: if velocity pulled is zero, value will be redrawn
	for x in xrange(0,int(sys.argv[1])):
		while v1 == 0:
			loc1x = randint(0,dim[1]-1)
			loc1y = randint(0,dim[2]-1)
			v1 = vbar.value[loc1x,loc1y]
#Pull the second random velocity: if velocity pulled is zero, value will be redrawn
		while v2 == 0:
			loc2x = randint(0,dim[1]-1)
			loc2y = randint(0,dim[2]-1)
			v2 = vbar.value[loc2x,loc2y]

#Create delta v and delta x arrays
		deltav[x] = abs(v1-v2)
		deltar[x] = abs(((loc2x-loc1x)**2+(loc2y-loc1y)**2)**.5)

#Debugging commented out
#		print v1, v2, deltav[x]
#		print loc2x, loc1x, loc2y, loc1y, deltar[x]

#Reset values of v1, v2 for next random draw
		v1=0; v2=0;
	
#Create scatterplot of deltav on y and deltar on x
	plt.plot(deltar,deltav,"o")
	figname = cloud[:-5] + ' vel'
	plt.savefig(figname)
	plt.clf()

#Read fits file names from folder and use them as arguments for our plotting function
import glob
array = glob.glob("/mnt/work/dcbolton/top10/*.fits")
i=0
for name in array: 
	print array[i]
        if i>len(array):
                exit()
        func(array[i])
	i=i+1
