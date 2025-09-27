import numpy as np
import time

def space():
    print("-" * 30)

print("\n--- NumPy Operations with Execution Time ---")
numpy_start_time = time.time()

"""
Q2. 3D Array Indexing and Slicing
"""

print("\nQuestion 2: 3D Array Indexing and Slicing\n")

# Create a 3D array (2x3x4)
arr1 = np.arange(1, 25).reshape(2, 3, 4)
print("3D Array (Shape: 2x3x4):\n", arr1)
space()

# --- Indexing ---
element_index = arr1[1, 2, 3]
print(f"Element at [1, 2, 3]: {element_index}")
space()

# --- Slicing ---
slice_block_0 = arr1[0]
print("Slice 1: First block (arr1[0]) - A 3x4 matrix:\n", slice_block_0)
space()

slice_row_1_block_0 = arr1[0, 1, :]
print("Slice 2: Second row of first block (arr1[0, 1, :]) - A 1D array:\n", slice_row_1_block_0)
space()

slice_col_0_all = arr1[:, :, 0]
print("Slice 3: First column from all blocks (arr1[:, :, 0]) - Shape 2x3:\n", slice_col_0_all)

"""
# Q3. Odd Numbers, Reshaping, and 3D Slicing
"""

print("\nQuestion 3: Odd Numbers, Reshaping, and 3D Slicing\n")

# Odd numbers between 1 and 30
odds = np.array([x for x in range(1, 31) if x % 2 != 0])
print("Odd Numbers (1-30, 15 elements):\n", odds)
space()

# Reshape into 3D array (3x5x1)
arr2 = odds.reshape(3, 5, 1)
print("3D Array with odds (Shape: 3x5x1):\n", arr2)
space()

# --- Indexing ---
element_index_q3 = arr2[0, 1, 0]
print(f"Element at [0, 1, 0]: {element_index_q3} (The number 3)")
space()

# --- Slicing ---
slice_block_0_q3 = arr2[0]
print("Slice 1: First block (arr2[0]) - A 5x1 matrix:\n", slice_block_0_q3)
space()

slice_second_block_rows = arr2[1, :, 0]
print("Slice 2: All rows of the second block, squeezed (arr2[1, :, 0]):\n", slice_second_block_rows)

"""
# Q4. Extracting and Sorting in 3D Array
"""

print("\nQuestion 4: Extracting and Sorting in 3D Array\n")

# Create 3D array (2x3x3)
arr3 = np.random.randint(1, 50, (2, 3, 3))
print("3D Array (Shape: 2x3x3):\n", arr3)
space()

# --- Extract the inner matrix ---
inner_matrix = arr3[0]
print("Extracted Inner Matrix (arr3[0]):\n", inner_matrix)
space()

# --- Sort the elements row-wise and column-wise ---
row_sorted = np.sort(inner_matrix, axis=1)
print("Row-wise sorted (axis=1):\n", row_sorted)
space()

col_sorted = np.sort(inner_matrix, axis=0)
print("Column-wise sorted (axis=0):\n", col_sorted)

numpy_end_time = time.time()
numpy_execution_time = numpy_end_time - numpy_start_time
print(f"--- NumPy Execution Time: {numpy_execution_time:.6f} seconds ---")
print("-" * 50)