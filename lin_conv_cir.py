import numpy as np


g=np.array([1, 2, 3, 4])
h=np.array([1, 2, 3, 4])

L = g.size
M = h.size

N = L + M - 1

g1 = np.zeros(N-L)
h1 = np.zeros(N-M)

g2 = np.concatenate([g, g1])
h2 = np.concatenate([h, h1])

print(f'g = {g2}, h = {h2}')


def linconv(g, h):
  h = np.concatenate([[h[0]], h[:0:-1]])
  y = np.zeros(N)

  for n in np.arange(N):
    y[n] = np.sum(g*h)  
    h = np.roll(h,1)

  return y

print(f'y(n) = {linconv(g2, h2)}')
