𝑥[𝑛]=𝑢[𝑛]−𝑢[𝑛−3],ℎ[𝑛]=𝑢[𝑛]−𝑢[𝑛−2]
import numpy as np
import matplotlib.pyplot as plt

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

# First signal
print("Please enter the array of x1:")
x1 = list(map(int, input().split()))
print("Please enter the array of y1:")
y1 = list(map(int, input().split()))

# Second signal
print("Please enter the array of x2:")
x2 = list(map(int, input().split()))
print("Please enter the array of y2:")
y2 = list(map(int, input().split()))

# Convolution
x_conv = np.arange(-10, 10, 1)
y_conv = np.convolve(x1, x2)

# original signal1
chart1 = plt.subplot(311)
plt.plot(x1, y1)

# original signal2
chart1 = plt.subplot(311)
plt.plot(x2, y2)

# Convolution
chart2 = plt.subplot(312)
plt.plot(x_conv, y_conv)

plt.show()