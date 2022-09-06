import numpy as np 
import matplotlib.pyplot as plt 
print()
print(" _  _ ___   ___              _ _       ")
print("| || |__ \ / _ \            (_) |      ")
print("| || |_ ) | | | | __ ___   ___| | __ _ ")
print("|__   _/ /| | | |/ _` \ \ / / | |/ _` |")
print("   | |/ /_| |_| | (_| |\ V /| | | (_| |")
print("   |_|____|\___/ \__,_| \_/ |_|_|\__,_|")
print()
print() 
def mandelbrot(re, im, max_iter):
    c = complex(re,im)
    z = 0.0j

    for i in range(max_iter):
        z = z*z + c
        if(z.real*z.real + z.imag*z.imag) >= 4:
            return i
    return max_iter

columnas = 3000
filas = 3000 

plano = np.zeros([columnas,filas])

for indice_fila, re in enumerate(np.linspace(-2,1,num=filas)):
    for indice_columna, im in enumerate(np.linspace(-1,1, num=columnas)):
        plano[indice_columna,indice_fila] = mandelbrot(re,im,100)

plt.figure(dpi=100)
plt.imshow(plano, cmap='viridis', extent=[-2,1,-1,1])
plt.show()

