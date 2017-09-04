import numpy as np
import pylab as pl
# crea un vector (arreglo) con los valores del eje X
x = [ 1, 2, 3, 4, 5]
# crea un vector (arreglo) con los valores del eje Y para cada valor en el eje x
y = [ 1, 4, 9, 16, 25]
# Grafica el vector x contra el vector y
pl.plot(x, y)
#Guardar la grafica en formato png
pl.savefig('temp1.png')

