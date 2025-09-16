"""
Q2. Develop a Python program to generate an array list and showcase the concepts of slicing and indexing on arrays for 3-D array.
"""
print("\nQuestion 2\n")

import numpy as np

# Create a 3D array (2x3x4)
arr1 = np.arange(1, 25).reshape(2, 3, 4)
print("3D Array:\n", arr1)

# Indexing
print("\nElement at [1][2][3]:", arr1[1][2][3])   # 2nd block, 3rd row, 4th col

# Slicing
print("\nFirst block:\n", arr1[0])                          # 2D matrix
print("\nSecond row of first block:\n", arr1[0][1])         # 1D matrix
print("\nAll blocks, first column:\n", arr1[:, :, 0])       # 1st column from all blocks


"""
Q3. Develop a Python program to generate an array list with only odd numbers between 1 to 30 using python function and showcase the concepts of slicing and indexing on 3-D array
"""
print("\nQuestion 3\n")

# Odd numbers between 1 and 30
odds = np.array([x for x in range(1, 31) if x % 2 != 0])
print("Odd Numbers (1-30):\n", odds)

# Reshape into 3D array (3x5x1 since 3*5*1 = 15)
arr2 = odds.reshape(3, 5, 1)
print("\n3D Array with odds:\n", arr2)

# Indexing
print("\nElement at [0][1][0]:", arr2[0][1][0])

# Slicing
print("\nFirst block:\n", arr2[0])
print("\nLast column of all rows (second block):\n", arr2[1, :, 0])


"""
Q4. Develop a Python program that generates a 3-D array and executes the following
operations on its elements:
🔹Extract the inner matrix.
🔹Sort the elements rowswise and columnwise
"""
print("\nQuestion 4\n")

# Create 3D array (2x3x3)
arr3 = np.random.randint(1, 50, (2, 3, 3))
print("3D Array:\n", arr3)

# Extract inner matrix (first block)
inner_matrix = arr3[0]
print("\nExtracted inner matrix:\n", inner_matrix)

# Row-wise sort
row_sorted = np.sort(inner_matrix, axis=1)
print("\nRow-wise sorted:\n", row_sorted)

# Column-wise sort
col_sorted = np.sort(inner_matrix, axis=0)
print("\nColumn-wise sorted:\n", col_sorted)
