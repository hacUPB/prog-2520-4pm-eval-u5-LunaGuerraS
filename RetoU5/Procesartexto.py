import os

# Creo una función para leer el archivo de texto.
def lectura():

    try: #Uso try de una vez para prevenir errores.

        #Creo un with para que el archivo abra y se cierre automaticamente.
        with open("C:\\Users\\lunag\\OneDrive\\Desktop\\Trabajos Semestre 2\\Programación\\Reto U5-Archivos\\Archivo de texto.txt" , "r" , encoding="utf-8") as Texto:

            #Leo primero todo el archivo.
            contenido = Texto.read()

            #Aqui le pedi ayuda a la IA de como podia hacer que separara o leyera solo las palabras. Y me dijo que se usa el comando .split
            palabras = contenido.split()

            #Aqui ya solo uso el comando len() que ya habiamos usado antes para que me regrese el número de elementos de "palabras"
            num_palabras = len(palabras)

            #Aqui hago lo mismo pero con contenido para que incluya tambien los espacios.
            num_caracterestotal = len(contenido)

            #Aqui lo mismo pero como necesito que no tenga en cuenta los espacios uso el contenido pero remplazo los espacios por nada y asi los elimino. Fue lo que se me ocurrio.
            num_caracteres = len(contenido.replace(" ", ""))

            print(f"El archivo contiene: \n {num_palabras} palabras. \n {num_caracterestotal} caracteres totales (incluyendo los espacios). \n {num_caracteres} caracteres (sin espacios). \n")

    except FileNotFoundError:
        print("No se encontro el archivo.")

    except Exception:
        print("Ocurrió un error.")





# Creo una función para reemplazar una palabra por otra en el archivo de texto.

def reemplazar():

    try: #Uso try de una vez para prevenir errores.

        #Creo un with para que el archivo abra y se cierre automaticamente.
        with open("C:\\Users\\lunag\\OneDrive\\Desktop\\Trabajos Semestre 2\\Programación\\Reto U5-Archivos\\Archivo de texto.txt" , "r" , encoding="utf-8") as Texto:

            palabra = input("Ingrese la palabra que desea remplazar: ")
            print()
            reemplazo = input("Ingrese la palabra por la cual la quiere remplazar: ")
            
            #Leo primero todo el archivo.
            contenido = Texto.read()

            #Busco y reemplazo la palabra.
            nuevo = contenido.replace(palabra , reemplazo)

#Aquí use un ejemplo que esta en el capitulo de Archivos en notion como ejemplo. El ejemplo que tome de referencia es este:
    # Usamos 'with' para crear el contexto y escribir datos en el archivo 
    # with open(nombre_archivo, 'w') as archivo:
    #     # Solicitamos al usuario los datos a escribir en el archivo
    #     datos = input("Ingrese los datos que desea escribir en el archivo: ")
    #     archivo.write(datos)

    #Tambien vi la tabla de Notion donde esta la distinción entre usar r y usar w.

        with open("C:\\Users\\lunag\\OneDrive\\Desktop\\Trabajos Semestre 2\\Programación\\Reto U5-Archivos\\Archivo de texto.txt" , "w" , encoding="utf-8") as Texto:
            Texto.write (nuevo)

            print("La palabra se reemplazó con exito")


    except FileNotFoundError:
        print("No se encontro el archivo.")

    except Exception:
        print("Ocurrió un error.")






# Creo una función para crear un histograma(grafica de barras) del archivo de texto.

#Como es grafica me toca importar: 
import matplotlib.pyplot as plt
import numpy as np

def Histograma ():
    try:
        with open("C:\\Users\\lunag\\OneDrive\\Desktop\\Trabajos Semestre 2\\Programación\\Reto U5-Archivos\\Archivo de texto.txt" , "r" , encoding="utf-8") as Texto:

#Aqui le pregunte a la IA si existia un comando que permita contar las veces que aparece un caracter (letra) en un archivo de texto.
#"Sí, se puede usar el método .count() para un archivo de texto en Python,
# pero debe leerse primero el contenido del archivo y guardarlo en una variable de tipo cadena, ya que .count() funciona sobre cadenas de texto.
# Una vez que tenga la cadena, puede usar cadena.count(caracter) para obtener el número de veces que aparece el carácter."

            contenido = Texto.read()

            #Aqui cuento cuantas veces aparece cada vocal.
            A = contenido.count("a")
            E = contenido.count ("e")
            I = contenido.count("i")
            O = contenido.count("o")
            U = contenido.count("u")

            #La grafica se crea con una lista entonces todo el contedo de las vocales lo meto en una sola lista.
            vocales = [A, E, I, O, U]

            #Ahora se tiene que hacer el grafico; esto lo copie, peque y adapte de la parte de histograma de Notion.
            #Crear el histograma.
            plt.hist(vocales, bins=5, edgecolor='purple')

            # Agregar título y etiquetas
            plt.title('Histograma.')
            plt.xlabel('Vocales.')
            plt.ylabel('Apariciones.')

            # Mostrar la gráfica
            plt.show()

    except FileNotFoundError:
        print("No se encontro el archivo.")