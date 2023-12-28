# mendefinisikan fungsi trapesium
# fungsi(fungsi yang akan diintegralkan), a dan b (batas-batas integrasi), n (jumlah subinterval)
def trapesium(fungsi, a, b, n):
    
    h = (b - a) / n
    x = [a + i * h for i in range(n+1)]
    
    integral = 0
    
    for i in range(1, n):
        integral += fungsi(x[i])
    
    integral += (fungsi(a) + fungsi(b)) / 2
    integral *= h
    
    return integral

# contoh fungsi yang akan diintegralkan
def f(x):
    return x**2

a = 0
b = 2
n = 100

# memanggil fungsi metode trapesium
hasil_integral = trapesium(f, a, b, n)

# mencetak hasil integral
print("Hasil Integral:", hasil_integral)