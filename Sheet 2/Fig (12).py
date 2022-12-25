import matplotlib.pyplot as plt

plt.axis([0, 140, 80, 0])
plt.axis('on')
plt.title('Line styles')

plt.plot([40,100],[20,20],linewidth=2,color='r')
plt.plot([40,100],[30,30],linewidth=4,color='g',linestyle=':')
plt.plot([40,100],[40,40],linewidth=6,color='b',linestyle='-')
plt.plot([40,100],[50,50],linewidth=2,color='k',linestyle='-.')

plt.show()