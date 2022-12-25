import matplotlib.pyplot as plt

x1 = 40
x2 = 120
y1 = 0
y2 = 100

plt.axis([x1, x2, y1, y2])
plt.axis('on')

plt.title('Color Intensity')

plt.scatter(60, 50, s = 1000, color = 'b', alpha = 1)
plt.scatter(80, 50, s = 1000, color = 'b', alpha = 0.5)
plt.scatter(100, 50, s = 1000, color = 'b', alpha = 0.1)

plt.text(58, 35, '(1)')
plt.text(77, 35, '(0.5)')
plt.text(97, 35, '(0.1)')

plt.text(77.5, 24, 'alpha')

plt.show()