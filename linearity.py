from random import sample
import numpy as np
from dft import dft

N = 4

a = np.array([7])
b = np.array([6])
x1 = np.array(sample(range(1, 2*N), N))
x2 = np.array(sample(range(1, 2*N), N))

X1 = np.round(dft(x1))
X2 = np.round(dft(x2))

print(dft(a*x1+b*x2), a*X1+b*X2)

# DFT function (DFT module)
def dft(x):
    N = x.size
    y = np.zeros(N, dtype=np.cdouble)
    for k in range(N):
        for n in range(N):
            y[k] += x[n] * np.exp(-1j*2*np.pi*n*k/N)
    return np.round(y)
