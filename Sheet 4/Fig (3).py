import matplotlib.pyplot as plt 
import numpy as np 
from math import radians, sin, cos  

plt.axis([-10,140,90,-10])
plt.axis('on') 
plt.grid(True) 
#axes
plt.arrow(0,0,20,0,head_length=4,head_width=3,color='k')
plt.arrow(0,0,0,20,head_length=4,head_width=3,color='k')
plt.text(16,-3,'x') 
plt.text(-5,17,'y') 
xc=20
yc=20
r=40
#plot arc 
p1=radians(20)
p2=radians(70)
dp=(p2-p1)/100
for p in np.arange(p1,p2,dp):
    x=xc+r*cos(p) 
    y=yc+r*sin(p)
    plt.scatter(x,y,s=1,color='g')
#labels
plt.text(61,34,'(x1,y1)')
plt.text(16,60,'(x2,y2)')
plt.scatter(xc,yc,s=10,color='k')
plt.text(xc+4,yc-4,'(xc,yc)',color='k')

plt.show()