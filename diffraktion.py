import numpy as np
from matplotlib import pyplot as plt
import scipy.fftpack as sfft

# Fourier transform
lbd = 532.8E-9
numpoints = 1000000
x = np.linspace(-3.14,3.14,100000)
shift = int(100000/4)
singleslit = np.zeros_like(x)
opening = 50
singleslit[shift:shift+opening] = 1
sep = opening*10
dblslit = np.copy(singleslit)
dblslit[sep+shift:sep+shift+opening] = 1

tripslit = np.copy(dblslit)
tripslit[2*sep+shift:2*sep+shift+opening] = 1

plt.figure()
#plt.plot(singleslit)
#plt.plot(dblslit)
plt.plot(tripslit)
plt.show()

ftsnigel = np.fft.fft(singleslit)
ftsnigelfreq = np.fft.fftfreq(len(singleslit))

ftdub = np.fft.fft(dblslit)
ftdubfreq = np.fft.fftfreq(len(singleslit))


fttrp = np.fft.fft(tripslit)
fttrpfreq = np.fft.fftfreq(len(singleslit))


plt.figure()
#plt.plot(ftsnigelfreq,np.abs(ftsnigel)**2)
#plt.plot(ftsnigelfreq,np.abs(ftdub)**2)
plt.plot(ftsnigelfreq,np.abs(fttrp)**2)

#plt.xlim(-.01,.01)
plt.show()


#############################################################
## 2d grejor ###########################
def create_circular_mask(h, w, center=None, radius=None):

    if center is None: # use the middle of the image
        center = [int(w/2), int(h/2)]
    if radius is None: # use the smallest distance between the center and image walls
        radius = min(center[0], center[1], w-center[0], h-center[1])

    Y, X = np.ogrid[:h, :w]
    dist_from_center = np.sqrt((X - center[0])**2 + (Y-center[1])**2)

    mask = dist_from_center <= radius
    return mask

numside = 1000
circ = np.zeros((numside,numside))
mask = create_circular_mask(numside, numside, radius=50)
circ[~mask] = 10
circfft = np.fft.fft(circ)
Z_fft = sfft.fft2(circ)
Z_shift = sfft.fftshift(Z_fft)
plt.figure()
plt.imshow(circ)
plt.show()
#np.fft.fftfreq
plt.figure()
plt.imshow(np.abs(Z_shift), vmin=0, vmax=75000, cmap='jet')
plt.xlim([300,700])
plt.ylim([300,700])
plt.colorbar()
plt.show()


# Lets create square
numside = 1000
square = np.zeros((numside,numside))
square[490:510,490:510] = 10
squarefft = np.fft.fft(square)
Z_fft = sfft.fft2(square)
Z_shift = sfft.fftshift(Z_fft)
plt.figure()
plt.imshow(square)
plt.show()
plt.figure()
plt.imshow(np.abs(Z_shift), vmin=0, vmax=750)
plt.colorbar()
plt.show()


# Lets create Slit
numside = 1000
square = np.zeros((numside,numside))
square[450:550,490:510] = 10
squarefft = np.fft.fft(square)
Z_fft = sfft.fft2(square)
Z_shift = sfft.fftshift(Z_fft)
plt.figure()
plt.imshow(square)
plt.show()
plt.figure()
plt.imshow(np.abs(Z_shift), vmin=0, vmax=2000)
plt.colorbar()
plt.show()
