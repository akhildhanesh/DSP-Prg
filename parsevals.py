import numpy as np

N = 5

x1 = np.random.sample(N)
x2 = np.random.sample(range(1, 10), N)
x3 = np.conj(x2)

LHS = sum(x1*x3)

x4 = np.fft.fft(x1, axis=0)
x5 = np.fft.fft(x2, axis=0)
x6 = np.conj(x5)

RHS = 1/5*(sum(x4*x6))

print(LHS, RHS, LHS==RHS)
