# Square Matrix Multiply
# Strassen Algorithm

import numpy as np


def strassen_multiply(A, B):
    if len(A) == 1:
        return A * B

    n = len(A)
    half_n = n // 2

    A11 = A[:half_n, :half_n]
    A12 = A[:half_n, half_n:]
    A21 = A[half_n:, :half_n]
    A22 = A[half_n:, half_n:]

    B11 = B[:half_n, :half_n]
    B12 = B[:half_n, half_n:]
    B21 = B[half_n:, :half_n]
    B22 = B[half_n:, half_n:]

    P1 = strassen_multiply(A11 + A22, B11 + B22)
    P2 = strassen_multiply(A21 + A22, B11)
    P3 = strassen_multiply(A11, B12 - B22)
    P4 = strassen_multiply(A22, B21 - B11)
    P5 = strassen_multiply(A11 + A12, B22)
    P6 = strassen_multiply(A21 - A11, B11 + B12)
    P7 = strassen_multiply(A12 - A22, B21 + B22)

    C11 = P1 + P4 - P5 + P7
    C12 = P3 + P5
    C21 = P2 + P4
    C22 = P1 - P2 + P3 + P6

    result = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))

    return result


# Example Testing
A = np.random.randint(0, 10, (4, 4))
B = np.random.randint(0, 10, (4, 4))

print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)

result = strassen_multiply(A, B)
print("\nResult:")
print(result)
