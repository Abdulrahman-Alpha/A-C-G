import matplotlib.pyplot as plt
plt.axes().set_aspect('equal')

x1 = -10.5
x2 = 10.5
y1 = 10.5
y2 = -10.5

plt.axis([x1, x2, y1, y2])
plt.axis('on')
plt.grid(True)

plt.title('Distortion Corrected by equalizing axes')


plt.plot([-5,5],[-5,-5], linewidth = 2, linestyle = '-', color = 'k')
plt.plot([5,5],[-5,5], linewidth = 2, linestyle = '-', color = 'k')
plt.plot([5,-5],[5,5], linewidth = 2, linestyle = '-', color = 'k')
plt.plot([-5,-5],[5,-5], linewidth = 2, linestyle = '-', color = 'k')



plt.show()