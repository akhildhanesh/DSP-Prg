from scipy import fft
from random import sample
import numpy as np

N = 4
x = sample(range(1, 2*N), N)
print(x)

print(np.round(fft.fft(x, axis=0)))

y = np.zeros((N), dtype=np.cdouble)

for k in range(N):
    for n in range(N):
        y[k] += x[n] * np.exp((-1j*2*np.pi*k*n)/N)

print(np.round(y))

w = np.exp(-1j*2*np.pi/N)
d = np.zeros((N, N), dtype=np.cdouble)

for k in range(N):
    for n in range(N):
        d[k, n] = w**(k*n)

print(np.round(d@x))
