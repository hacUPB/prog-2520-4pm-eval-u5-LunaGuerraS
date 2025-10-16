Neruda = open("C:\\Users\\lunag\\Downloads\\PoemaNeruda.txt", "r", encoding="utf-8")

#Crea una lista y cada linea es un elemento de la lista.
'''
linea = Neruda.readlines(2)
print(linea)

linea = Neruda.readline()
print(linea)

linea = Neruda.readline()
print(linea)
'''

#En python el archivo es un elemento iterable. Porque se puede recorrer como las listas o diccionarios con el bucle for.

for linea in Neruda:
    print(linea,end="") #Print por defecto despues de lo que imprime pone un enter, y como el archivo ya tiene un enter despues de esa linea entonces con ese codigo se quita la linea.
    

    print(linea[0]) #Imprime el primer carácter de cada linea. (Cada que se dice linea es parrafo.)

Neruda.close()