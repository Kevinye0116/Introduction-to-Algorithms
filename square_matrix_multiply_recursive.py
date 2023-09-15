# Square Matrix Multiplication
# Divide and Conquer Algorithm --- Recursive


def matrix_multiply_recursive(A, B):
    n = len(A)

    if n <= 1:
        return [A[0][0] * B[0][0]]

    half_size = n // 2
    A11 = [row[:half_size] for row in A[:half_size]]
    A12 = [row[half_size:] for row in A[:half_size]]
    A21 = [row[:half_size] for row in A[half_size:]]
    A22 = [row[half_size:] for row in A[half_size:]]

    B11 = [row[:half_size] for row in B[:half_size]]
    B12 = [row[half_size:] for row in B[:half_size]]
    B21 = [row[:half_size] for row in B[half_size:]]
    B22 = [row[half_size:] for row in B[half_size:]]

    C11 = matrix_multiply_recursive(A11, B11) + matrix_multiply_recursive(A12, B21)
    C12 = matrix_multiply_recursive(A11, B12) + matrix_multiply_recursive(A12, B22)
    C21 = matrix_multiply_recursive(A21, B11) + matrix_multiply_recursive(A22, B21)
    C22 = matrix_multiply_recursive(A21, B12) + matrix_multiply_recursive(A22, B22)

    result = []
    for i in range(n):
        row = []
        for j in range(n):
            if i < half_size:
                if j < half_size:
                    row.append(C11[i][j])
                else:
                    row.append(C12[i][j - half_size])
            else:
                if j < half_size:
                    row.append(C21[i - half_size][j])
                else:
                    row.append(C22[i - half_size][j - half_size])
        result.append(row)

    return result


# Example Testing
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = matrix_multiply_recursive(A, B)
for row in result:
    print(row)
