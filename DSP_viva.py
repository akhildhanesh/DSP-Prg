# -*- coding: utf-8 -*-
"""DSP LAB VIVA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/akhildhanesh/bf87ce7f6226ab0e7173c889de9a9475/dsp-lab-viva.ipynb

*   Write a prg to find the linear convolution of the given sequence x1(n) = {1, 2, 3, 4} & x2(n) = {1, 2, 3, 4}
"""

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

"""* Write a function to implement DFT of sequence x(n) = {1, 2, 2, 4, 5}. Plot its magnitude and phase spectrum."""

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 2, 4, 5])

def dft(x):
  N = x.size
  D = np.empty((N,N),dtype=np.cdouble)
  W  =np.exp(-1j*2*np.pi/N)

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

"""* Write a prg to perform circular convolution of the given sequence x₁(n) = {1, 2, 3} & x₂(n) = {1, 1, 1, 1}"""

import numpy as np


g=np.array([1, 2, 3])
h=np.array([1, 1, 1, 1])

L = g.size
M = h.size

N = max(L, M)

g1 = np.zeros(N-L)
h1 = np.zeros(N-M)

g2 = np.concatenate([g, g1])
h2 = np.concatenate([h, h1])

print(f'g = {g2}, h = {h2}')


def circonv(g, h):
  h = np.concatenate([[h[0]], h[:0:-1]])
  y = np.zeros(N)

  for n in np.arange(N):
    y[n] = np.sum(g*h)  
    h = np.roll(h,1)

  return y

print(f'y(n) = {circonv(g2, h2)}')

"""* Write a prg to verify the relationship between linear & circular convolution"""

import numpy as np


g=np.array([1, 2, 3, 4])
h=np.array([1, 2, 3, 4])

def circular_conv(g, h):    
  L = g.size
  M = h.size

  N = max(L, M)

  g1 = np.zeros(N-L)
  h1 = np.zeros(N-M)

  g = np.concatenate([g, g1])
  h = np.concatenate([h, h1])

  print(f'Circular Convolution => g = {g}, h = {h}\n')

  h = np.concatenate([[h[0]], h[:0:-1]])

  y = np.zeros(N)

  for n in np.arange(N):
    y[n] = np.sum(g*h)  
    h = np.roll(h,1)

  return y

def linear_conv(g, h):
  L = g.size
  M = h.size

  N = L + M - 1

  g1 = np.zeros(N-L)
  h1 = np.zeros(N-M)

  g = np.concatenate([g, g1])
  h = np.concatenate([h, h1])

  print(f'Linear Convolution => g = {g}, h = {h}\n')

  h = np.concatenate([[h[0]], h[:0:-1]])
  y = np.zeros(N)

  for n in np.arange(N):
    y[n] = np.sum(g*h)  
    h = np.roll(h,1)

  return y

lin = linear_conv(g, h)

arr = np.split(lin, [max(L, M)])

arr[0] = np.concatenate([arr[0], np.zeros((max(arr[0].size, arr[1].size)-arr[0].size))])
arr[1] = np.concatenate([arr[1], np.zeros((max(arr[0].size, arr[1].size)-arr[1].size))])

print(f'\nCircular Convolution => y(n) = {circular_conv(g, h)}, Linear Convolution => g = {linear_conv(g, h)}')

LHS = arr[0] + arr[1]
RHS = circular_conv(g, h)

print(f'LHS = {LHS}, RHS = {RHS}', 'LHS = RHS, hence verified' if list(LHS) == list(RHS) else 'not equal')

"""* Write a prg to compute circular convolution of the given sequence  x₁(n) = {1, 2, 3, 4} & x₂(n) = {1, 2, 3, 4}. Find the linear convolution of the sequence x₁(n) & x₂(n), Compare the output of sequence."""

import numpy as np


g=np.array([1, 2, 3, 4])
h=np.array([1, 2, 3, 4])

def circular_conv(g, h):    
  L = g.size
  M = h.size

  N = max(L, M)

  g1 = np.zeros(N-L)
  h1 = np.zeros(N-M)

  g = np.concatenate([g, g1])
  h = np.concatenate([h, h1])

  print(f'Circular Convolution => g = {g}, h = {h}\n')

  h = np.concatenate([[h[0]], h[:0:-1]])

  y = np.zeros(N)

  for n in np.arange(N):
    y[n] = np.sum(g*h)  
    h = np.roll(h,1)

  return y

def linear_conv(g, h):
  L = g.size
  M = h.size

  N = L + M - 1

  g1 = np.zeros(N-L)
  h1 = np.zeros(N-M)

  g = np.concatenate([g, g1])
  h = np.concatenate([h, h1])

  print(f'Linear Convolution => g = {g}, h = {h}\n')

  y = np.zeros(N)

  for n in np.arange(N):
    y[n] = np.sum(g*h)  
    h = np.roll(h,1)

  return y

print(f'\nCircular Convolution => y(n) = {circular_conv(g, h)}, Linear Convolution => g = {linear_conv(g, h)}')
