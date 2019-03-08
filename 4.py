# import math
import numpy as np
import matplotlib.pyplot as plt

m = input()
print(m)
pi = np.pi

# Continuous
chart1 = plt.subplot(311)
x = np.arange(-30, 30, 0.01)
y1 = np.sin(2*pi*0.043*x)
y2 = np.sin(2*pi*0.031*x)
y = y1+y2
plt.plot(x,y)

# Discrete
x = np.arange(-30, 30, 1)
y1 = np.sin(2*pi*0.043*x)
y2 = np.sin(2*pi*0.031*x)
y = y1+y2
plt.stem(x,y)

# Continuous with down sampling
chart2 = plt.subplot(312)
x = np.arange(-30, 30, 0.01)
y1 = np.sin(int(m)*2*pi*0.043*x)
y2 = np.sin(int(m)*2*pi*0.031*x)
y = y1+y2
plt.plot(x,y)

# Discrete with down sampling
x = np.arange(-30, 30, 1)
y1 = np.sin(int(m)*2*pi*0.043*x)
y2 = np.sin(int(m)*2*pi*0.031*x)
y = y1+y2
plt.stem(x,y)

# Draw both normal & down sampling: Continuous
chart3 = plt.subplot(313)
x = np.arange(-30, 30, 0.01)
y1 = np.sin(2*pi*0.043*x)
y2 = np.sin(2*pi*0.031*x)
y = y1+y2
plt.plot(x,y)
y1 = np.sin(int(m)*2*pi*0.043*x)
y2 = np.sin(int(m)*2*pi*0.031*x)
y = y1+y2
plt.plot(x,y)

# Draw both normal & down sampling: Discrete
x = np.arange(-30, 30, 1)
y1 = np.sin(2*pi*0.043*x)
y2 = np.sin(2*pi*0.031*x)
y = y1+y2
plt.stem(x,y)
y1 = np.sin(int(m)*2*pi*0.043*x)
y2 = np.sin(int(m)*2*pi*0.031*x)
y = y1+y2
plt.stem(x,y)

#show
plt.show()