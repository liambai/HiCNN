from matplotlib import pyplot as plt
import numpy as np

data = np.load('out.npy')
plt.imshow(data, cmap='gray')
plt.show()
