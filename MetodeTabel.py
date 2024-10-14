import re
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def Intro():
    print("\n +------------------------+")
    print(" |      Metode Tabel      |")
    print(" +------------------------+\n")

def f(x):
    pass

Intro()

#Input
Fungsi = input(" Masukkan Fungsi  : ")
Batas_Bawah = int(input(" Batas bawah      : "))
Batas_Atas = int(input(" Batas atas       : "))
Iterasi_Maksimum = int(input(" Iterasi Maksimum : "))

# Kebutuhan sistem
h = (Batas_Atas - Batas_Bawah) / Iterasi_Maksimum
Fungsi = Fungsi.replace('E', 'e').replace('X','x')
Fungsi = re.sub(r'\s+', '', Fungsi)
Fungsi = re.sub(r'(\d+)(x)', r'\1*\2', Fungsi)
Fungsi = re.sub(r'e\^([a-zA-Z0-9]+)', r'math.exp(\1)', Fungsi)

# Definisikan fungsi dengan exec
Fungsi_Baru = f"""
def f(x):
    return {Fungsi}
"""
exec(Fungsi_Baru)

# Header tabel
print("\n +----------+----------+-------------+-------------+---------------------+")
print(" | Iterasi  |    xi    |    f(xi)    |  f(x(i+1))  |  f(xi)*f(x(i+1))    |")
print(" +----------+----------+-------------+-------------+---------------------+")

# Operasi
xi_values = []
f_xi_values = []
Iterasi = 0
while Iterasi <= Iterasi_Maksimum:
    xi = Batas_Bawah + Iterasi * h
    xi_1 = Batas_Bawah + (Iterasi + 1) * h
    
    f_xi = f(xi)
    f_xi_1 = f(xi_1)

    xi_values.append(xi)
    f_xi_values.append(f_xi)

    if Iterasi == Iterasi_Maksimum:
        print(f" | {Iterasi:<8} | {xi:<8.4f} | {f_xi:<11.4f} |")
        print(" +----------+----------+-------------+")
        break

    f_xi__f_xi_1 = f_xi * f_xi_1
    
    print(f" | {Iterasi:<8} | {xi:<8.4f} | {f_xi:<11.4f} | {f_xi_1:<11.4f} | {f_xi__f_xi_1:<19.4f} |")
    print(" +----------+----------+-------------+-------------+---------------------+")
    
    Iterasi += 1
    # Plotting
fig, ax = plt.subplots()
line, = plt.plot(xi_values, f_xi_values)  # Save reference to the plotted line
plt.xlabel('xi')
plt.ylabel('f(xi)')
plt.title('Metode Tabel')   

# Add slider for interactive plot
axcolor = 'lightgoldenrodyellow'
ax_h = plt.axes([0.25, .03, 0.50, 0.02], facecolor=axcolor)
h_slider = Slider(ax_h, 'h', 0.1, 10.0, valinit=h)

def update(val):
    h = h_slider.val
    xi_values = []
    f_xi_values = []
    Iterasi = 0
    while Iterasi <= Iterasi_Maksimum:
        xi = Batas_Bawah + Iterasi * h
        f_xi = f(xi)
        xi_values.append(xi)
        f_xi_values.append(f_xi)
        Iterasi += 1

    # Update the plot with new values
    line.set_xdata(xi_values)
    line.set_ydata(f_xi_values)
    ax.relim()  # Recalculate limits
    ax.autoscale_view()  # Rescale the view
    fig.canvas.draw_idle()  # Redraw the figure

# Connect the slider to the update function
h_slider.on_changed(update)

# Show the plot
plt.show()


