import numpy as np
from random import random
import matplotlib.pyplot as plt

x = np.array([random() for _ in range(100)])

slices = (slice(0, 4), slice(4, 8), slice(8, 12), slice(12, 40), slice(40, 100))
y = [np.average(x[s]) for s in slices]
plt.plot(y)
plt.show()