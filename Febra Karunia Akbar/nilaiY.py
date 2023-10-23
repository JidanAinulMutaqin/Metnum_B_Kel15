def solve_gauss(coefficients, constants):
    n = len(coefficients)

    # Membuat matriks augmented
    augmented_matrix = [coefficients[i] + [constants[i]] for i in range(n)]

    # Menerapkan metode eliminasi Gauss
    for i in range(n):
        # Pilih baris dengan elemen terbesar di kolom i
        max_row = max(range(i, n), key=lambda j: abs(augmented_matrix[j][i]))
        augmented_matrix[i], augmented_matrix[max_row] = augmented_matrix[max_row], augmented_matrix[i]

        # Membuat elemen i, i menjadi 1
        factor = augmented_matrix[i][i]
        for j in range(i, n + 1):
            augmented_matrix[i][j] /= factor

        # Menghilangkan elemen i dari baris lainnya
        for j in range(n):
            if j != i:
                factor = augmented_matrix[j][i]
                for k in range(i, n + 1):
                    augmented_matrix[j][k] -= factor * augmented_matrix[i][k]

    # Mengambil solusi dari matriks augmented
    solution = [row[-1] for row in augmented_matrix]

    return solution

# Contoh penggunaan
coefficients = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
constants = [8, -11, -3]

result = solve_gauss(coefficients, constants)  # Temukan solusi SPL menggunakan fungsi solve_gauss
print("Solusi SPL:", result)
