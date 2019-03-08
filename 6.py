import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def r(n):
    a = []
    for i in range(-30, 30):
        if i<n:
            a.append(0)
            # print(i, ":", 0)
        else:
            # print(i, ":", i-n)
            a.append(i-n)
    return a

def u(n):
    a = []
    for i in range(-30, 30):
        if i<n:
            a.append(0)
            # print(i, ":", 0)
        else:
            a.append(1)
            # print(i, ":", 1)
    return a

x = [x11 - x22 for (x11, x22) in zip(u(0), u(12))]
y = [y11 - y22 - y33 - y44 for (y11, y22, y33, y44) in zip(r(0), r(4), r(12), r(16))]

recorded = signal.convolve(x, y)
x = np.arange(-30, 30, 0.1)
plt.plot(x,recorded)


# Show
plt.show()