# Función para lsitar archivos.

import os

def listar_archivos ():
    # #Aqui se usó la IA para que me explicara como listar un archivo y me dio la siguiente función:
    # "Para listar un archivo en Python, usa la función os.listdir() del módulo os
    # la cual devuelve una lista con los nombres de todos los archivos y directorios en una ruta especificada."

#Aqui solo la dirección de una carpeta que creé para poner los archivos que voy a usar en el reto.
    ruta = "C:\\Users\\lunag\\OneDrive\\Desktop\\Trabajos Semestre 2\\Programación\\Reto U5-Archivos"

#Se usa la funcion que la IA me dio para que solo mostrata los archivos que estaban en esa carpeta.
    archivos = os.listdir(ruta)
    print(f"Los archivos que se van a utilizar en este reto son: \n {archivos}")
