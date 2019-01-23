import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, fftfreq
from numpy import sin
from math import pi

t = np.linspace(0, 2*pi * 10, 1000)
s1 = sin(t)
s2 = sin(2*t)
s3 = sin(5*t)
s4 = sin(10*t)
s_tot = s1+s2+s3

# Signal (sinus)
plt.plot(s_tot)
plt.show()

# Plot fft (De cette maniere le graph indique le nombre de fois que le sin a de cycles dans la fenetre (diviser ces valeur en fonction de l'axe des x (ou ce sera le temps))
sp = fft(s_tot)
shape = s_tot.shape[-1]
freq = fftfreq(shape)
plt.plot(freq, sp.real)
plt.show()