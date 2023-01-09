import matplotlib.pyplot as plt
x1 = 0
x2 = 20
y1 = 0
y2 = 20

plt.axis([x1, x2, y1, y2])
plt.axis('on')

plt.grid(True, color = 'k')
plt.title('plotting area with (0,0) located in the center')

plt.xlabel('x axis')
plt.ylabel('y axis')

plt.show()