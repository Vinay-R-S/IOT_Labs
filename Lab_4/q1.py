"""
Q1.Develop a Python program that generates a 2-D array and executes the following operations on its
elements:
🔹Determine the number of elements in each dimension.
🔹Identify the Data type of the matrix
🔹Determine the dimension of the matrix
🔹Compute inverse and transpose of the matrix
🔹Determine eigen and determinant values
🔹Create identity matrix
🔹Create an array filled with ones
🔹Create an array filled with zeros
🔹Demonstrate empty() method
🔹Convert the given array to float type
🔹Sort the elements in either ascending and descending order
🔹Identify any unique elements present in the array.
🔹Compute inverse and transpose of the matrix
🔹Calculate the square and square root of each element
🔹Raise each element to a specified power
🔹Compute the mean and median values of the elements
🔹Determine the sum, minimum, and maximum values of the elements
🔹Calculate the variance and standard deviation
🔹Matrix multiplication
🔹Demonstrate flatten() function
🔹splitting arrays
🔹Iterating arrays
🔹Find the number of rows and columns of the array
🔹Change the shape of the array using reshape.
🔹Concatenation of an arrays
🔹Stacking arrays
🔹Demonstrate arrange and linspace
"""

import numpy as np

def space():
    print("\n")

# Creating a 2D array
arr = np.array([[4,6,2],[7,2,8],[1,5,8]])
print(arr)
space()

# Determine the number of elements in each dimension.
print(f"Total number of elements in dimension 1: {np.size(arr)} \nTotal number of elements in dimension 2: {np.size(arr[0])}")
space()

# Identify the Data type of the matrix
print(f"Data type of matrix: {type(arr[0][0])}")
space()

# Determine the dimension of the matrix
print(f"Dimension of the Matrix: {np.shape(arr)}")
space()

# Compute inverse and transpose of the matrix
print(f"Inverse of matrix arr: \n{np.invert(arr)} \nTranspose of matrix arr: \n{np.transpose(arr)}")
space()

# Determine eigen and determinant values
determinant = np.linalg.det(arr)
eigenvalues, eigenvectors = np.linalg.eig(arr)
print(f"Determinant of matrix arr: {determinant}")
print(f"Eigen values: {eigenvalues} \nEigen vectors: \n{eigenvectors}")
space()

# Create identity matrix
identity_mat = np.identity(3)
print(f"Indentity matrix: \n{identity_mat}")
space()

# Create an array filled with ones
one_mat = np.ones((3,3))
print(f"One matrix: \n{one_mat}")
space()

# Create an array filled with zeros
zero_mat = np.zeros((3,3))
print(f"Zero matrix: \n{zero_mat}")
space()

# Demonstrate empty() method - This method will create a matrix of given dimension and with garbage values without initialization
empty_mat = np.empty((3,4))
print(f"Empty Matrix: \n{empty_mat}")
space()

# Convert the given array to float type
float_arr = np.float64(arr)
print(f"Type casting matrix arr from int64 to float64: \n{float_arr}")
space()

# Sort the elements in either ascending and descending order
sort_arr = np.sort(arr, axis=None).reshape(arr.shape)
print(f"The sorted array: \n{sort_arr}")
space()

# Identify any unique elements present in the array.
unique_elements = np.unique(arr)
print(f"The unique elements in the matrix arr: {unique_elements}")
space()

# Calculate the square and square root of each element
square_arr = np.square(arr)
square_root_arr = np.sqrt(arr)
print(f"The Square of the elements in the matrix: \n{square_arr}\n\nThe Square root of the elements in the matrix: \n{square_root_arr}")
space()

# Raise each element to a specified power
power_arr = np.pow(arr, 3)
print(f"Each element of matrix raised by power 3: \n{power_arr}")
space()

# Compute the mean and median values of the elements
mean_arr = np.mean(arr)
median_arr = np.median(arr)
print(f"Mean of the matrix arr: {mean_arr} \nMedian of matrix arr: {median_arr}")
space()

# Determine the sum, minimum, and maximum values of the matrix
sum = np.sum(arr)
min = np.min(arr)
min = np.max(arr)
print(f"Sum: {sum} \nMin: {min} \nMax: {max}")
space()

# Calculate the variance and standard deviation
var = np.var(arr) 
std = np.sqrt(var)
print(f"Variance of matrix arr: {var} \nStandard deviation of matrix arr: {std}")
space()

# Matrix multiplication
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix_muliplication = np.matmul(arr, arr2)
print(f"Multiplication of matrix arr x arr2: \n{matrix_muliplication}")
space()

# Demonstrate flatten() function - flatten function is used to convert the multi dimensions matrix to 1D
flat_arr = arr.flatten()
print(f"Flattened matrix arr: {flat_arr}")
space()

# splitting arrays
split_arr = np.split(arr, 3) 
print(f"The matrix is slpit row-wise: \n{split_arr}")
space()

# Iterating arrays
for oneD_arr in arr:
    print(oneD_arr, end=" ")
space()

# Find the number of rows and columns of the array
row, col = np.shape(arr)
print(f"Row: {row} \nColumn: {col}")
space()

# Change the shape of the array using reshape.
reshaped_arr = np.reshape(arr, (1,9))
print(f"Reshaped array is: {reshaped_arr}")
space()

# Concatenation of an arrays
concat_arr = np.concatenate((arr, arr2), axis=0)
print(f"The concatenated array: \n{concat_arr}")
space()

# Stacking arrays
# Vertical stack
vstack_arr = np.vstack((arr, arr2))
print("\nVertical Stack:\n", vstack_arr)

# Horizontal stack
hstack_arr = np.hstack((arr, arr2))
print("\nHorizontal Stack:\n", hstack_arr)

# Depth stack (adds a new axis)
dstack_arr = np.dstack((arr, arr2))
print("\nDepth Stack (3D):\n", dstack_arr)
space()

# Demonstrate arrange and linspace
arrange_arr = np.arange(1, 10, 2)
linespace_arr = np.linspace(1, 2, 5)
print(f"The arranged array: {arrange_arr}\n The linespaced array: {linespace_arr}")
space()
