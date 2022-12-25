import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, radians

plt.axis ([0,140,0,120])
plt.grid()
plt.title('shape')

alpha1= radians(0)
alpha2= radians(360)
dalpha= radians(18)
half = radians(9)

r=40
xc= 80
yc= 60
plt.scatter(xc,yc,s=10,color='k')

for alpha in np.arange( alpha1,alpha2,dalpha):
    x =xc+r*cos(alpha)
    y= yc + r* sin(alpha)
    plt.plot([x,xc],[y,yc],color='k')
    Nalpha=alpha + half
    xx=xc+ (r+10)*cos(Nalpha)
    yy=yc+ (r+10)*sin(Nalpha)
    plt.plot([x,xx],[y,yy],color='k')
    # xx=xc+ (r-10)*cos(Nalpha)
    # yy=yc+ (r-10)*sin(Nalpha)
    # plt.plot([x,xx],[y,yy],color='k')
    
    Nalpha=alpha - half
    xx=xc+ (r+10)*cos(Nalpha)
    yy=yc+ (r+10)*sin(Nalpha)
    plt.plot([x,xx],[y,yy],color='k')
    # xx=xc+ (r-10)*cos(Nalpha)
    # yy=yc+ (r-10)*sin(Nalpha)
    # plt.plot([x,xx],[y,yy],color='k')
    
plt.show()