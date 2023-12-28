# mendefinisikan fungsi simpson yang menerima empat parameter
def simpson(fungsi, a, b, n): 
# fungsi(fungsi yang akan diintegralkan), a dan b (batas-batas integrasi), n (jumlah subinterval)
    h = (b - a) / n
    x = [a + i * h for i in range(n+1)]
    
    integral = 0
    
    for i in range(n):
        integral += (h / 6) * (fungsi(x[i]) + 4 * fungsi((x[i] + x[i+1]) / 2) + fungsi(x[i+1]))
    
    return integral

# contoh fungsi yang akan diintegralkan 
def f(x):
    return x**2

a = 0
b = 2
n = 100

# memanggil fungsi simpson
hasil_integral = simpson(f, a, b, n)

# menampilkan hasil integral
print("Hasil Integral:", hasil_integral)