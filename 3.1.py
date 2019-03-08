import numpy as np
import matplotlib.pyplot as plt
import math

############ YOU HAVE TO ENTER 10 NUMBERS FOR EACH PART #########

# First signal
x1 = np.arange(0, 10, 1)
print("Please enter the array of y1:")
y1 = list(map(int, input().split()))

# Second signal
x2 = np.arange(0, 10, 1)
print("Please enter the array of y2:")
y2 = list(map(int, input().split()))

# Convolution
x = np.arange(0, 19, 1)
y_conv = np.convolve(y1, y2)
print(y_conv)

# original signal1
chart1 = plt.subplot(311)
plt.plot(x1, y1)

# original signal2
chart1 = plt.subplot(312)
plt.plot(x2, y2)

# Convolution
chart2 = plt.subplot(313)
plt.plot(x, y_conv)
# Show
plt.show()