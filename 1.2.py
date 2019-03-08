import numpy as np
import matplotlib.pyplot as plt

j = np.complex(0, 1)
pi = np.pi

#continuous
x = np.arange(-0, 2.01, 0.1)
y1 = np.cos(2*pi*x)
y2 = np.sin(pi*x)
y = y1+y2
plt.plot(x,y)

#discrete
x = np.arange(-0, 2.01, 1)
y1 = np.cos(2*pi*x)
y2 = j*np.sin(pi*x)
y = y1+y2
plt.stem(x,y)

#show
plt.show()

# T = 2 but i have set 2.01 for range to see the exact 2 too