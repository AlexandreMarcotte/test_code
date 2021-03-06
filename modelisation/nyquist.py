from scipy import signal
import matplotlib.pyplot as plt

# Transfer function: H(s) = 5 / (s-1)^3
s1 = signal.ZerosPolesGain([], [1, 1, 1], [5])

w, H = signal.freqresp(s1)

plt.figure()
plt.plot(H.real, H.imag, "b")
plt.plot(H.real, -H.imag, "r")
plt.show()
