import matplotlib.pyplot as plt
import numpy as np
from math import sin,cos,radians
plt.axis([-10,140,90,-10])
plt.axis('on')
plt.grid(True)

#———————————————————————axes
plt.arrow(0,0,15,0,head_length=2,head_width=1,color='b')
plt.arrow(0,0,0,15,head_length=2,head_width=1,color='b')
#-------------------------
plt.text(-5,-2,'(x0,y0)')
#-------------------------------------------------------------------
plt.plot([0,10],[10,10],linewidth=1, color='k',linestyle='dashdot')
plt.plot([10,10],[0,10],linewidth=1, color='k',linestyle='dashdot')
#-------------------------------------------------------------------
plt.scatter(0,0,s=15,color='k')
plt.scatter(10,10,s=15,color='k')
#-------------------------------------------------------------------
xc=40
yc=10
#-------------------------------------------------------------------- 
plt.plot([xc-10,xc+90],[yc,yc],linewidth=1,color='k') #—-X
plt.plot([xc,xc],[yc-5,yc+75],linewidth=1,color='k') #—-Y
#-------------------------------------------------------------------
plt.text(20,-2,'Xg',color='b')
plt.text(-7,20,'Yg',color='b')
plt.scatter(xc,yc,s=20,color='k')
plt.text(xc-15,yc-2,'(xc,yc)')
#—————————————————–define rotation matrix rz
def rotz(xp,yp,rz): #——–xp,yp=un-rotated coordinates relative to xc,yc
       c11=np.cos(rz)
       c12=-np.sin(rz)
       c21=np.sin(rz)
       c22=np.cos(rz)
       xpp=xp*c11+yp*c12 #—-xpp,ypp=rotated coordinates relative to xc,yc
       ypp=xp*c21+yp*c22
       xg=xc+xpp #—-xg,yg=rotated coordinates relative to xg,yg
       yg=yc+ypp
       return [xg,yg]

#————————————-coordinates of first point P1 relative to xc,yc
xp=60
yp=0
#——————————————————————————————————
rz=20
rz=rz*np.pi/180
[xg,yg]=rotz(xp,yp,rz)
plt.scatter(xg,yg,s=30,color='k')
plt.text(xg+1,yg+6,r"$\mathbf{P(xp,yp)}$",color='k')
xpp4=xg
ypp4=yg
#——————————————————————————————————
rz=50
rz=rz*np.pi/180
[xg,yg]=rotz(xp,yp,rz)
plt.scatter(xg,yg,s=30,color='r')
plt.text(xg+1,yg+6,r"$\mathbf{P^{\prime}(xp^{\prime},yp^{\prime})}$",color='r')
xpp3=xg #——save for later in line 76
ypp3=yg
#————————————————————————————————————————————————plot vectors
plt.arrow(xc,yc,xpp4-4-xc,ypp4-2-yc,head_length=4,head_width=2,color='k')
plt.text(xpp4-10,ypp4-5,r'$\mathbf{P}$',color='k')
#-------------------------------------------------------------------------
plt.plot([xc,104.0],[yc,44.8],linewidth=0.5, color='r',linestyle='solid')
#-----------------------------------------------------------------dash lines
plt.plot([79,xpp3],[yc,ypp3],linewidth=1, color='r',linestyle='dashdot')
plt.text(77,yc-2,r'$\mathbf{xp^{\prime}}$',color='r')

plt.plot([xc,xpp3],[ypp3,ypp3],linewidth=1,color='r',linestyle='dashdot')
plt.text(xc-10,ypp3,r'$\mathbf{yp^{\prime}}$',color='r')
#-------------------------------------------------------line of yp in rotate
plt.plot([xpp4,xpp3],[ypp4+10,ypp3],linewidth=1, color='r',linestyle='solid')
plt.text(((xpp4+xpp3)/2)+2,((ypp4+10+ypp3)/2)+2,r'$\mathbf{yp}$',color='r')
#---------------------------------------------------line of yp before rotate
plt.plot([96,xpp4],[yc,ypp4],linewidth=1, color='k',linestyle='solid')
plt.text(((96+xpp4)/2)+2,((yc+ypp4)/2)+2,r'$\mathbf{yp}$',color='k')
#-------------------------------------------------------------------------
plt.arrow(xc,yc,xpp3-2-xc,ypp3-2-yc,head_length=2,head_width=2,color='r')
plt.text(61,45,r'$\mathbf{P^{\prime}}$',color='r')
#-------------------------------------------------------------------------
plt.arrow(xc,yc,50-xc,yc-yc,head_length=2,head_width=2,color='k')
plt.text(88,yc-2,r'$\mathbf{xp}$',color='k')
plt.text(xc+5,yc-2,'i')
#-------------------------------------------------------------------------
plt.text(110,yc-2,r'$\mathbf{X}$',color='k')
#-------------------------------------------------------------------------
plt.text(xc+2,yc+75,r'$\mathbf{Y}$',color='k')
#_________________________________________________________________________
plt.text(105.0,45,r'$\mathbf{X^{\prime}}$',color='r')
#-------------------------------------------------------------------------
plt.plot([xc,-0.3],[yc,59.5],linewidth=0.5, color='r',linestyle='solid')
plt.text(((xc+(-0.3))/2)+2,((yc+59.5)/2)+2,r'$\mathbf{Y^{\prime}}$',color='r')
#-------------------------------------------------------------------------
plt.arrow(xc,yc,35.0-xc,15.5-yc,head_length=2,head_width=2,color='r')
plt.text(35.0,20,r'$\mathbf{j^{\prime}}$',color='r')
#-------------------------------------------------------------------------
plt.arrow(xc,yc,xc+7-xc,yc+4-yc,head_length=2,head_width=2,color='r')
plt.text(xc+8,yc+10,r'$\mathbf{i^{\prime}}$',color='r')
#----------------------------------Rz arrow-------------------------------------
p1= radians(0)
p2= radians(12)
dp=(p2-p1)/180
r=80
for p in np.arange(p1,p2,dp):
    x=r*cos(p)+xc
    y=r*sin(p)+yc
    plt.scatter(x,y,s=.1,color='k')
#-------------------------------------------------------------------------
p1= radians(18)
p2= radians(29)
dp=(p2-p1)/180
r=80
for p in np.arange(p1,p2,dp):
    x=r*cos(p)+xc
    y=r*sin(p)+yc
    plt.scatter(x,y,s=.1,color='k')
#-----------------------------------------------------------------------
plt.arrow(112.5,44.75,-1.75,2.75,head_length=3,head_width=2,color='k')
plt.text(115,32,'Rz',size = 'large')
#-------------------------------------------------------------------------
plt.title("Rotation Model Created by Abdul-Rahman")
plt.show()
#------------------------------------THIS CODE CREATED BY ABDULRAHMAN ALPHA-----------------------------------------------#