# Importing necessary libraries
import numpy as np
import time
# import pytest

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


# Unit tests:
# setting expected value of multiplication (calculated with calculator)
expected_product = np.array([[3681381,1359894,1355237],[6609720,3138884,3200828],[61085206,37379202,37312978]])

def test_matrix_multiply_manual():
    result = matrix_multiply_manual(A, B)
    assert np.array_equal(result, expected_product), "Method 1 fails"

def test_np_matrix_multiply():
    result = np_matrix_multiply(A, B)
    assert np.array_equal(result, expected_product), "Method 2 fails"

def test_matrix_multiply_einsum():
    result = matrix_multiply_einsum(A, B)
    assert np.array_equal(result, expected_product), "Method 3 fails"

# Measure execution time for each method
if __name__ == "__main__":
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

