# Aquí se presenta el analisis del Reto 5.

## Se explicarán los conceptos más importantes, como se extructuró el programa y los comandos más relevantes:

## 1. Estructura del Programa.

El programa se estructuró en base a un menu prncipal y luego 3 archivos que contienen las funciones respectivas a casa inciso del menu:

- **MenuPrincipal.py**: Contiene el menú principal y los submenús.
- **ListarArchivos.py**: Responde a la primera función del menu.
- **ProcesarTexto.py**: Responde a la segunda función del menu principal sobre procesar archivos de texto.
- **ProcesarCSV.py**: Responde a la tercera y última función del menu proncipal sobre procesar archivos CSV.

## 2. Conceptos Principales Implementados.

#### Archivos de Texto
- Se uso el comando `open()` para manejarlo más facil y evitar tener que estar abriendo y cerrando el archivo en cada función.
- Se uso el modo de apertura `'r'` para lectura y `'w'` para escritura dependiendo de la necesidad.
- Comandos vistos en clase como `read()`, `replace()`
- Hubo investigación propia, en busca de una manera más agil de hacer las cosas se descrubrieon comandos nuevos como `split()`, `count` asi como la función de estadistica para tener de forma automatica la mediana y la disperción.

#### Archivos CSV
- Uso del módulo `csv` con `csv.reader()` como se vio en clase.
- Se uso la especificación de delimitador, aunque por defecto sea la coma(,) se quizo usarlo para evitar confusión del programa o una falla por causa de delimitadores.
- Hubo lectura por aparte de encabezados e incluir datos en una lista para graficar.

#### Matplotlib
- Gráficas de dispersión usando `plt.scatter()` basandose en los ejemplos proporcionados en Notion.
- Histogramas para determinar la frecuencia de vocales.
- Personalización de gráficas:
  - Títulos
  - Etiquetas de ejes.
  - Colores y marcadores.
  - Tamaños y estilo de puntos.

### Manejo de Errores

Se uso con bastante frecuencia el `try-except` para asegurar que el codigo siguiera ejecutandoce en todo momento sin importar si se llega a presentar una falla porque al ser un codigo bastante largo es mejor manejar fallas como:
- `FileNotFoundError`: Archivos no encontrados.
- `ValueError`: Entradas inválidas.
- Excepciones generales.
