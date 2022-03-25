import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq

pi = np.pi
A1 = 1
A2 = 0.2
f1 = 5
f2 = 50
t = np.arange(0, 1, .0001)

y=A1*np.sin(2*pi*f1*t)+A2*np.sin(2*pi*f2*t)

# plt.plot(t, y)
# plt.show()

yf = fft(y)
xf = fftfreq(int(1/.0001), .0001)

plt.plot(xf, np.abs(yf))
plt.xlim([-60, 60])
plt.show()