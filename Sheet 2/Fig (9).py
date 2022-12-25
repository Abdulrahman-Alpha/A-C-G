import matplotlib.pyplot as plt
import numpy as np
from math import radians,sin,cos

plt.title('Distortions corrected by applying a scale factor\nto each point as it is plotted')
plt.axis([0,100,100,0])

plt.grid(True)
r = 40

alpha1 = radians(0)
alpha2 = radians(360)
dalpha = radians(2)

xc=50
yc=50

dx = 6.5
dy = 5
sfx = dy/dx

plt.scatter(xc,yc,s=10,color='k')

for alpha in np.arange(alpha1,alpha2,dalpha):
    x=xc+sfx*r*cos(alpha)
    y=yc+r*sin(alpha)
    plt.scatter(x,y,s=5,color='k')

plt.show()