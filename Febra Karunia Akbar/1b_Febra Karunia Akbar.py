import numpy as np  # Mengimpor pustaka NumPy untuk operasi numerik.

# Fungsi penyelesaian dengan metode Bagi Dua
def my_bisection(f, a, b, e, max_iter=1000):
    # Jika tanda fungsi pada a dan b sama, lemparkan exception
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception('Tidak ada akar pada interval a dan b')
    
    m = (a + b) / 2  # Menghitung titik tengah interval [a, b].
    
    # Jika nilai mutlak dari f(m) < e, return m (akar ditemukan dengan akurasi yang memadai).
    if np.abs(f(m)) < e:
        return m
    
    # Jika mencapai maksimum iterasi, lemparkan exception.
    elif max_iter == 0:
        raise Exception('Maksimum iterasi tercapai')
        
    # Jika tanda f(a) dan f(m) sama, akar berada di interval [m, b].
    elif np.sign(f(a)) == np.sign(f(m)):
        return my_bisection(f, m, b, e, max_iter-1)
    
    # Jika tanda f(b) dan f(m) sama, akar berada di interval [a, m].
    elif np.sign(f(b)) == np.sign(f(m)):
        return my_bisection(f, a, m, e, max_iter-1)

f2 = lambda x: np.exp(x) - x  # Definisi fungsi f2(x) = e^x - x.

# Memanggil fungsi my_bisection untuk mencari akar dari f2 pada interval [-1, 1] dengan galat 0.001.
r2 = my_bisection(f2, -1, 1, 0.001)
print("r2 =", r2)  # Mencetak nilai akar r2.
print("f(r2) =", f2(r2))  # Mencetak nilai f2(r2).