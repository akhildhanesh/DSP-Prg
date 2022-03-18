"""
<--------------------------------------------------->DFT Module<--------------------------------------------------->

import numpy as np

def dft(x):
    N = x.size
    y = np.zeros(N, dtype=np.cdouble)
    for k in range(N):
        for n in range(N):
            y[k] += x[n] * np.exp(-1j*2*np.pi*n*k/N)
    return np.round(y)     


if __name__ == '__main__':
    arr = np.array([1,2,3,4])
    print(dft(arr), np.fft.fft(arr), dft(arr) == np.fft.fft(arr))
"""

from random import sample
from dft import dft, np

N = 4

a = np.array(sample(range(1, 2*N), 1))
b = np.array(sample(range(1, 2*N), 1))
x1 = np.array(sample(range(1, 2*N), N))
x2 = np.array(sample(range(1, 2*N), N))

X1 = np.round(dft(x1))
X2 = np.round(dft(x2))

LHS = dft(a*x1+b*x2)
RHS = a*X1+b*X2

print(LHS, RHS, '\nLHS = RHS; Therefore, Linearity Property is Proved' if (LHS == RHS).all() else 'Not Equal')
