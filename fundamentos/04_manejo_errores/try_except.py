"""
Este módulo muestra ejemplos básicos de manejo de errores en Python.
"""

print("\n-- TRY EXCEPT --\n")
try:
    resultado = 10 / 0
except ZeroDivisionError:  # Captura la excepción si ocurre una división por cero.
    print("Error: No se puede dividir por cero.")  # Mensaje de error.

print("\n-- MULTIPLES EXCEPCIONES --\n")
try:
    print("Division")
    numero1 = int(input("Ingresa dividendo: "))
    numero2 = int(input("Ingresa divisor: "))
    print(f"Resultado: {numero1 / numero2}")
except ValueError:  # Captura la excepción si no se puede convertir a entero.
    print("Error: No se puede convertir a entero.")
except ZeroDivisionError:  # Captura la excepción si el divisor es cero.
    print("Error: No se puede dividir por cero.")

print("\n-- EXCEPCION GENERICA --\n")
try:
    resultado = 10 / 0
except Exception as e:  # Captura cualquier excepción que ocurra.
    print(f"Ocurrió un error: {e}")  # Muestra el mensaje de la excepción.

print("\n-- EXCEPCION CON ELSE --\n")
try:
    resultado = 10 / 2
except ZeroDivisionError:  # Captura la excepción si ocurre una división por cero.
    print("Error: No se puede dividir por cero.")
else:  # Se ejecuta si no ocurre ninguna excepción.
    print(f"El resultado es: {resultado}")

print("\n-- FINALLY --\n")
try:
    resultado = 10 / 0
except ZeroDivisionError:  # Captura la excepción si ocurre una división por cero.
    print("Error: No se puede dividir por cero.")
finally:  # Este bloque siempre se ejecuta, haya o no excepción.
    print("Este bloque siempre se ejecuta.")

print("\n-- RAISE --\n")
def dividir(a, b):
    if b == 0:  # Verifica si el divisor es cero.
        raise ValueError("El divisor no puede ser cero.")  # Lanza una excepción.
    return a / b  # Retorna el resultado de la división.

try:
    resultado = dividir(10, 0)
except ValueError as e:  # Captura la excepción lanzada por raise.
    print(e)  # Muestra el mensaje de la excepción.

print("\n-- EXCEPCION PERSONALIZADA --\n")
class MiErrorPersonalizado(Exception):  # Define una excepción personalizada.
    pass

def verificar_valor(valor):
    if valor < 0:  # Verifica si el valor es negativo.
        raise MiErrorPersonalizado("El valor no puede ser negativo.")  # Lanza la excepción.

try:
    verificar_valor(-5)
except MiErrorPersonalizado as e:  # Captura la excepción personalizada.
    print(e)  # Muestra el mensaje de la excepción.

print("\n-- EXCEPCION ANIDADA --\n")
try:
    try:
        resultado = 10 / 0
    except ZeroDivisionError:  # Captura la excepción si ocurre una división por cero.
        print("Error interno: División por cero.")  # Mensaje de error interno.
    resultado = int("no es un número")  # Intenta convertir una cadena no válida a entero.
except ValueError:  # Captura la excepción si no se puede convertir a entero.
    print("Error externo: No se puede convertir a entero.")  # Mensaje de error externo.

print("\n-- ASSERT --\n")
def dividir2(a, b):
    assert b != 0, "El divisor no puede ser cero."  # Verifica que el divisor no sea cero.
    return a / b  # Retorna el resultado de la división.

try:
    resultado = dividir2(10, 0)
except AssertionError as e:  # Captura la excepción si la condición de assert es falsa.
    print(e)  # Muestra el mensaje de la excepción.

print("\n-- WITH --\n")
try:
    with open("archivo_inexistente.txt", "r") as archivo:  # Intenta abrir un archivo.
        contenido = archivo.read()  # Lee el contenido del archivo.
except FileNotFoundError:  # Captura la excepción si el archivo no existe.
    print("Error: El archivo no existe.")  # Mensaje de error.
