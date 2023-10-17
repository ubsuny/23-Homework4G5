# test_matrix_multiplication.py
import time
import numpy as np
from matrix_multiplication import *

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
