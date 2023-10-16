"""
This module performs matrix multiplication using various methods and 
tests their correctness and performance.
"""

import time
import numpy as np

# List to store the names of methods used and execution time for each method
METHOD_LIST = ["For Loops", "NumPy", "EinSum"]
TIME_LIST = [0, 0, 0]

# Creating two matrices matrix_a, matrix_b of dimension 3x3
MATRIX_A = np.array([[200, 533, 233], [532, 332, 534], [6342, 4434, 3434]])
MATRIX_B = np.array([[4454, 5545, 5456], [2423, 434, 345], [6434, 84, 344]])

def matrix_multiply_manual(matrix_a, matrix_b):
    """
    Perform matrix multiplication using nested loops.
    """
    result_matrix = np.zeros((matrix_a.shape[0], matrix_b.shape[1]))
    for i in range(matrix_a.shape[0]):
        for j in range(matrix_b.shape[1]):
            for k in range(matrix_a.shape[1]):
                result_matrix[i, j] += matrix_a[i, k] * matrix_b[k, j]
    return result_matrix

def np_matrix_multiply(matrix_a, matrix_b):
    """
    Perform matrix multiplication using NumPy's built-in function.
    """
    return np.dot(matrix_a, matrix_b)

def matrix_multiply_einsum(matrix_a, matrix_b):
    """
    Perform matrix multiplication using Einstein notation.
    """
    return np.einsum('ij,jk->ik', matrix_a, matrix_b)

# Setting expected value of multiplication (calculated with calculator)
EXPECTED_PRODUCT = np.array([
    [3681381, 1359894, 1355237],
    [6609720, 3138884, 3200828],
    [61085206, 37379202, 37312978]
])

def test_matrix_multiply_manual():
    """Test matrix multiplication using nested loops."""
    result = matrix_multiply_manual(MATRIX_A, MATRIX_B)
    assert np.array_equal(result, EXPECTED_PRODUCT), "Method 1 fails"

def test_np_matrix_multiply():
    """Test matrix multiplication using NumPy's built-in function."""
    result = np_matrix_multiply(MATRIX_A, MATRIX_B)
    assert np.array_equal(result, EXPECTED_PRODUCT), "Method 2 fails"

def test_matrix_multiply_einsum():
    """Test matrix multiplication using Einstein notation."""
    result = matrix_multiply_einsum(MATRIX_A, MATRIX_B)
    assert np.array_equal(result, EXPECTED_PRODUCT), "Method 3 fails"

# Measure execution time for each method
if __name__ == "__main__":
    start_time = time.time()
    _ = matrix_multiply_manual(MATRIX_A, MATRIX_B)
    end_time = time.time()
    TIME_LIST[0] = end_time - start_time
    print(f"Method 1 (Manual) Execution Time: {end_time - start_time:.4f} seconds")

    start_time = time.time()
    _ = np_matrix_multiply(MATRIX_A, MATRIX_B)
    end_time = time.time()
    TIME_LIST[1] = end_time - start_time
    print(f"Method 2 (NumPy) Execution Time: {end_time - start_time:.4f} seconds")

    start_time = time.time()
    _ = matrix_multiply_einsum(MATRIX_A, MATRIX_B)
    end_time = time.time()
    TIME_LIST[2] = end_time - start_time
    print(f"Method 3 (Einstein Notation) Execution Time: {end_time - start_time:.4f} seconds")
