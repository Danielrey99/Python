"""
Este módulo muestra ejemplos de funciones en Python.
"""

import asyncio

print("\n-- FUNCIONES --\n")
def hola_mundo():
    print("Hola Mundo")

hola_mundo()

def saludo(nombre, apellido):
    print(f"Hola {nombre} {apellido}")

saludo("Daniel", "Rey")

# Return
def suma(numero1, numero2):
    return numero1 + numero2

print(suma(5,5))

# Funcion con parámetro opcional
def saludo_personalizado(nombre, mensaje="Hola"):
    print(f"{mensaje}, {nombre}!")

saludo_personalizado("Juan")
saludo_personalizado("Ana", "Buenos días")

# Funcion con argumento nombrado
saludo_personalizado(mensaje="Buenos dias ", nombre="Fernando")

# Xargs
def resta (*numeros):
    resultado = 0
    for numero in numeros:
        resultado -= numero
    print(resultado)

resta(50, 25 ,10 ,5)

#KWargs
def get_products(**datos):
    print(datos)
    print(f"ID: {datos["id"]} | NAME: {datos["name"]} PRICE: {datos["price"]}")

get_products(id="1", name="Samsung", price="200")

# Funciones lambda
print("\n-- FUNCIONES LAMBDA --\n")
multiplicar = lambda x, y: x*y
print(multiplicar(5,5))

# Funciones recursivas
print("\n-- FUNCIONES RECURSIVAS --\n")
def factorial(n):
    if n ==1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5)) #120

# Funciones generadoras
print("\n-- FUNCIONES GENERADORAS --\n")
def generar_numeros():
    yield 1
    yield 2
    yield 3

for numero in generar_numeros():
    print(numero)

# Funciones de orden superior
print("\n-- FUNCIONES DE ORDEN SUPERIOR --\n")
def aplicar_funcion(func, valor):
    return func(valor)

resultado = aplicar_funcion(lambda x: x * 2, 5)
print(resultado)  # Salida: 10

# Funciones decoradoras
print("\n-- FUNCIONES DECORADORAS --\n")
def decorador(func):
    def wrapper():
        print("Antes de la función")
        func()
        print("Después de la función")
    return wrapper

@decorador
def saludar():
    print("Hola")

saludar()

# Funciones asíncronas
print("\n-- FUNCIONES ASINCRONAS --\n")
async def tarea_asincrona():
    print("Iniciando la tarea...")
    await asyncio.sleep(2)
    print("Tarea completada")

async def print_asincrona():
    print("Lanzando la tarea asíncrona")
    await tarea_asincrona()
    print("Fin del programa")

asyncio.run(print_asincrona())

# Map
print("\n-- MAP --\n")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def cuadrado(x):
    return x ** 2

resultados = map(cuadrado, numeros)
print(list(resultados))

# Map
print("\n-- MAP LAMBDA --\n")
resultados = map(lambda x: x ** 2, numeros)

print(list(resultados))

# Filter
def es_par(x):
    return x % 2 == 0

resultados = filter(es_par, numeros)
print(list(resultados))  # 2, 4, 6, 8, 10

# Filter lambda
resultados = filter(lambda x: x % 2 == 0, numeros)
print(list(resultados))  # 2, 4, 6, 8, 10
