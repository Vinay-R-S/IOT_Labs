import numpy as np

"""
Q5. Implement a NumPy program to flatten a 3D array into 1D.
"""
print("\nQuestion 5\n")

arr = np.arange(1, 25).reshape(2, 3, 4)
print("Original 3D Array:\n", arr)

# Flatten
flattened = arr.flatten()
print("\nFlattened 1D Array:\n", flattened)


"""
Q6. Create 4x4 matrix filled with random integers between 1 and 50, and display the diagonal elements.
"""
print("\nQuestion 6\n")

arr = np.random.randint(1, 51, (4, 4))
print("4x4 Matrix:\n", arr)

# Diagonal elements
diag = np.diag(arr)
print("\nDiagonal Elements:", diag)


"""
Q7. Demonstrate rules of Broadcasting in NumPy with examples
"""
print("\nQuestion 7\n")


# Adding scalar to array
arr = np.array([1, 2, 3])
print("Array + 5:\n", arr + 5)

# Row vector + Column vector
row = np.array([1, 2, 3])
col = np.array([[10], [20], [30]])
print("\nRow + Column (broadcasting):\n", row + col)

# 2D + 1D
mat = np.array([[1, 2, 3], [4, 5, 6]])
vec = np.array([10, 20, 30])
print("\nMatrix + Vector:\n", mat + vec)

# Shape mismatch error (for demo)
try:
    a = np.array([[1, 2], [3, 4]])
    b = np.array([1, 2, 3])
    print("\nThis will fail:\n", a + b)
except ValueError as e:
    print("\nBroadcasting Error Example:", e)
