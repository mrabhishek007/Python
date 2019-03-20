import numpy as np

a1 = np.array([
    [1, 2],
    [4, 5]
])

a2 = np.array([
    [10, 20],
    [100, 200]
])

# shape must be shame in-order to perform operations on 2 arrays together
print(f'Addition in two 2d array :: {a1 + a2}')  # addition
print(f'Subtraction in two 2d array :: {a1 - a2}')  # subtraction
print(f'Matrix mul between two 2d array :: {a1.dot(a2)}')  # matrix multiplication


print(f' sum along horizontal axis in an 2d array {a1.sum(axis=0)} ')
print(f' sum along vertical axis in an 2d array  {a1.sum(axis=1)} ')