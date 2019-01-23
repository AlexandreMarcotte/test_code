from collections import deque
import numpy as np
x = [deque(np.zeros(10), maxlen=10) for _ in range(3)]
y = deque(np.ones(10), maxlen=10)
print('x', x, '---', np.array(x).shape)
print('y', y, '---', np.array(y)[None, :].shape)


y = np.array(y)[None, :]
# z =
print('xy', np.concatenate((x, y, y)))


#%%
x = np.zeros(10)
print(x)
print(x[0:5])