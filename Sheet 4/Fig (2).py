import matplotlib.pyplot as plt  
import numpy as np 

plt.axis([-20,130,80,-20])
plt.axis('off') 
plt.grid(False) 

x1=0
x2=100
y1=60
y2=20
q=np.sqrt((x2-x1)**2+(y2-y1)**2) 
ux=(x2-x1)/q
uy=(y2-y1)/q
for l in np.arange(0,q,.5):
    px=x1+l*ux 
    py=y1+l*uy
    plt.scatter(px,py,s=1,color='gray')


plt.plot([x2,x2],[y2,y1],color = 'k')
plt.plot([x2,x1+23],[y1,y1],color = 'k')

plt.arrow(x1,y1,16.25,-6.5,head_length=3,head_width=2,color='b')
plt.plot([x1,x1+20],[y1,y1],color = 'b')
plt.plot([x1+20,x1+20],[y1,y1-8],color = 'b')

plt.scatter(x1,y1,s=20,color = 'k')
plt.scatter(x2,y2,s=20,color = 'k')


plt.text(8,64,'ux')
plt.text(22,57,'uy')
plt.text(-5,60,'1')
plt.text(102,18,'2')
plt.text(8,55,'u',rotation=20)


plt.plot([0,0],[60,73],color = 'k')
plt.plot([100,100],[62,73],color = 'k')
plt.text(50,70,'A')
plt.arrow(40,68,-37,0,head_length=3,head_width=2,color='k')
plt.arrow(60,68,37,0,head_length=3,head_width=2,color='k')

plt.plot([102,115],[20,20],color = 'k')
plt.plot([102,115],[60,60],color = 'k')
plt.text(108,40,'B')
plt.arrow(110,35,0,-12,head_length=3,head_width=2,color='k')
plt.arrow(110,43,0,14,head_length=3,head_width=2,color='k')

plt.plot([-1,-7],[58,45],color = 'gray')
plt.plot([99,92],[18,5],color = 'gray')
plt.text(42,30,'Q',rotation=20)
plt.arrow(40,30,-42,17,head_length=3,head_width=2,color='k')
plt.arrow(48,26,42,-17,head_length=3,head_width=2,color='k')


plt.show()    