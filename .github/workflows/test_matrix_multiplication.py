# Importing necessary libraries
import numpy as np
import time
import matplotlib.pyplot as plt

# List to store the names of methods used
method_list = ["For Loops", "NumPy", "EinSum"]  # List to store methods used
time_list = [0, 0, 0]  # List to store execution time for each method

# Creating two matrices A, B of dimension 3x3
A = np.array([[200, 533, 233], [532, 332, 534], [6342, 4434, 3434]])
B = np.array([[4454, 5545, 5456], [2423, 434, 345], [6434, 84, 344]])

# Method 1: Manual matrix multiplication using nested loops
def matrix_multiply_manual(A, B):
    """
    Perform matrix multiplication using nested loops.

    Parameters:
    - A (numpy.ndarray): The first matrix.
    - B (numpy.ndarray): The second matrix.

    Returns:
    - C (numpy.ndarray): The result of matrix multiplication.
    """
    C = np.zeros((A.shape[0], B.shape[1]))
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(A.shape[1]):
                C[i, j] += A[i, k] * B[k, j]    
    return C

# Method 2: NumPy's built-in matrix multiplication
def np_matrix_multiply(A, B):
    """
    Perform matrix multiplication using NumPy's built-in function.

    Parameters:
    - A (numpy.ndarray): The first matrix.
    - B (numpy.ndarray): The second matrix.

    Returns:
    - C (numpy.ndarray): The result of matrix multiplication.
    """
    return np.dot(A, B)

# Method 3: Matrix multiplication using Einstein notation
def matrix_multiply_einsum(A, B):
    """
    Perform matrix multiplication using Einstein notation.

    Parameters:
    - A (numpy.ndarray): The first matrix.
    - B (numpy.ndarray): The second matrix.

    Returns:
    - C (numpy.ndarray): The result of matrix multiplication.
    """
    return np.einsum('ij,jk->ik', A, B)

# Measure execution time for each method
start_time = time.time()
C1 = matrix_multiply_manual(A, B)
end_time = time.time()
time_list[0] = end_time - start_time
print(f"Method 1 (Manual) Execution Time: {end_time - start_time} seconds")

start_time = time.time()
C2 = np_matrix_multiply(A, B)
end_time = time.time()
time_list[1] = end_time - start_time
print(f"Method 2 (NumPy) Execution Time: {end_time - start_time} seconds")

start_time = time.time()
C3 = matrix_multiply_einsum(A, B)
end_time = time.time()
time_list[2] = end_time - start_time
print(f"Method 3 (Einstein Notation) Execution Time: {end_time - start_time} seconds")

#Unit tests:
#setting expected value of multiplication (calculated with calculator)
expected_product = np.array([[3681381,1359894,1355237],[6609720,3138884,3200828],[61085206,37379202,37312978]])

#testing method 1
are_equal1 = np.array_equal(matrix_multiply_manual(A, B), expected_product)
assert are_equal1 == True, "method 1 fails"

#testing method 2
are_equal2 = np.array_equal(np_matrix_multiply(A, B), expected_product)
assert are_equal1 == True, "method 2 fails"

#testing method 3
are_equal3 = np.array_equal(matrix_multiply_einsum(A, B), expected_product)
assert are_equal1 == True, "method 3 fails"


# Plotting Results

# Create a bar graph
plt.bar(method_list, time_list)

# Adding labels and title
plt.ylabel('Time (s)')
plt.title('Execution Time of a Program Calculating Multiplication of two 3x3 Matrices')

# Display the plot
plt.show()
