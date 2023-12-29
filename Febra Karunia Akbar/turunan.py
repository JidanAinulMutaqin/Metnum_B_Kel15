# mendefinisikan fungsi hitung turunan untuk rumus metode
def hitung_turunan(fungsi, x, h):
    turunan_maju = (fungsi(x + h) - fungsi(x)) / h
    turunan_mundur = (fungsi(x) - fungsi(x - h)) / h
    turunan_pusat = (fungsi(x + h) - fungsi(x - h)) / (2 * h)
    
    return turunan_maju, turunan_mundur, turunan_pusat

# mendefinisikan fungsi yang ingin kita turunkan
def f(x):
    return x**2

x0 = 2
h0 = 0.001

turunan_maju, turunan_mundur, turunan_pusat = hitung_turunan(f, x0, h0)

# menampilkan hasil turunan
print("Turunan Maju:", turunan_maju)
print("Turunan Mundur:", turunan_mundur)
print("Turunan Pusat:", turunan_pusat)