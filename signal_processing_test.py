import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq
import scipy.signal as filter

pi = np.pi
A1 = 1
A2 = 0.2
f1 = 5
f2 = 50
t = np.arange(0, 1, .0001)

y=A1*np.sin(2*pi*f1*t)+A2*np.sin(2*pi*f2*t)

plt.plot(t, y)
plt.show()

yf = fft(y)
xf = fftfreq(int(1/.0001), .0001)

plt.plot(xf, np.abs(yf))
plt.xlim([-60, 60])
plt.show()

a, b = filter.iirnotch(50, 50/200, int(1/.0001))
print(a, b)
filtered_data = filter.lfilter(a, b, y)
yf = fft(filtered_data)
xf = fftfreq(int(1/.0001), .0001)
print(type(y[0]))
#plt.plot(xf, yf)
plt.plot(t, filtered_data)
plt.xlim([0, 1])
plt.show()