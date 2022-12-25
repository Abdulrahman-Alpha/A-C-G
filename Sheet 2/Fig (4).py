import matplotlib.pyplot as plt

x1 = 0
x2 = 150
y1 = 0
y2 = 100

plt.axis([x1, x2, y1, y2])
plt.axis('on')

plt.title('Overplotting with lines and dots')

plt.plot([20,60],[20,20],linewidth=5, color = 'r')
plt.plot([30,30],[10,30],linewidth=5, color = 'g')
plt.text(45,10,'(A)')
plt.text(15,20,'1')
plt.text(30,5,'2')

plt.scatter(40,60,s=1000,color='navy')
plt.plot([20,60],[60,60],linewidth=5, color = 'r')
plt.scatter(60,60,s=1000,color='b')
plt.text(45,75,'(B)')
plt.text(40,50,'1')
plt.text(10,60,'2')
plt.text(60,50,'3')



plt.scatter(100,40,s=1000,color='r')
plt.scatter(110,40,s=1000,color='b')
plt.scatter(120,40,s=1000,color='y')
plt.text(110,55,'(C)')
plt.text(100,30,'1')
plt.text(110,30,'2')
plt.text(120,30,'3')



plt.show()