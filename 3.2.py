import numpy as np
import matplotlib.pyplot as plt


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

# original signal1
chart1 = plt.subplot(311)
x1 = np.arange(-10, 10, 1)
y1 = [x11 - x22 for (x11, x22) in zip(u(0), u(3))]
plt.stem(x1, y1)

# original signal2
chart1 = plt.subplot(312)
x2 = np.arange(-10, 10, 1)
y2 = [x11 - x22 for (x11, x22) in zip(u(0), u(2))]
plt.stem(x2, y2)

# Convolution
chart2 = plt.subplot(313)
x = np.arange(-20, 19, 1)
y_conv = np.convolve(y1, y2)
plt.stem(x, y_conv)
# Show
plt.show()