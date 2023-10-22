def forward_substitution(matrix, b):
    n = len(matrix)
    x = [0] * n

    for i in range(n):
        x[i] = b[i]
        for j in range(i):
            x[i] -= matrix[i][j] * x[j]
        x[i] /= matrix[i][i]

    return x

def backward_substitution(matrix, b):
    n = len(matrix)
    x = [0] * n

    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= matrix[i][j] * x[j]
        x[i] /= matrix[i][i]

    return x

def el_gauss(matrix, b):
    upper_triangle = True  # Check if the matrix is upper triangular

    for i in range(len(matrix)):
        for j in range(i):
            if matrix[i][j] != 0:
                upper_triangle = False
                break

    if upper_triangle:
        x = backward_substitution(matrix, b)
    else:
        x = forward_substitution(matrix, b)

    return x

# Contoh penggunaan
A = [
    [2, 1, -1],
    [0, 2, -3],
    [0, 0, 5]
]

b = [8, -3, 5]

solution = el_gauss(A, b)
print("Solusi sistem persamaan linear:")
for i, x in enumerate(solution):
    print(f'x{i+1} = {x}')
