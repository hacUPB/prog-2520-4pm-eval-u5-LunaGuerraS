# Importar las bibliotecas.
import matplotlib.pyplot as plt
import numpy as np
import math
import os
import csv

# Puse por separado las funciones para que queda más ordenado y aqui importo las funciones.
from ListarArchivos import *
from Procesartexto import *
from ProcesarCSV import *


# Hacer el menu principal de opciiones.
def menu ():
    while True:
        print("Menú Principal. \n1. Listar archivos. \n2. Procesar archivo .txt \n3. Procesar archivo .csv \n4. Salir.")
        opcion = int(input("Seleccione una acción: "))
        match opcion:
            case 1:
                print()
                listar_archivos()
                print()

            case 2:
                print()

                #Creo el submenu para lo que se puede hacer con el archivo de texto.
                while True:
                    print("Opciones: \n1. Contar número de palabras y caracteres. \n2. Reemplazar una palabra por otra. \n3. Histograma de ocurrencia de las vocales. \n4. Volver al menu principal.")
                    accion =int(input("Por favor ingrese la acción que desea ejecutar: "))

                    match accion:
                        case 1:
                            print()
                            lectura()

                        case 2:
                            print()
                            reemplazar()
             
                        case 3:
                            print()
                            Histograma()
             
                        case 4:
                            break
             
                        case _:
                            print()
                            print("Por favor seleccionar una acción valida,")

            case 3:
                print()

                #Creo el submenu para lo que se puede hacer con el archivo CSV.
                while True:
                    print("Opciones: \n1. Mostrar las 15 primeras filas. \n2. Calcular Estadísticas. \n3. Graficar una columna completa con los datos. \n4. Volver al menu principal.")
                    accion =int(input("Por favor ingrese la acción que desea ejecutar: "))

                    match accion:
                        case 1:
                            print()
                            primerasfilas()

                        case 2:
                            print()
                            
             
                        case 3:
                            print()
                            
             
                        case 4:
                            break
             
                        case _:
                            print()
                            print("Por favor seleccionar una acción valida,")

            case 4: #Opción para salir del programa.
                print()
                print("Ha salido del menu.")
                break

            case _:
                print()
                print("SELECCIONE UNA OPCION VALIDA, INTENTE DE NUEVO.")
                

if __name__ == "__main__":
    menu()