import matplotlib.pyplot as plt  
import numpy as np 
from math import radians

plt.axis([-10,150,100,-10]) 
plt.axis('on')
plt.grid(True)
#axes
plt.arrow(0,0,40,0,head_length=4,head_width=2,color='b')
plt.arrow(0,0,0,40,head_length=4,head_width=2,color='b') 
plt.text(30,-3,'Xg',color='b')
plt.text(-8,34,'Yg',color='b')
 #center of rotation
xc=75
yc=50
plt.plot([xc-40,xc+60],[yc,yc],linewidth=1,color='grey') #—-X
plt.plot([xc,xc],[yc-40,yc+45],linewidth=1,color='grey') #—-Y
plt.text(127,48,'X')  
plt.text(70,90,'Y')
plt.scatter(xc,yc,s=20,color='k') #—plot center of rotation 
plt.text(70,49,'c')
#define function rot_ 
def rot_(xp,yp,rz):
    c11=np.cos(rz) 
    c12=-np.sin(rz)
    c21=np.sin(rz) 
    c22=np.cos(rz)
    xpp=xp*c11+yp*c12 #relative to xc,yc
    ypp=xp*c21+yp*c22
    xg=xc+xpp #relative to xg,yg
    yg=yc+ypp 
    return [xg,yg] #plot unrotated rectangle 
    
#rectangle corner coordinates in X,Y system 
xp1=-20
xp2=+20
xp3=+20
xp4=-20
yp1=-5
yp2=-5
yp3=+5
yp4=+5
#label
plt.text(50,45,'1') 
plt.text(97,45,'2') 
plt.text(97,57,'3')
plt.text(50,57,'4')
#plot unrotated rectangle
plt.scatter(xp1+xc,yp1+yc,s=10,color='k')
plt.scatter(xp2+xc,yp2+yc,s=10,color='k')
plt.scatter(xp3+xc,yp3+yc,s=10,color='k')
plt.scatter(xp4+xc,yp4+yc,s=10,color='k')
#corner coordinates in Xg,Yg system
xg1=xc+xp1 
yg1=yc+yp1
xg2=xc+xp2
yg2=yc+yp2
xg3=xc+xp3
yg3=yc+yp3
xg4=xc+xp4
yg4=yc+yp4
xg=[xg1,xg2,xg3,xg4,xg1]
yg=[yg1,yg2,yg3,yg4,yg1]
plt.plot((xg),(yg),color='k')
#rotate rectangle corner coordinates 
rz=45
rz=radians(rz)
#point 1
xp=xp1
yp=yp1
[xg,yg]=rot_(xp,yp,rz) 
[xg1,yg1]=[xg,yg]
#point 2
xp=xp2
yp=yp2
[xg,yg]=rot_(xp,yp,rz) 
[xg2,yg2]=[xg,yg]
#point 3
xp=xp3
yp=yp3
[xg,yg]=rot_(xp,yp,rz) 
[xg3,yg3]=[xg,yg]
#point 4
xp=xp4
yp=yp4
[xg,yg]=rot_(xp,yp,rz) 
[xg4,yg4]=[xg,yg]

#plot rotated rectangle 
xg=[xg1,xg2,xg3,xg4,xg1]
yg=[yg1,yg2,yg3,yg4,yg1]
plt.plot(xg,yg,color='r')

plt.show()