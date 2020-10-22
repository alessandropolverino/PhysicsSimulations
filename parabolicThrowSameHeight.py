import matplotlib.pyplot as plt 
import numpy as np
import math
import random


for _ in range(7):
    v0 = random.randint(1, 100)
    ang = math.radians(random.randint(1, 89))

    tpar = (v0/9.81)*2

    t = np.linspace(0, tpar, 100)
    xcoords = []
    ycoords = []
    for k in t:
        x = (v0*k)*math.cos(ang)
        y = (v0*k)*math.sin(ang) - (9.81/2)*(k)**2
        if y < 0:
            break
        xcoords.append(x)
        ycoords.append(y)
        plt.plot(xcoords, ycoords)

plt.show()