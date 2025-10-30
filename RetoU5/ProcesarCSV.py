import csv

def primerasfilas():
    try: #Uso try de una vez para prevenir errores.

        #Creo un with para que el archivo abra y se cierre automaticamente.
        with open("C:\\Users\\lunag\\OneDrive\\Desktop\\Trabajos Semestre 2\\Programación\\Reto U5-Archivos\\salida_mensual_pasajeros_aeropuerto_destino_internacional.csv" , "r") as CSV:
            
            #Tomado del codigo de ejemplo realizado en clase.
            lector = csv.reader(CSV, delimiter =',') #Se usa el método reader y se pone como delimitador la coma.
            encabezado =next(lector)

            #Leer el encabezado y las primeras 15 lineas
            print(encabezado[0])
            for i, fila in enumerate(lector):
                if i < 15:
                    print(fila)


    except FileNotFoundError:
        print("No se encontro el archivo.")

    except Exception:
        print("Ocurrió un error.")

    
