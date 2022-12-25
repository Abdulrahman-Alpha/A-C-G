import matplotlib.pyplot as plt

plt.axis([0, 140, 80, 0])
plt.axis('on')
plt.title('Line styles')

plt.arrow(40,20,60,0,linewidth=1,color='r',head_length=5, head_width=3)
plt.arrow(40,30,60,0,linewidth=1,color='g',linestyle=':', head_length=10,head_width=5)
plt.arrow(40,40,60,0,linewidth=1,color='b',linestyle='-', head_length=8,head_width=4)
plt.arrow(40,50,60,0,linewidth=4,color='k',linestyle='-', head_length=8,head_width=3)

plt.show()