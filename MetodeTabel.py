def fungsi(x):
    return x ** 3 - 3*x + 7


# Input
Batas_Bawah = float(input("Batas Bawah : "))
Batas_Atas  = float(input("Batas Atas  : "))
Iterasi_Maksimum = float(input("Iterasi Maksimum : "))

Iterasi = 0
h = (Batas_Atas - Batas_Bawah) / Iterasi_Maksimum
hasil = 0

while (Iterasi<=Iterasi_Maksimum and Batas_Bawah<Batas_Atas):
    x = Batas_Atas+(Iterasi*h)
    f_x1 = fungsi(x)
    f_x2 = fungsi(x+1)

    if f_x1 == 0:
        hasil = x

    elif f_x1 * f_x2 < 0 :
        if abs(f_x1) < abs (f_x2):
            hasil = x
        else :
            hasil = x+1
    
    print(Iterasi, x , f_x1)
    Iterasi +=1
