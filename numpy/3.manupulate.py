import numpy as np

x = np.array([1, 2, 3, 4, 5])
print(x[1:3])  # similar to python list slicing

x1 = np.array([
    [1, 3],
    [5, 7],
    [7, 9]
])

# print using loop
print('print using Normal Loop')
for row in x1:
    print(row)

# print in 1d array
print('print using Flat')
for item in x1.flat:
    print(item)

r1 = np.arange(6).reshape(3, 2)
r2 = np.arange(6, 12).reshape(3, 2)

# stacking / merging both arrays vertically (y-axis)
vertical_stack = np.vstack((r1, r2))
print(f'vertical_stacking : {vertical_stack}')

# stacking / merging both arrays horizontally(x-axis)
horizontal_stack = np.hstack((r1, r2))
print(f'horizontal_stacking:  {horizontal_stack}')

r3 = np.arange(30).reshape(2, 15)  # generated 2d array with 2 rows 15 columns
print(f'Array : {r3}')

# equally dividing arrays horizontally
horizontally_splitted_array = np.hsplit(r3,
                                        3)  # it divides generated array into equal 2d arrays horizontally ( here  5 column each )
print(f'Equally divided array horizontally (x-axis) : {horizontally_splitted_array}')

# equally dividing arrays vertically
vertically_splitted_array = np.vsplit(r3,
                                      2)  # it divides generated array into equal 2d arrays horizontally ( here  5 column each )
print(f'Equally divided array vertically : {vertically_splitted_array}')

# boolean indexing using np array (Important)
arr = np.arange(12).reshape(3, 4)
bool_match = arr > 4  # convert true or false for each element based on condition and returns an array
print(f'Normal Array :  {arr}')
print(f'Conditional array :  {bool_match}')
print(f'Matched indexes :  {arr[bool_match]}')  # returns list of matched indexes on array based on the above condition
arr[bool_match] = -1 # changes the true value i.e. matched indexes with -1 on original array
print(f'Array now : {arr}')
