import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def r(n):
    a = []
    for i in range(-10, 10):
        if i<n:
            a.append(0)
            # print(i, ":", 0)
        else:
            # print(i, ":", i-n)
            a.append(i-n)
    return a

def u(n):
    a = []
    for i in range(-10, 10):
        if i<n:
            a.append(0)
            # print(i, ":", 0)
        else:
            a.append(1)
            # print(i, ":", 1)
    return a


# First signal
chart1 = plt.subplot(311)
x1 = np.arange(-10, 10, 1)
x = [x11 - x22 for (x11, x22) in zip(u(0), u(12))]
plt.plot(x1, x)

# Second signal
chart2 = plt.subplot(312)
x2 = np.arange(-10, 10, 1)
y = [y11 - y22 - y33 - y44 for (y11, y22, y33, y44) in zip(r(0), r(4), r(12), r(16))]
plt.stem(x2, y)

# Deconvolution
chart3 = plt.subplot(313)
x = np.arange(-19, 20, 1)
recovered, remainder = signal.deconvolve(x, y)
plt.stem(x,recovered)

# Show
plt.show()