#1. Abrir archivo.
Texto = open("C:\\Users\\lunag\\Downloads\\texto_aleaorio.txt","r", encoding="utf-8")

#2. Leer el archivo.

datos = Texto.read() #Para que lo lea todo.

#datos = Texto.read(200) #Para que lea solo 200 carácteres.

#3. Leer solo una "linea", en realidad un parrafo porque es hasta un enter.
parrafo = Texto.readline()

#4. Se hace la operación de lectura solo para que se mueva el cursor para poder leer una palabra en una posicion en espesifica por ende no es necesario recuperrarlo.
Texto.readline()
Texto.read(5)
otro = Texto.readline(7)

#5. Cerrar el archivo.
Texto.close()

#6. Se imprime lo que se leyó del archivo.
print(datos)