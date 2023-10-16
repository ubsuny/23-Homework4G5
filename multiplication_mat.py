import numpy as np
import time
import matplotlib.pyplot as plt

# Creating two matrices A, B of dimension 3x3
A = np.array([[200, 533, 233], [532, 332, 534], [6342, 4434, 3434]])
B = np.array([[4454, 5545, 5456], [2423, 434, 345], [6434, 84, 344]])

# Method 1: Manual matrix multiplication using nested loops
def matrix_multiply_manual(A, B):
    C = np.zeros((A.shape[0], B.shape[1]))
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(A.shape[1]):
                C[i, j] += A[i, k] * B[k, j]    
    return C

# Method 2: NumPy's built-in matrix multiplication
def np_matrix_multiply(A, B):
    return np.dot(A, B)

# Method 3: Matrix multiplication using Einstein notation
def matrix_multiply_einsum(A, B):
    return np.einsum('ij,jk->ik', A, B)

methods = [matrix_multiply_manual, np_matrix_multiply, matrix_multiply_einsum]
method_names = ["Manual", "NumPy", "Einstein Notation"]
time_list = []

# Open a log file to write execution times
with open('execution_times.log', 'w') as log_file:
    # Measure execution time for each method
    for method, name in zip(methods, method_names):
        start_time = time.time()
        C = method(A, B)
        end_time = time.time()
        execution_time = end_time - start_time
        time_list.append(execution_time)
        
        # Write execution time to log file
        log_file.write(f"{name} Execution Time: {execution_time} seconds\n")

# Plotting Results
# plt.bar(method_names, time_list)
# plt.ylabel('Time (s)')
# plt.title('Execution Time of Different Matrix Multiplication Methods')
# plt.savefig('multiplication_methods_comparison.png')
