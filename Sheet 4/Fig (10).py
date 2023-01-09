import matplotlib.pyplot as plt
import numpy as np
from math import sin,cos,radians

plt.axis([-20,140,90,-10])
plt.axis('on')
plt.grid(True, linestyle = ':')

plt.arrow(0,0,20,0,head_length=4,head_width=2,color = 'b')
plt.arrow(0,0,0,20,head_length=4,head_width=2,color='b')
plt.text(9,-3,'Xg',color='b')
plt.text(-8,13,'Yg',color='b')
plt.scatter(0,0,s=20,color='b')
plt.text(-15,-3,'(x0,y0)',color='b')
plt.scatter(12,12,s=20,color='b')
plt.text(12+1,12+6,'(xg,yg)',color='b')
plt.plot([12,12],[0,12],linewidth=1,linestyle='--',color='b')
plt.plot([0,12],[12,12],linewidth=1,linestyle='--',color='b')


xc=40
yc=10

plt.plot([xc-18,xc+90],[yc,yc],linewidth=1,color='k')
plt.plot([xc,xc],[yc-8,yc+75],linewidth=1,color='k')
plt.text(xc-16,yc-2,'(xc,yc)')
plt.arrow(xc,yc,10,0,head_length=3,head_width=1.5,color = 'k')
plt.arrow(xc,yc,0,10,head_length=3,head_width=1.5,color = 'k')


#P
xp = 50
yp = 20

def rotz(xp,yp,rz):
    c11=np.cos(rz)
    c12=-np.sin(rz)
    c21=np.sin(rz)
    c22=np.cos(rz)
    xpp=xp*c11+yp*c12
    ypp=xp*c21+yp*c22
    xg=xc+xpp
    yg=yc+ypp
    return[xg,yg]


#P
rz=0
rz=rz*np.pi/180
[xg,yg]=rotz(xp,yp,rz)
plt.scatter(xg,yg,s=30,color='k' )
plt.text(xg+1,yg+6,'P(xp,yp)',color='k')
plt.arrow(xc,yc,xp-3,yp-1,head_length=3,head_width=1.5,color = 'k')
plt.plot([xp+xc,xp+xc],[yc,yp+yc],linewidth=1,color='k')



# p'
rz=30
rz=rz*np.pi/180
[xg,yg]=rotz(xp,yp,rz)
plt.scatter(xg,yg,s=30,color='r')
plt.text(xg+1,yg+6,'P\'(xp\',yp\')',color='r')
plt.arrow(xc,yc,xg-xc-2,yg-yc-2.5,head_length=3,head_width=1.5,color = 'r')

plt.plot([xg,xg],[yc-2,yg],linewidth=1,linestyle='--',color='r')
plt.plot([xc-2,xg],[yg,yg],linewidth=1,linestyle='--',color='r')

#x-axis rotation
[xcg,ycg]=rotz(90,0,rz)
plt.plot([xc,xcg],[yc,ycg],linewidth=1,color='r')

#y-axis rotation
[xcg,ycg]=rotz(0,75,rz)
plt.plot([xc,xcg],[yc,ycg],linewidth=1,color='r')

#i rotation
[xcg,ycg]=rotz(10,0,rz)
plt.arrow(xc,yc,xcg-40,ycg-10,head_length=3,head_width=1.5,color = 'r')

#j rotation
[xcg,ycg]=rotz(0,10,rz)
plt.arrow(xc,yc,xcg-40,ycg-10,head_length=3,head_width=1.5,color = 'r')

#yp rotation
[xcg,ycg]=rotz(xp,0,rz)
plt.plot([xcg,xg],[ycg,yg],linewidth=1,color='r')


p1= radians(0)
p2= radians(10)
dp=(p2-p1)/180
r=80
for p in np.arange(p1,p2,dp):
    x=r*cos(p)+xc
    y=r*sin(p)+yc
    plt.scatter(x,y,s=.1,color='k')

p1= radians(18)
p2= radians(29)
dp=(p2-p1)/180
r=80
for p in np.arange(p1,p2,dp):
    x=r*cos(p)+xc
    y=r*sin(p)+yc
    plt.scatter(x,y,s=.1,color='k')

plt.arrow(112.5,44.75,-1.75,2.75,head_length=3,head_width=2,color='k')
plt.text(115,32,'Rz',size = 'large')


p1= radians(90)
p2= radians(100)
dp=(p2-p1)/180
r=70
for p in np.arange(p1,p2,dp):
    x=r*cos(p)+xc
    y=r*sin(p)+yc
    plt.scatter(x,y,s=.1,color='k')

p1= radians(110)
p2= radians(119)
dp=(p2-p1)/180
r=70
for p in np.arange(p1,p2,dp):
    x=r*cos(p)+xc
    y=r*sin(p)+yc
    plt.scatter(x,y,s=.1,color='k')

plt.arrow(9.75,73.4,-1.75,-1,head_length=3,head_width=2,color='k')
plt.text(19,79,'Rz',size = 'large')

plt.show()