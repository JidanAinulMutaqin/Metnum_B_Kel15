import numpy as np  # Mengimpor pustaka NumPy untuk operasi numerik.
import matplotlib.pyplot as plt  # Mengimpor pustaka Matplotlib untuk membuat grafik.

# Modifikasi 2.1: Program berhenti setelah n iterasi
def my_bisection_max_iter(f, a, b, e, max_iter=1000):
    # Jika tanda fungsi pada a dan b sama, lemparkan exception.
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception('Tidak ada akar pada interval a dan b')
    
    m = (a + b) / 2  # Menghitung titik tengah interval [a, b].
    
    # Jika nilai mutlak dari f(m) < e atau mencapai maksimum iterasi, return m (akar ditemukan atau batas iterasi tercapai).
    if np.abs(f(m)) < e or max_iter == 0:
        return m
    
    # Jika tanda f(a) dan f(m) sama, akar berada di interval [m, b].
    elif np.sign(f(a)) == np.sign(f(m)):
        return my_bisection_max_iter(f, m, b, e, max_iter-1)
    
    # Jika tanda f(b) dan f(m) sama, akar berada di interval [a, m].
    elif np.sign(f(b)) == np.sign(f(m)):
        return my_bisection_max_iter(f, a, m, e, max_iter-1)

# Modifikasi 2.2: User dapat menginputkan fungsi, batas, dan galat
def user_input_bisection():
    f_input = input("Masukkan fungsi (gunakan x sebagai variabel): ")  # Meminta input fungsi dari pengguna.
    a = float(input("Masukkan batas a: "))  # Meminta input batas a dari pengguna dan mengonversinya ke float.
    b = float(input("Masukkan batas b: "))  # Meminta input batas b dari pengguna dan mengonversinya ke float.
    e = float(input("Masukkan galat (e): "))  # Meminta input galat dari pengguna dan mengonversinya ke float.
    result = my_bisection_max_iter(lambda x: eval(f_input), a, b, e)  # Memanggil my_bisection_max_iter dengan fungsi yang dievaluasi dari input pengguna.
    print("Hasil akar:", result)  # Mencetak hasil akar.

# Modifikasi 2.3: Akar ditampilkan dalam grafik
def plot_function(f, a, b, root=None):
    x = np.linspace(a, b, 100)  # Menghasilkan 100 titik dari a hingga b.
    y = f(x)  # Menghitung nilai fungsi f pada setiap titik x.
    plt.plot(x, y, label='f(x)')  # Membuat plot f(x).
    if root is not None:
        plt.plot(root, f(root), 'ro', label='Root')  # Menandai akar pada plot jika ada.
    plt.xlabel('x')  # Memberi label sumbu x.
    plt.ylabel('f(x)')  # Memberi label sumbu y.
    plt.legend()  # Menampilkan legenda (jika ada).
    plt.show()  # Menampilkan grafik.

# Gabungkan semua modifikasi
user_input_bisection()  # Memanggil fungsi untuk mengambil input dari pengguna dan mencari akar.