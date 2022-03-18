import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 2, 4, 5])

def dft(x):
  N = x.size
  D = np.empty((N,N),dtype=np.cdouble)
  W = np.exp(-1j*2*np.pi/N)

  for k in np.arange(N):
    for n in np.arange(N):
        D[k,n] = W**(k*n)
    
  X=D@x
  return np.round(X)

dft_x = dft(x)
print(f'X(n) = {dft_x}')

plt.subplot(1,2,1)
plt.stem(dft_x.real)
plt.subplot(1,2,2)
plt.stem(dft_x.imag)
