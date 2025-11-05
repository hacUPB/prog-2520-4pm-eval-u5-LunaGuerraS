import matplotlib.pyplot as plt
import numpy as np
import math

#Grafica de Coseno.
'''
# Datos
x = []
y = []
for i in range(100):
    dato = i/100
    x.append(dato)

for j in range(len(x)):
    dato = math.cos(2*math.pi*x[j])
    y.append(dato)


# Crear la gráfica
plt.plot(x, y)

# Agregar título y etiquetas
plt.title('Gráfica de Coseno')
plt.xlabel('X')
plt.ylabel('cos(X)')

# Mostrar la gráfica
plt.show()
'''

# Grafica de puntitos
'''
x = [1, 3, 46, 23, 76, 92]
y = [3, 6, 28 ,13 ,54, 23]

plt.plot(x,y)   #Hacer la grafica

#Agregar título y etiquetas
plt.title('Grafica random')
#Mostrar la grafica
plt.show()

'''

# Datos
categorias = ['A', 'B', 'C', 'D']
valores = [35, 28, 19, 17]

# Crear la gráfica de barras con personalizacion de colores
plt.bar(categorias, valores, color=["#B7A3E3", '#FFA4A4', '#91C4C3', '#86B0BD'])

# Agregar título y etiquetas
plt.title('Gráfica de Barras')
plt.xlabel('Categorías')
plt.ylabel('Valores')

# Mostrar la gráfica
plt.show()

