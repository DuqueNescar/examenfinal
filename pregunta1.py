import random

def generar_valores():
    valores = []
    for i in range(10):
        valores.append(random.randint(1, 20))
    return valores

def filtrar_valores(valores):
    valores_sin_repetir = []
    valores_repetidos = []
    for valor in valores:
        if valor not in valores_repetidos:
            if valor not in valores_sin_repetir:
                valores_sin_repetir.append(valor)
            else:
                valores_sin_repetir.remove(valor)
                valores_repetidos.append(valor)
    return valores_sin_repetir

# Generamos la lista de valores aleatorios
valores = generar_valores()

# Mostramos la lista original
print("Lista original:", valores)

# Filtramos los valores repetidos
valores_sin_repetir = filtrar_valores(valores)

# Mostramos los valores sin repetir
print("Valores sin repetir:", valores_sin_repetir)


def ordenar_valores(valores):
    valores_sin_repetir = filtrar_valores(valores)
    valores_sin_repetir.sort(reverse=True)
    return valores_sin_repetir

valores_ordenados = ordenar_valores(valores)
print('De mayor a menor es: ',valores_ordenados)

def encontrar_maximo_ordenado(valores):
    valores_ordenados = ordenar_valores(valores)
    maximo = valores_ordenados[0]
    return maximo

maximo = encontrar_maximo_ordenado(valores)
print('El valor maximo es:', maximo)