import matplotlib.pyplot as plt

x1 = 0
x2 = 150
y1 = 0
y2 = 100

plt.axis([x1, x2, y1, y2])
plt.axis('on')

plt.title('Overplotting with lines, arrows, and dots')

plt.scatter(40,60,s=1000,color='navy')
plt.arrow(20,60,60,0,head_width = 2,linewidth=5, color = 'r')
plt.scatter(60,60,s=1000,color='b')
plt.text(40,50,'1')
plt.text(10,60,'2')
plt.text(60,50,'3')



plt.arrow(90,40,40,0,head_width = 2,linewidth=5, color = 'r')
plt.arrow(100,50,0,-20,head_width = 2,linewidth=5, color = 'b')
plt.text(80,40,'1')



plt.plot([20,60],[20,20],linewidth=5, color = 'r')
plt.arrow(30,30,0,-20,head_width = 2,linewidth=5, color = 'g')
plt.arrow(50,30,0,-20,head_width = 2,linewidth=5, color = 'b')
plt.text(15,20,'1')
plt.text(20,10,'2')
plt.text(55,10,'3')




plt.show()