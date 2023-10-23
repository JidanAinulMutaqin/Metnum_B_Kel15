def forward_substitution(matrix, b):
    n = len(matrix)
    x = [0] * n

    for i in range(n):
        x[i] = b[i]  # Masukkan elemen dari b ke dalam solusi sementara x
        for j in range(i):
            x[i] -= matrix[i][j] * x[j]  # Kurangi dengan hasil perkalian elemen matriks dengan solusi yang sudah diketahui
        x[i] /= matrix[i][i]  # Bagi dengan elemen diagonal matriks

    return x

def backward_substitution(matrix, b):
    n = len(matrix)
    x = [0] * n

    for i in range(n - 1, -1, -1):
        x[i] = b[i]  # Masukkan elemen dari b ke dalam solusi sementara x
        for j in range(i + 1, n):
            x[i] -= matrix[i][j] * x[j]  # Kurangi dengan hasil perkalian elemen matriks dengan solusi yang sudah diketahui
        x[i] /= matrix[i][i]  # Bagi dengan elemen diagonal matriks

    return x

def el_gauss(matrix, b):
    upper_triangle = True  # Periksa apakah matriks berbentuk segitiga atas

    for i in range(len(matrix)):
        for j in range(i):
            if matrix[i][j] != 0:
                upper_triangle = False
                break

    if upper_triangle:
        x = backward_substitution(matrix, b)  # Jika segitiga atas, gunakan substitusi mundur
    else:
        x = forward_substitution(matrix, b)  # Jika tidak, gunakan substitusi maju

    return x

# Contoh penggunaan
A = [
    [2, 1, -1],
    [0, 2, -3],
    [0, 0, 5]
]

b = [8, -3, 5]

solution = el_gauss(A, b)  # Temukan solusi menggunakan eliminasi Gauss
print("Solusi sistem persamaan linear:")
for i, x in enumerate(solution):
    print(f'x{i+1} = {x}')
