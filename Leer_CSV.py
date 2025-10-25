
import csv

temperatura = []
presion = []
humedad = []
densidad = []

with open('C:\\Users\\lunag\\Downloads\\Variables.csv' , 'r') as csvfile:
#El with es un manejador de contexto. mientras estoy dentro del with se trabaja con el archivo y si sale se cierra el archivo automaticamente.
    lector = csv.reader(csvfile, delimiter =';')   #Se usa el método reader
    encabezado =next(lector)
    
    print(encabezado[0])
    for fila in lector:    #con el for se itera sobre el obrejto para leer
        dato = int(fila[0])
        temperatura.append (dato)
        print(temperatura)


        print(encabezado[1])
        dato1 = int(fila[1])
        presion.append (dato1)
        print(presion)


        print(encabezado[2])
        dato2 = fila[2]     #Hay un problema que no se puede cambiar de str a float porque en el excel esta escrito con comas y los float en excel es con puntos asi que hay que cambiar la coma por un punto.
        dato2 = float(dato2.replace(',' , '.'))
        humedad.append(dato2)
        print(humedad)

        print(encabezado[3])
        dato3 = fila[3]     #Hay un problema que no se puede cambiar de str a float porque en el excel esta escrito con comas y los float en excel es con puntos asi que hay que cambiar la coma por un punto.
        dato3 = float(dato3.replace(',' , '.'))
        densidad.append(dato3)
        print(densidad)

print ("hola")
