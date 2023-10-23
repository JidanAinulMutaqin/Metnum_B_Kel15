def divided_difference(x_values, y_values):
    n = len(x_values)
    table = [[0] * n for _ in range(n)]
    
    for i in range(n):
        table[i][0] = y_values[i]

    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x_values[i + j] - x_values[i])

    return table

def newton_interpolation(x, x_values, table):
    n = len(x_values)
    result = table[0][0]

    for j in range(1, n):
        term = table[0][j]
        for i in range(j):
            term *= (x - x_values[i])
        result += term

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

# Hitung tabel perbedaan terbagi
table = divided_difference(x_values, y_values)

# Lakukan interpolasi
interpolated_value = newton_interpolation(x_interpolate, x_values, table)

print(f"Hasil interpolasi pada x={x_interpolate}: {interpolated_value}")