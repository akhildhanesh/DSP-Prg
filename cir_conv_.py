import numpy as np

g = np.array([4, 3, 5, 6])
h = np.array([1, 2])

n1 = g.size
n2 = h.size

N = max(n1, n2)

g1 = np.concatenate([g, np.zeros(N-n1)])
h1 = np.concatenate([h, np.zeros(N-n2)])

print(g1, h1)

def cir_con(g, h):
    h2 = np.concatenate([[h[0]], h[:0:-1]])
    y = np.zeros(N)

    for i in range(N):
        y[i] = np.sum(g1*h2)
        h2 = np.roll(h2, shift=1)
        
    return y

print(cir_con(g1, h1))
