import numpy as np
import matplotlib.pyplot as plt


#continuous
x = np.arange(-10, 10, 0.1)
y = np.cos(6*x/7)
plt.plot(x,y)

#discrete
x = np.arange(-10, 10, 1)
y = np.cos(6*x/7)
plt.stem(x,y)

#show
plt.show()
