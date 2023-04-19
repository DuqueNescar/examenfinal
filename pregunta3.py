import time

def tiempo_de_ejecucion(funcion):
    def decorador(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(f"La función {funcion.__name__} tardó {fin - inicio} segundos en ejecutarse.")
        return resultado
    return decorador

@tiempo_de_ejecucion
def multiplicacion(a, b, c, d):
    return a * b * c * d


resultado = multiplicacion(2, 3, 4, 5)
print('El resultado es',resultado)

@tiempo_de_ejecucion
def suma(a, b, c, d):
    return a + b + c + d

resultado = suma(2, 3, 4, 5)
print('El resultado es',resultado)

@tiempo_de_ejecucion
def resta(a, b, c, d):
    return a - b- c - d
resultado = resta(2, 3, 4, 5)
print('El resultado es',resultado)
