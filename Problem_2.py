# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 16:43:22 2020

@author: admin
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.gca(projection = '3d')

t = np.arange(10**(-7), 1.1*10**(-7), 10**(-11))


def move_func(s,t):
    x, v_x, y, v_y, z, v_z = s
    dxdt = v_x
    dv_xdt = q/ m* (Ex + v_y * Bz - By* v_z) - (G*M / ((x-xc)**2 + (y-yc)**2 + (z-zc)**2)**(1.5)) * (x-xc)
    dydt = v_y
    dv_ydt = q/ m *(Ey + v_z * Bx - Bz * v_x) - (G*M / ((x-xc)**2 + (y-yc)**2 + (z-zc)**2)**(1.5)) * (y-yc)
    dzdt = v_z
    dv_zdt = q/ m *(Ez + v_x * By - Bx * v_y) - (G*M / ((x-xc)**2 + (y-yc)**2 + (z-zc)**2)**(1.5)) * (z-zc)

    return dxdt, dv_xdt, dydt, dv_ydt, dzdt, dv_zdt

x0 = 0
v_x0 = 10**7
xc = 0.0025

y0 = 0
v_y0 = 10**6
yc = 0.008

z0 = 0
v_z0 = 0
zc = 0.0100

s0 = x0, v_x0, y0, v_y0, z0, v_z0

M = 5*10**22
m = 1.6 *10**(-31)
q = 1.6 * 10**(-19)
G = 6.67*10**(-11)

Ex = 0
Ey = 10**(-3)
Ez = 0

Bx =0
By = 10**(-3)
Bz = 0

sol=odeint(move_func, s0, t)

fix = plt.figure()
ax = fig.gca(projection = '3d')

ax.plot(sol[:,0], sol[:,2], sol[:,4])
#ax.plot(xc, yc, zc)

ax.quiver(x0, y0, z0, Bx, By, Bz, length=(sol[len(t)-1,4] - sol[0,4]), normalize = True, color = 'r')
ax.quiver(x0, y0, z0, Ex, Ey, Ez, length=(sol[len(t)-1,4] - sol[0,4]), normalize = True, color = 'g')
ax.quiver(x0, y0, z0, v_x0, v_y0, v_z0, length=(sol[len(t)-100,4] - sol[0,4]), normalize = True, color = 'k')

ax.legend()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('z')
plt.show()