import matplotlib.pyplot as plt
import numpy as np

x1 = 0
x2 = 100
y1 = 0
y2 = 10

plt.axis([x1, x2, y1, y2])
plt.axis('on')


plt.title('Color Mixing')

red = np.arange(0,1,0.01)

for x in range(0,100):
    plt.plot([x,x], [y1,y2], linewidth = 5, color=(red[x],0,0))

plt.show()