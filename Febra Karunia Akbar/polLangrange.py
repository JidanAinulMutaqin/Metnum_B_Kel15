def lagrange_basis(x, i, x_values):
    basis = 1
    xi = x_values[i]
    for j, xj in enumerate(x_values):
        if i != j:
            basis *= (x - xj) / (xi - xj)  # Menghitung dasar Lagrange
    return basis

def lagrange_interpolation(x, x_values, y_values):
    result = 0
    for i in range(len(x_values)):
        result += y_values[i] * lagrange_basis(x, i, x_values)  # Menghitung hasil interpolasi Lagrange
    return result

# Input nilai x dan y dari pengguna
n = int(input("Jumlah titik data: "))
x_values = []
y_values = []

for i in range(n):
    x = float(input(f"Masukkan nilai x-{i}: "))
    y = float(input(f"Masukkan nilai y-{i}: "))
    x_values.append(x)
    y_values.append(y)

# Input nilai yang akan diinterpolasi
x_interpolate = float(input("Masukkan nilai x yang akan diinterpolasi: "))

# Lakukan interpolasi
interpolated_value = lagrange_interpolation(x_interpolate, x_values, y_values)

print(f"Hasil interpolasi pada x={x_interpolate}: {interpolated_value}")
