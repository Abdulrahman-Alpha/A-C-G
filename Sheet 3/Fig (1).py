import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, radians

plt.axis([0,150,0,120])
plt.title('acrs')

xc = 80
yc = 60

plt.scatter(xc,yc,s=5,color='k')

alpha1 = radians(0)
alpha2 = radians(90)
dalpha = radians(1)

for r in [30,40,50]:
    for alpha in np.arange(alpha1,alpha2,dalpha):
        x=xc+r*cos(alpha)
        y=yc+r*sin(alpha)
        plt.scatter(x,y,s=2,color='k')


alpha1 = radians(180)
alpha2 = radians(270)
dalpha = radians(1)

for r in [30,40,50]:
    for alpha in np.arange(alpha1,alpha2,dalpha):
        x=xc+r*cos(alpha)
        y=yc+r*sin(alpha)
        plt.scatter(x,y,s=2,color='k')

plt.show()
