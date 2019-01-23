from math import log
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 1000)[1:-1]
y = np.array([-log(1-i) for i in x])


plt.plot(x, y)
plt.show()
