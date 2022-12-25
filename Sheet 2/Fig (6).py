import matplotlib.pyplot as plt

x1 = -10
x2 = 10
y1 = 10
y2 = -10

plt.axis([x1, x2, y1, y2])
plt.axis('on')
plt.grid(True)

plt.title('Distortion of a mathematically correct square')

plt.plot([-5,5],[-5,-5], linewidth = 2, linestyle = '-', color = 'k')
plt.plot([5,5],[-5,5], linewidth = 2, linestyle = '-', color = 'k')
plt.plot([5,-5],[5,5], linewidth = 2, linestyle = '-', color = 'k')
plt.plot([-5,-5],[5,-5], linewidth = 2, linestyle = '-', color = 'k')

plt.show()