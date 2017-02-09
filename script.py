from spectral_cube import SpectralCube
s = SpectralCube.read('cohrscld_11918.fits')
import matplotlib.pyplot as plt
from turbustat.statistics import PCA
from spectral_cube import SpectralCube
from astropy.io import fits
hdu = fits.open('cohrscld_11918.fits')
hdu[0].header['BMAJ']=15/3600.
hdu[0].header['BMIN']=15/3600.
hdu[0].header['BPA']=0.
cube = SpectralCube.read(hdu)
import astropy.units as u
pca = PCA(cube, distance=250 * u.pc)
pca.run(verbose=True, min_eigval=0.005)

