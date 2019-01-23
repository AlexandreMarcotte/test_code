import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# create a group of time series
num_samples = 90
group_size = 10
x = np.linspace(0, 10, num_samples)
group = np.sin(x) + np.linspace(0, 2, num_samples) \
        + np.random.rand(group_size, num_samples) \
        + np.random.randn(group_size, 1)
df = pd.DataFrame(group.T, index=range(0,num_samples))

# plot time series with seaborn
ax = sns.tsplot(data=df.T.values) #, err_style="unit_traces")

# Add std deviation bars to the previous plot
mean = df.mean(axis=1)
std  = df.std(axis=1)
ax.errorbar(df.index, mean, yerr=std, fmt='-') #fmt=None to plot bars only

plt.show()


#%%
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 1000)
y = np.sin(x)
y_max = np.percentile(np.abs(y), 100)
y[y < -y_max] = -y_max
y[y > y_max] = y_max
plt.plot(y)
plt.show()

#%%
import numpy as np
from scipy.ndimage.interpolation import shift

xs = np.array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.])
x = np.random.rand(100)
print(np.argmin(x))
# shift(xs, 3, cval=0)