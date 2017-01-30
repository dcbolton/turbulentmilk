import sys
from spectral_cube import SpectralCube
from numpy import unravel_index
import matplotlib.pyplot as plt

def func(argv):
	from numpy import unravel_index
	s = SpectralCube.read(argv)
        high = unravel_index(s.argmax(), s.shape)
	plt.plot(s[:,high[1],high[2]].value)
	figname = argv[:-5] + ' ' + str(high[1]) + ' ' + str(high[2])
	
	plt.savefig(figname)
	plt.clf()
	

import glob
array = glob.glob("/mnt/work/dcbolton/top10/*.fits")
i=0
for name in array: 
	if i>len(array):
		exit()
	func(array[i])
	i=i+1
	#func(sys.argv[1])


