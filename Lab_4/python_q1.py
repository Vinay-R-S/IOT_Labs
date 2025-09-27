import time
import math

def space():
    print("\n")

# --- Pure Python Execution Start ---
print("--- Pure Python Operations ---")
python_start_time = time.time()

# Creating a 2D array (list of lists)
py_arr = [[4,6,2],[7,2,8],[1,5,8]]
print(f"Original List:\n{py_arr}")
space()

# Determine the number of elements in each dimension.
total_elements = sum(len(row) for row in py_arr)
if py_arr:
    row_elements = len(py_arr[0])
else:
    row_elements = 0
print(f"Total number of elements in dimension 1 (total): {total_elements} \nTotal number of elements in dimension 2 (row size): {row_elements}")
space()

# Identify the Data type of the matrix
# Data type is dynamic, checking first element
data_type = type(py_arr[0][0]) if py_arr and py_arr[0] else None
print(f"Data type of matrix elements (first element): {data_type}")
space()

# Determine the dimension of the matrix
rows = len(py_arr)
cols = len(py_arr[0]) if py_arr else 0
print(f"Dimension (shape) of the Matrix: ({rows}, {cols})")
space()

# Compute inverse (complex, skipped) and transpose of the matrix
# Transpose
py_transpose = [[py_arr[j][i] for j in range(len(py_arr))] for i in range(len(py_arr[0]))]
print(f"Transpose of list py_arr: \n{py_transpose}")
space()

# Determine eigen and determinant values (complex, skipped/simplified)
print("Determinant/Eigen: Requires external libraries or complex custom math. Skipped for pure Python comparison.")
space()

# Create identity matrix
py_identity = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
print(f"Indentity list: \n{py_identity}")
space()

# Create an array filled with ones
py_ones = [[1 for _ in range(3)] for _ in range(3)]
print(f"One list: \n{py_ones}")
space()

# Create an array filled with zeros
py_zeros = [[0 for _ in range(3)] for _ in range(3)]
print(f"Zero list: \n{py_zeros}")
space()

# Demonstrate empty() method - not applicable in pure Python, lists are initialized explicitly.
print("Empty list (equivalent): Not directly applicable; new lists are initialized with known values.")
py_uninitialized = [] # Placeholder
space()

# Convert the given array to float type
py_float = [[float(x) for x in row] for row in py_arr]
print(f"Type casting list py_arr to float: \n{py_float}")
space()

# Sort the elements in either ascending and descending order
py_flatten = [x for row in py_arr for x in row]
py_sort_asc = sorted(py_flatten)
py_sort_desc = sorted(py_flatten, reverse=True)
print(f"The sorted list (ascending, flattened): {py_sort_asc}")
print(f"The sorted list (descending, flattened): {py_sort_desc}")
space()

# Identify any unique elements present in the array.
py_unique = sorted(list(set(py_flatten)))
print(f"The unique elements in the list py_arr: {py_unique}")
space()

# Calculate the square and square root of each element
py_square = [[x**2 for x in row] for row in py_arr]
py_square_root = [[math.sqrt(x) for x in row] for row in py_arr]
print(f"The Square of the elements in the list: \n{py_square}\n\nThe Square root of the elements in the list: \n{py_square_root}")
space()

# Raise each element to a specified power
py_power = [[x**3 for x in row] for row in py_arr]
print(f"Each element of list raised by power 3: \n{py_power}")
space()

# Compute the mean and median values of the elements
py_sum = sum(py_flatten)
py_mean = py_sum / len(py_flatten)
py_median = (py_sort_asc[len(py_sort_asc)//2] + py_sort_asc[len(py_sort_asc)//2 - 1]) / 2 if len(py_sort_asc) % 2 == 0 else py_sort_asc[len(py_sort_asc)//2]
print(f"Mean of the list py_arr: {py_mean} \nMedian of list py_arr: {py_median}")
space()

# Determine the sum, minimum, and maximum values of the matrix
py_min = min(py_flatten)
py_max = max(py_flatten)
print(f"Sum: {py_sum} \nMin: {py_min} \nMax: {py_max}")
space()

# Calculate the variance and standard deviation
py_variance = sum((x - py_mean)**2 for x in py_flatten) / len(py_flatten)
py_std = math.sqrt(py_variance)
print(f"Variance of list py_arr: {py_variance} \nStandard deviation of list py_arr: {py_std}")
space()

# Matrix multiplication
py_arr2 = [[1,2,3],[4,5,6],[7,8,9]]
py_matrix_muliplication = [[sum(py_arr[i][k] * py_arr2[k][j] for k in range(len(py_arr2))) for j in range(len(py_arr2[0]))] for i in range(len(py_arr))]
print(f"Multiplication of list py_arr x py_arr2: \n{py_matrix_muliplication}")
space()

# Demonstrate flatten() function (already done)
print(f"Flattened list py_arr: {py_flatten}")
space()

# splitting arrays (by row)
py_split = [row for row in py_arr]
print(f"The list is split row-wise: \n{py_split}")
space()

# Iterating arrays
print("Iterating lists (by row):")
for oneD_list in py_arr:
    print(oneD_list, end=" ")
space()

# Find the number of rows and columns of the array (already done)
print(f"Row: {rows} \nColumn: {cols}")
space()

# Change the shape of the array using reshape (manual implementation)
py_reshaped = [py_flatten[i:i + 9] for i in range(0, len(py_flatten), 9)] # Reshape to 1x9
print(f"Reshaped list (1x9) is: {py_reshaped}")
space()

# Concatenation of an arrays
py_concat = py_arr + py_arr2
print(f"The concatenated list (row-wise): \n{py_concat}")
space()

# Stacking arrays (row stacking is concatenation)
py_vstack = py_arr + py_arr2
print("Vertical Stack (vstack):\n", py_vstack)
# Horizontal stack (element-wise concatenation)
py_hstack = [py_arr[i] + py_arr2[i] for i in range(len(py_arr))]
print("Horizontal Stack (hstack):\n", py_hstack)
print("Depth Stack (dstack): Complex, skipped.")
space()

# Demonstrate arrange and linspace
# Range (equivalent of arange)
py_range = list(range(1, 10, 2))
# Linspace (requires more complex calculation) - simplified range
py_linspace = [1 + i * (2 - 1) / (5 - 1) for i in range(5)]
print(f"The ranged list: {py_range}\n The linespaced list (simplified): {py_linspace}")
space()


python_end_time = time.time()
python_execution_time = python_end_time - python_start_time
print(f"--- Pure Python Execution Time: {python_execution_time:.6f} seconds ---")
print("-" * 50)