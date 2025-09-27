import time
import random

def space():
    print("-" * 30)

# --- Helper Functions for Pure Python ---

# Q5: Manual Flattening
def manual_flatten(arr_3d):
    flat_list = []
    for block in arr_3d:
        for row in block:
            flat_list.extend(row)
    return flat_list

# Q6: Manual Diagonal Extraction
def manual_diag(matrix):
    # Works only for square matrices (n x n)
    return [matrix[i][i] for i in range(len(matrix))]

# Q7: Manual Broadcasting Addition (Scalar/Vector)
def manual_add(mat1, mat2):
    # Handles scalar + array or 2D array + 1D vector (broadcast across rows)
    if isinstance(mat2, int) or isinstance(mat2, float):
        # Scalar addition
        return [[x + mat2 for x in row] for row in mat1]
    
    # Check for 2D list + 1D list (broadcast across rows)
    if isinstance(mat1[0], list) and not isinstance(mat2[0], list):
        if len(mat1[0]) != len(mat2):
            raise ValueError(f"Pure Python Broadcasting Error: dimensions must be equal for this simple broadcast. List 1 rows size ({len(mat1[0])}) must match list 2 size ({len(mat2)}).")
        
        result = []
        for row in mat1:
            new_row = [row[i] + mat2[i] for i in range(len(row))]
            result.append(new_row)
        return result
    
    # Handle Row + Column (requires a full outer addition)
    if not isinstance(mat1[0], list) and isinstance(mat2[0], list):
        # mat1 is [1, 2, 3], mat2 is [[10], [20], [30]]
        rows_m1 = len(mat1)
        cols_m2 = len(mat2)
        
        result = []
        for i in range(rows_m1):
            new_row = []
            for j in range(cols_m2):
                new_row.append(mat1[i] + mat2[j][0])
            result.append(new_row)
        return result
    
    raise ValueError("Unsupported Pure Python addition for this demonstration.")


# --- Pure Python Execution Start ---
print("\n--- Pure Python Operations with Execution Time (Q5, Q6, Q7) ---")
python_start_time = time.time()

"""
# Q5. Flattening a 3D list into 1D.
"""

print("\nQuestion 5: Flattening a 3D List\n")

# Create a 3D List (2x3x4)
numbers = list(range(1, 25))
py_arr_q5 = [
    [numbers[i:i+4] for i in range(0, 12, 4)],
    [numbers[i:i+4] for i in range(12, 24, 4)]
]
print("Original 3D List:\n", py_arr_q5)

# Flatten
py_flattened = manual_flatten(py_arr_q5)
print("\nFlattened 1D List:\n", py_flattened)
space()

"""
# Q6. Create 4x4 matrix and display the diagonal elements.
"""

print("\nQuestion 6: Diagonal Elements\n")

# Create 4x4 list with random integers between 1 and 50
py_arr_q6 = [[random.randint(1, 50) for _ in range(4)] for _ in range(4)]
print("4x4 List:\n", py_arr_q6)

# Diagonal elements
py_diag = manual_diag(py_arr_q6)
print("\nDiagonal Elements:", py_diag)
space()

"""
# Q7. Demonstrate Broadcasting rules with examples (Manual Implementation)
"""

print("\nQuestion 7: Manual Broadcasting\n")

# 1. Scalar to array
py_arr_q7_scalar = [1, 2, 3]
result_scalar = [x + 5 for x in py_arr_q7_scalar]
print(f"1. Scalar Addition ({py_arr_q7_scalar} + 5):\n", result_scalar)

# 2. Row vector + Column vector (Simulating outer addition)
py_row = [1, 2, 3]
py_col = [[10], [20], [30]]
result_row_col = [[r + c[0] for r in py_row] for c in py_col] # Manual Outer Addition
print(f"\n2. Row + Column (Manual Outer Addition):\n", result_row_col)

# 3. 2D + 1D (Vector broadcast across rows)
py_mat = [[1, 2, 3], [4, 5, 6]]
py_vec = [10, 20, 30]
result_mat_vec = manual_add(py_mat, py_vec)
print(f"\n3. Matrix + Vector (Manual Broadcast):\n", result_mat_vec)

# Shape mismatch error
try:
    a_fail = [[1, 2], [3, 4]]
    b_fail = [1, 2, 3]
    manual_add(a_fail, b_fail)
except ValueError as e:
    print("\n4. Broadcasting Error Example:", e)

python_end_time = time.time()
python_execution_time = python_end_time - python_start_time
print(f"\n--- Pure Python Execution Time: {python_execution_time:.6f} seconds ---")
print("-" * 50)