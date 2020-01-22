# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 16:35:03 2020

@author: admin
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.gca(projection = '3d')

t = np.arange(0.01, 12*np.pi, 0.01)

x = 2**(-0.1*t)*np.cos(t)
y = 2**(-0.1*t)*np.sin(t)
z = -t

ax.plot(x, y, z)
ax.legend()

plt.show()