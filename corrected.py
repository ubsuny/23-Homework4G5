import numpy as np


# Implementations of matrix multiplication methods
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


# Test functions
A = np.array([[200, 533, 233], [532, 332, 534], [6342, 4434, 3434]])
B = np.array([[4454, 5545, 5456], [2423, 434, 345], [6434, 84, 344]])
expected_product = np.array([
    [3681381, 1359894, 1355237],
    [6609720, 3138884, 3200828],
    [61085206, 37379202, 37312978]
])


def test_matrix_multiply_manual():
    result = matrix_multiply_manual(A, B)
    print("Method 1 (Manual) Result:")
    print(result)
    assert np.array_equal(result, expected_product), f"Method 1 (Manual) fails\nExpected:\n{expected_product}\nGot:\n{result}"


def test_np_matrix_multiply():
    result = np_matrix_multiply(A, B)
    print("\nMethod 2 (NumPy) Result:")
    print(result)
    assert np.array_equal(result, expected_product), f"Method 2 (NumPy) fails\nExpected:\n{expected_product}\nGot:\n{result}"


def test_matrix_multiply_einsum():
    result = matrix_multiply_einsum(A, B)
    print("\nMethod 3 (EinSum) Result:")
    print(result)
    assert np.array_equal(result, expected_product), f"Method 3 (EinSum) fails\nExpected:\n{expected_product}\nGot:\n{result}"


if __name__ == '__main__':
    print("Expected Product:")
    print(expected_product)
    test_matrix_multiply_manual()
    test_np_matrix_multiply()
    test_matrix_multiply_einsum()
    print("\nAll tests passed!")
