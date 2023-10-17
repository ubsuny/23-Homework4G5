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
