import numpy as np
# Implementations of matrix multiplication methods
def matrix_multiply_manual(A, B):
    C = np.zeros((A.shape[0], B.shape[1]))
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(A.shape[1]):
                C[i, j] += A[i, k] * B[k, j]
    return C

def matrix_multiply_with_dot(A, B):
    return np.dot(A, B)

def matrix_multiply_einsum(A, B):
    return np.einsum('ij,jk->ik', A, B)

def test_matrix_multiply_manual(A, B, expected_product):
    result = matrix_multiply_manual(A, B)
    print("Method 1 (Manual) Result:")
    print(result)
    m1 = (f"M1(Manual) fails\nExpected:\n{expected_product}\nGot:\n{result}")
    assert np.array_equal(result, expected_product), m1

def test_matrix_multiply_with_dot(A, B, expected_product):
    result = matrix_multiply_with_dot(A, B)
    print("\nMethod 2 (NumPydot) Result:")
    print(result)
    m2 = (f"M(2NumPydot) fails\nExpected:\n{expected_product}\nGot:\n{result}")
    assert np.array_equal(result, expected_product), m2

def test_matrix_multiply_einsum(A, B, expected_product):
    result = matrix_multiply_einsum(A, B)
    print("\nMethod 3 (EinSum) Result:")
    print(result)
    m3 = (f"M3(EinSum) fails\nExpected:\n{expected_product}\nGot:\n{result}")
    assert np.array_equal(result, expected_product), m3

if __name__ == '__main__':
    A = np.array([[200, 533, 233], [532, 332, 534], [6342, 4434, 3434]])
    B = np.array([[4454, 5545, 5456], [2423, 434, 345], [6434, 84, 344]])
    expected_product = np.array([
        [3681381, 1359894, 1355237],
        [6609720, 3138884, 3200828],
        [61085206, 37379202, 37312978]
    ])
    print("Expected Product:")
    print(expected_product)
    
    test_matrix_multiply_manual(A, B, expected_product)
    test_matrix_multiply_with_dot(A, B, expected_product)
    test_matrix_multiply_einsum(A, B, expected_product)
    
    print("\nAll tests passed!")
