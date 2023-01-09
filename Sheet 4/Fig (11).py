import matplotlib.pyplot as plt
import numpy as np
from math import sin,cos,radians


plt.axis([-10,150,100,-10])
plt.axis('on')
plt.grid(True,linestyle = ':')

plt.arrow(0,0,40,0,head_length=4,head_width=2,color='b')
plt.arrow(0,0,0,40,head_length=4,head_width=2,color='b')
plt.text(30,-3,'Xg',color='b')
plt.text(-8,34,'Yg',color='b')

xc=80
yc=30

plt.plot([xc-50,xc+65],[yc,yc],linewidth=1,color='grey')
plt.plot([xc,xc],[yc-35,yc+60],linewidth=1,color='grey') 
plt.text(xc+50,yc-2,'X')
plt.text(xc-5,yc+55,'Y')

plt.scatter(xc,yc,s=20,color='k') 
plt.text(xc-17,yc-3,'(xc,yc)')

def rotz(xp,yp,rz):
    c11=np.cos(rz)
    c12=-np.sin(rz)
    c21=np.sin(rz)
    c22=np.cos(rz)
    xpp=xp*c11+yp*c12
    ypp=xp*c21+yp*c22
    xg=xc+xpp
    yg=yc+ypp
    return [xg,yg]

r = 10
p1=0
p2=2*np.pi
dp=(p2-p1)/100

alpha1=0
alpha2=0.80*np.pi
dalpha=(alpha2-alpha1)/2

for alpha in np.arange(alpha1,alpha2,dalpha):
    xcc=25*np.cos(alpha)
    ycc=25*np.sin(alpha)
    for p in np.arange(p1,p2,dp):
        xp=xcc+r*np.cos(p)
        yp=ycc+r*np.sin(p)
        [xg,yg]=rotz(xp,yp,0)
        if p < np.pi:
            plt.scatter(xg,yg,s=1,color='r')
        else:
            plt.scatter(xg,yg,s=1,color='g')
        xp1=xcc+r
        yp1=ycc+0
        [xg1,yg1]=rotz(xp1,yp1,0)
        xp2=xcc-r
        yp2=ycc+0
        [xg2,yg2]=rotz(xp2,yp2,0)
        
        

plt.text(xc+34,yc-10,'starting circle')
plt.arrow(xc+34,yc-10,-2,2,head_length=1,head_width=1)
plt.text(xc+20,yc+17,'Rotated circle')
plt.arrow(xc+20,yc+17,-2,2,head_length=1,head_width=1)

plt.plot([xc-13,xc+42],[yc+24,yc+24],linewidth=1,color='grey')
plt.plot([xc,xc+20],[yc,yc+63],linewidth=1,color='grey')
plt.scatter(xc+7.5,yc+24,s=10,color='grey')
plt.plot([xc+7.5,xc+33],[yc+24,yc+40],linewidth=1,color='grey')
plt.scatter(xc+16.25,yc+29.5,s=10,color='b')

p1=0
p2= radians(30)
dp=(p2-p1)/90
r=25
for p in np.arange(p1,p2,dp):
    x=r*cos(p)+xc+7.5
    y=r*sin(p)+yc+24
    plt.scatter(x,y,s=.1,color='gray')
plt.arrow(110.75,63.5,-0.5,1,head_length=3,head_width=2,color='gray')
plt.text(114,62,'P',size = 'large')

p1=0
p2= radians(30)
dp=(p2-p1)/180
r=60
for p in np.arange(p1,p2,dp):
    x=r*cos(p)+xc
    y=r*sin(p)+yc
    plt.scatter(x,y,s=.1,color='gray')


p1= radians(43)
p2= radians(72)
dp=(p2-p1)/180
r=60
for p in np.arange(p1,p2,dp):
    x=r*cos(p)+xc
    y=r*sin(p)+yc
    plt.scatter(x,y,s=.1,color='gray')

plt.arrow(103.5,85.25,-2.25,1,head_length=3,head_width=2,color='gray')
plt.text(126.5,66.5,r'$\alpha$',size = 'large')

plt.text(-1,75,'Center of rotated circle\nis at xcc,ycc relative to xc,yc')

plt.show()