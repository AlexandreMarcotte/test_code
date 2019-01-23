from collections import deque
import numpy as np

x = deque(np.ones(10), maxlen=10)
y = deque(np.zeros(10), maxlen=10)
k = deque(np.ones(10) * 66, maxlen=10)
z = [x, y, k]
with open('CCCSVVV_eeg_data.csv', 'a') as f:
    for _ in range(100):
        np.savetxt(f, np.transpose(z), delimiter=',')
