import time

def space():
    print("-" * 30)

# Function to safely retrieve an element from a nested list (for indexing)
def get_element(arr, *indices):
    try:
        current = arr
        for index in indices:
            current = current[index]
        return current
    except IndexError:
        return None

# Function to get a slice (equivalent of arr[:, :, 0])
def slice_col_0(arr):
    # arr is 3D (Block x Row x Col). We want a 2D result (Block x Row)
    result = []
    for block in arr:
        block_result = []
        for row in block:
            # Append the first element of each row
            block_result.append(row[0])
        result.append(block_result)
    return result

# Function to sort a 2D list row-wise (axis=1)
def sort_rows(matrix):
    return [sorted(row) for row in matrix]

# Function to sort a 2D list column-wise (axis=0)
def sort_cols(matrix):
    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    
    # 1. Transpose the matrix
    transposed = [[matrix[r][c] for r in range(rows)] for c in range(cols)]
    
    # 2. Sort the transposed rows (which are the original columns)
    sorted_transposed = [sorted(col) for col in transposed]
    
    # 3. Transpose back
    return [[sorted_transposed[r][c] for r in range(cols)] for c in range(rows)]

# --- Pure Python Execution Start ---
print("\n--- Pure Python Operations with Execution Time ---")
python_start_time = time.time()

"""
# Q2. 3D Array Indexing and Slicing
"""

print("\nQuestion 2: 3D List Indexing and Slicing\n")

# Create a 3D List (2x3x4)
# Generate numbers 1 to 24
numbers = list(range(1, 25))
# Manually reshape: 2 blocks, 3 rows, 4 columns
py_arr1 = [
    [numbers[i:i+4] for i in range(0, 12, 4)], # Block 0 (1-12)
    [numbers[i:i+4] for i in range(12, 24, 4)] # Block 1 (13-24)
]
print("3D List (Shape: 2x3x4):\n", py_arr1)
space()

# --- Indexing ---
element_index = get_element(py_arr1, 1, 2, 3)
print(f"Element at [1, 2, 3]: {element_index}")
space()

# --- Slicing ---
# 1. Select the entire first block
slice_block_0 = py_arr1[0]
print("Slice 1: First block (py_arr1[0]) - A 3x4 list:\n", slice_block_0)
space()

# 2. Select the second row of the first block
slice_row_1_block_0 = py_arr1[0][1]
print("Slice 2: Second row of first block (py_arr1[0][1]) - A 1D list:\n", slice_row_1_block_0)
space()

# 3. Select the first column from all blocks
slice_col_0_all = slice_col_0(py_arr1)
print("Slice 3: First column from all blocks (Manual function) - Shape 2x3:\n", slice_col_0_all)

"""
# Q3. Odd Numbers, Reshaping, and 3D Slicing
"""

print("\nQuestion 3: Odd Numbers, Reshaping, and 3D Slicing\n")

# Odd numbers between 1 and 30 using Python list comprehension
py_odds = [x for x in range(1, 31) if x % 2 != 0]
print("Odd Numbers (1-30, 15 elements):\n", py_odds)
space()

# Reshape into 3D List (3x5x1)
# Manual reshape: 3 blocks, 5 rows, 1 column
py_arr2 = [
    [[x] for x in py_odds[i:i+5]] for i in range(0, 15, 5)
]
print("3D List with odds (Shape: 3x5x1):\n", py_arr2)
space()

# --- Indexing ---
element_index_q3 = get_element(py_arr2, 0, 1, 0)
print(f"Element at [0, 1, 0]: {element_index_q3} (The number 3)")
space()

# --- Slicing ---
# 1. Select the entire first block
slice_block_0_q3 = py_arr2[0]
print("Slice 1: First block (py_arr2[0]) - A 5x1 list:\n", slice_block_0_q3)
space()

# 2. Select all rows from the second block, and 'squeeze' the last dimension
# This means extracting the single element from each inner list of the second block.
slice_second_block_rows = [row[0] for row in py_arr2[1]]
print("Slice 2: All rows of the second block, squeezed:\n", slice_second_block_rows)

"""
# Q4. Extracting and Sorting in 3D Array
"""

print("\nQuestion 4: Extracting and Sorting in 3D List\n")

# Create 3D List (2x3x3) with random integers (simulated)
# Note: Python's random is used for simulation, not matrix operations.
import random
py_arr3 = [[[random.randint(1, 50) for _ in range(3)] for _ in range(3)] for _ in range(2)]
print("3D List (Shape: 2x3x3):\n", py_arr3)
space()

# --- Extract the inner matrix ---
inner_matrix = py_arr3[0]
print("Extracted Inner Matrix (py_arr3[0]):\n", inner_matrix)
space()

# --- Sort the elements row-wise and column-wise ---
# Row-wise sort (axis=1)
row_sorted = sort_rows(inner_matrix)
print("Row-wise sorted (Manual function):\n", row_sorted)
space()

# Column-wise sort (axis=0)
col_sorted = sort_cols(inner_matrix)
print("Column-wise sorted (Manual function):\n", col_sorted)

python_end_time = time.time()
python_execution_time = python_end_time - python_start_time
print(f"--- Pure Python Execution Time: {python_execution_time:.6f} seconds ---")
print("-" * 50)