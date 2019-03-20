import numpy as np

a1 = np.arange(100)  # create a np array of 100 size where each index will contain index value
a2 = np.arange(100)

print(a1 + a2)  # add two numpy array. we can perform any mathematical operation in this way

# creating 1d array

a3 = np.array([10, 20, 30])
print(f'1D Array : {a3}')

# creating 2d array

a4 = np.array([
    [10, 20],
    [100, 200],
    [1000, 2000]
], dtype=np.float)  # by default dtype parameter is optional & default type is int
a4[0][1] = 95
print(f'2D Array : {a4}')
print(f'Dimension of  Array : {a4.ndim}, Data type : {a4.dtype}, Data type size : {a4.itemsize}')
print(f'total-array-size : {a4.size}, length: {len(a4)}, shape of array : {a4.shape}   ')

# creating an 2d array with shape(row, col)
a5 = np.zeros((4, 3))
print(a5)
a5 = np.ones((4, 3))
print(a5)
a6 = np.arange(10)
print(a6)
a7 = np.arange(1, 15, 2)  # start , stop , steps (creates array starting from 1 to 15 with 2 steps each)
print(a7)
a8 = np.linspace(1, 5, 20)  # generates 20 linear sequence of number between 1 to 5
print(a8)

a9 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(f'reshaped array : {a9.reshape(3, 2)}')
print(f'reshaped array : {a9.reshape(6, 1)}')
print(f'making 1d array : {a9.flatten()}, or  {a9.ravel()}')

max_val = a9.max()
min_val = a9.min()
sum_val = a9.sum()

print(f'max val : {max_val}, min val: {min_val},  sum: {sum_val}')

print(f'sum of col values : {a9.sum(axis=0)}, sum of rows values : {a9.sum(axis=1)}')

print(f'square root of arrays val : {np.sqrt(a9)}')
