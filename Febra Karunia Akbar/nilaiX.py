import numpy as np

def solveUXY(U, Y):
    n = len(Y)  # Menentukan ordo matriks U
    X = np.zeros(n, dtype=float)  # Inisialisasi vektor X dengan nol

    for i in range(n - 1, -1, -1):
        X[i] = (Y[i] - np.dot(U[i, i + 1:], X[i + 1:])) / U[i, i]  # Menghitung nilai X[i] dengan substitusi mundur

    return X

# Meminta input dari pengguna
n = int(input("Masukkan ordo matriks (n): "))

# Meminta input untuk matriks segitiga atas U
print("Masukkan elemen-elemen matriks segitiga atas U:")
U = np.zeros((n, n), dtype=float)
for i in range(n):
    for j in range(i, n):
        elem = float(input(f"U[{i+1},{j+1}]: "))
        U[i, j] = elem

# Meminta input untuk vektor Y
print("Masukkan elemen-elemen vektor Y:")
Y = np.zeros(n, dtype=float)
for i in range(n):
    elem = float(input(f"Y[{i+1}]: "))
    Y[i] = elem

solusi_X = solveUXY(U, Y)  # Temukan solusi menggunakan fungsi solveUXY
print("Solusi X =", solusi_X)
