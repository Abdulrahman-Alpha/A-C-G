import matplotlib.pyplot as plt
import numpy as np
from math import radians,sin,cos

plt.title('Distortion corrected by applying a scale factor to the x axis')
plt.axis([0,150,120,0])
plt.grid(True)

r=40

alpha1=radians(0)
alpha2=radians(360)
dalpha=radians(2)

xc=80
yc=60

plt.scatter(xc,yc,s=10,color='k')

for alpha in np.arange(alpha1,alpha2,dalpha):
    x=xc+r*cos(alpha)
    y=yc+r*sin(alpha)
    plt.scatter(x,y,s=5,color='k')

plt.show()