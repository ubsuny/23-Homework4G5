import numpy as np
import time

# List to store the names of methods used
method_list = ["For Loops", "NumPy", "EinSum"]
time_list = [0, 0, 0]

A = np.array([[200, 533, 233], [532, 332, 534], [6342, 4434, 3434]])
B = np.array([[4454, 5545, 5456], [2423, 434, 345], [6434, 84, 344]])

expected_product = np.array([[3681381,1359894,1355237],[6609720,3138884,3200828],[61085206,37379202,37312978]])

def matrix_multiply_manual(A, B):
    C = np.zeros((A.shape[0], B.shape[1]))
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(A.shape[1]):
                C[i, j] += A[i, k] * B[k, j]    
    return C

def np_matrix_multiply(A, B):
    return np.dot(A, B)

def matrix_multiply_einsum(A, B):
    return np.einsum('ij,jk->ik', A, B)

def test_matrix_multiply_manual():
    result = matrix_multiply_manual(A, B)
    assert np.array_equal(result, expected_product), "method 1 fails"

def test_np_matrix_multiply():
    result = np_matrix_multiply(A, B)
    assert np.array_equal(result, expected_product), "method 2 fails"

def test_matrix_multiply_einsum():
    result = matrix_multiply_einsum(A, B)
    assert np.array_equal(result, expected_product), "method 3 fails"
