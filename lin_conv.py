import numpy as np
from random import sample

a = np.array(sample(range(1, 10), 6))
b = np.array(sample(range(1, 10), 6))

print(a, b)

N = a.size + b.size - 1

a1 = np.concatenate([a, np.zeros(N-a.size)])
b1 = np.concatenate([b, np.zeros(N-b.size)])

y = np.zeros(N)

for i in range(N):
    for j in range(i+1):
        y[i] += a1[j] * b1[i-j]

print(y)
