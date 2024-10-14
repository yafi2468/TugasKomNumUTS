import math
import matplotlib.pyplot as plt
import numpy as np

bawah = float(input("Masukkan batas bawah: "))
atas = float(input("Masukkan batas atas: "))
N = int(input("Masukkan Maksimum Iterasi: "))
print("")



h = float((atas - bawah) / N)
i = 0
hasil = None

x_array = []
fx1_array= []
fx2_array = []
fx3_array = []

def f(x):
    return math.exp(-x) - x

while i <= N:
    x = bawah + (i * h)
    fx1 = f(x)
    fx2 = f(bawah + ((i + 1) * h))
    fx3 = fx1 * fx2
    
    x_array.append(x)
    fx1_array.append(fx1)
    fx2_array.append(fx2)
    fx3_array.append(fx3)
    
    if fx1 == 0:
        hasil = x
    elif fx1 * fx2 < 0:
        if abs(fx1) < abs(fx2):
            hasil = x
        else:
            hasil = x + h
    
    print(i, round(x, 2), " ", round(fx1, 7), " ", round(fx2, 5), round(fx3, 5))
    i += 1

if hasil is not None:
    print("Akar ditemukan pada x =", hasil)
else:
    print("Akar tidak ditemukan dalam batas iterasi yang diberikan.")

def Plot_Style_Artis():
    fig, ax = plt.subplots(figsize=(5, 2.7))
    x = np.arange(len(x_array))
    ax.plot(x, np.cumsum(x_array), color='blue', linewidth=3, linestyle='--')
    l, = ax.plot(x, np.cumsum(fx1_array), color='orange', linewidth=2)
    l.set_linestyle(':')
    plt.show()

print("Plot Style Artis mau?")
inputan = input("Y/N: ")
if inputan == "y":
    Plot_Style_Artis()