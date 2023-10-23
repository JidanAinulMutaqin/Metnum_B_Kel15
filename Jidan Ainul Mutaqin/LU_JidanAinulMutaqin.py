import numpy as np

def lu_decomposition(a, b):
    n = len(a)
    l = np.zeros((n, n))
    u = np.zeros((n, n))

    for j in range(n):
        for i in range(j+1):
            # Hitung p1 untuk uij
            p1 = sum(l[i][k] * u[k][j] for k in range(i))
            u[i][j] = a[i][j] - p1

        for i in range(j, n):
            # Hitung p2 untuk lij
            p2 = sum(l[i][k] * u[k][j] for k in range(j))
            l[i][j] = (a[i][j] - p2) / u[j][j]

    return l, u

def solve_lu(l, u, b):
    n = len(l)
    y = np.zeros(n)
    x = np.zeros(n)

    # Solusi Ly = b
    for i in range(n):
        y[i] = b[i] - sum(l[i][j] * y[j] for j in range(i))

    # Solusi Ux = y
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - sum(u[i][j] * x[j] for j in range(i+1, n))) / u[i][i]

    return x

# Contoh penggunaan
a = [[2, -1, 1],
     [1, 3, 2],
     [1, 1, 1]]

b = [5, 10, 6]

# Hitung matriks L dan U
l, u = lu_decomposition(a, b)

# Solusi x
x = solve_lu(l, u, b)

# Output hasil
print("Matriks L:")
print(l)

print("\nMatriks U:")
print(u)

print("\nSolusi x:")
print(x)