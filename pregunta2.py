import random
import math

# Función para crear el archivo y dividirlo en dos
def crear_archivo():
    # Crear archivo principal
    archivo_principal = open("notas.txt", "w")
    archivo_principal.close()

    # Crear archivo de funciones
    archivo_funciones = open("funciones.py", "a+")
    archivo_funciones.write("# Archivo de funciones\n")
    archivo_funciones.close()

# Función para llenar la lista de manera aleatoria y escribirla en el archivo principal
def llenar_lista(tamano):
    # Crear lista de números aleatorios
    lista_numeros = [random.randint(0, 100) for i in range(tamano)]

    # Escribir la lista en el archivo principal
    archivo_principal = open("notas.txt", "a")
    archivo_principal.write("Lista de números aleatorios:\n")
    archivo_principal.write(str(lista_numeros) + "\n")
    archivo_principal.close()

# Función para calcular la raíz cuadrada de los números y escribirlos en el archivo principal
def calcular_raices():
    # Leer la lista de números del archivo principal
    archivo_principal = open("notas.txt", "r")
    lineas = archivo_principal.readlines()
    archivo_principal.close()

    # Obtener la lista de números
    lista_numeros = eval(lineas[1])

    # Calcular las raíces cuadradas
    lista_raices = [math.sqrt(num) for num in lista_numeros]

    # Escribir las raíces cuadradas en el archivo principal
    archivo_principal = open("notas.txt", "a")
    archivo_principal.write("Raíces cuadradas de los números:\n")
    archivo_principal.write(str(lista_raices) + "\n")
    archivo_principal.close()

# Crear el archivo y dividirlo en dos
crear_archivo()

# Pedir al usuario el tamaño de la lista
tamano_lista = int(input("Ingrese el tamaño de la lista: "))

# Llenar la lista de manera aleatoria y escribirla en el archivo principal
llenar_lista(tamano_lista)

# Calcular las raíces cuadradas y escribirlas en el archivo principal
calcular_raices()
