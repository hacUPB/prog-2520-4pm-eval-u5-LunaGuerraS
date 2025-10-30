import csv
import math
import statistics #Busque si habia comandos para poder sacar medidas de tendencia central y me salio que era con este, no con el de matematica.
import matplotlib.pyplot as plt
import numpy as np

# Creo una función para leer las primeras 15 lineas.
def primerasfilas():
    try: #Uso try de una vez para prevenir errores.

        #Creo un with para que el archivo abra y se cierre automaticamente.
        with open("C:\\Users\\lunag\\OneDrive\\Desktop\\Trabajos Semestre 2\\Programación\\Reto U5-Archivos\\salida_mensual_pasajeros_aeropuerto_destino_internacional.csv" , "r" , encoding="utf-8") as CSV:
            
            #Tomado del codigo de ejemplo realizado en clase.
            lector = csv.reader(CSV, delimiter =',') #Se usa el método reader y se pone como delimitador la coma.
            encabezado =next(lector)

            #Leer el encabezado y las primeras 15 lineas
            print(encabezado)
            for i, fila in (lector):   #Se inicia un bucle para recorrer el resto de las líneas del archivo.
                if i <= 15:
                    print(fila)
                else:
                    break

    except FileNotFoundError:
        print("No se encontro el archivo.")

    except Exception:
        print("Ocurrió un error.")




# Creo una función para calcular estadisticas.
def estadistica():
    try:
        with open("C:\\Users\\lunag\\OneDrive\\Desktop\\Trabajos Semestre 2\\Programación\\Reto U5-Archivos\\salida_mensual_pasajeros_aeropuerto_destino_internacional.csv" , "r" , encoding="utf-8") as CSV:
            columna = int(input("Escriba el numero de la columna que desea analizar: "))
            columna = columna - 1
#Esto porque como python lo cuenta desde 0 pero normalmente nosotros no lo contamos desde 0 sino desde 1

            #Para que no pase un error si se llega a poner un numero negativo.
            if columna < 0:
                print("Por favor ingresa un número valido.")

            #Se lee y se pasa el encabezado.
            lector = csv.reader(CSV, delimiter =',')
            encabezado = next(lector)

            #Hago una lista vacia para meter los datos de la columna que se escogió.
            datos_columna = []

#Apartir de acá pedi ayuda de la IA porque no entendia como hacer que leyera la columna y no la fila y en Notion no encontre ejemplo de eso asi que no tuve idea de como hacerlo.
            for fila in lector: #Para que pase por todas las filas del archivo.
                if columna < len(fila):
                #Verifica si la columna deseada existe en esa fila.
                
                    valor = fila[columna].strip() #Aca se selecciona de cada fila solo el elemento correspondiente a la columna que se seleccionó.
                
                #Para eliminar a los espacios y las comillas.
                    valor = valor.replace('"','').replace(' ', '')

                    if valor == '':
                        continue

                numeros = float(valor)
                datos_columna.append(numeros)

            if not datos_columna:
                print("No se encontraron datos numéricos en la columna seleccionada.")


#Ahora se hacen todos los analisis. Estos si los hice yo, Busque en google que comando se usaba para cada operación matematica.
            numero_datos = len(datos_columna)
            promedio = sum(datos_columna)/ numero_datos
            mediana = statistics.median (datos_columna)
            desviacion = statistics.pstdev(datos_columna)
            minimo = min(datos_columna)
            maximo = max(datos_columna)

            print(f"El analisis de la comumna {columna} es:")
            print(f"Numero de datos: {numero_datos} \n Promedio: {promedio} \n Mediana: {mediana} \n Desviación estandar: {desviacion} \n Minimo: {minimo} \n Maximo: {maximo}")


    except FileNotFoundError:
        print("No se encontro el archivo.")
    except ValueError:
        print("Por favor, ingrese un número de columna válido.")
    except Exception:
        print("Ocurrió un error")






def Grafica_Columna():
    try:
        with open("C:\\Users\\lunag\\OneDrive\\Desktop\\Trabajos Semestre 2\\Programación\\Reto U5-Archivos\\salida_mensual_pasajeros_aeropuerto_destino_internacional.csv" , "r" , encoding="utf-8") as CSV:
            columna = int(input("Escriba el numero de la columna que desea graficar: "))
            columna = columna - 1

            #Para que no pase un error si se llega a poner un numero negativo.
            if columna < 0:
                print("Por favor ingresa un número valido.")

            lector = csv.reader(CSV, delimiter =',')
            encabezado = next(lector)

            #Hago una lista vacia para meter los datos de la columna que se escogió.
            datos_columna = []

            #Usé la misma logica que el ejercicio anterior.
            for fila in lector: #Para que pase por tdas las filas del archivo.
                    if columna < len(fila):
                        valor = fila[columna].strip() #Aca se selecciona de cada fila solo el elemento correspondiente a la columna que se seleccionó.
                    #Para eliminar a los espacios y las comillas.
                        valor = valor.replace('"','').replace(' ', '')

                        if valor == '':
                            continue

                    try:
                        numero = float(valor)
                        
                    except ValueError:
                        continue
                    datos_columna.append(numero)

                    if not datos_columna:
                        print("No se encontraron datos numéricos en la columna seleccionada.")

            #Tomado del ejemplo de grafica de dispersión de Notion.
            # Crear la gráfica de dispersión
            x = list(range(1, len(datos_columna) + 1))
            plt.scatter(x, datos_columna, s=50, c='#8C00FF', marker='+')

            # Agregar título y etiquetas
            plt.title('Gráfica de Dispersión')
            plt.xlabel('Indicie (fila)')
            plt.ylabel('Valor')

            # Mostrar la gráfica
            plt.show()


    except FileNotFoundError:
        print("No se encontro el archivo.")
    except ValueError:
        print("Por favor, ingrese un número de columna válido.")
    except Exception as o:
        print(f"Ocurrió un error de tipo {o}")