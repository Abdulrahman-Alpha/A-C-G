import numpy as np
import matplotlib.pyplot as plt
plt.axis([-50,50,-50,50])
plt.axis('on')
plt.grid(True)

plt.plot([-20,20],[-20,-20],linewidth=2,color='r')
plt.plot([20,20],[-20,20],linewidth=2,color='r')
plt.plot([20,-20],[20,20],linewidth=2,color='r')
plt.plot([-20,-20],[-20,20],linewidth=2,color='r')

x=[-30,30,30,-30,-30]
y=[-30,-30,30,30,-30]

plt.plot(x,y,linewidth=2,color='g')

plt.show()