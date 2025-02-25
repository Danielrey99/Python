"""
Este módulo muestra ejemplos básicos de variables y listas en Python.
"""

print("Hola Mundo "  * 2)

#Variables
number = 25
text = "Hola Mundo"
decimal = 1.75
flag = True

print("\n-- VARIABLES --\n")
print(f"number: {str(number)} type: {type(number)}")
print(f"text: {text} type: {type(text)}")
print(f"Decimal: {str(decimal)} type: {type(decimal)}")
print(f"Flag: {str(flag)} type: {type(flag)}")

# Conversión de tipos
print("\n-- CONVERSIÓN DE TIPOS --\n")
edad_str = str(number)
altura_int = int(decimal)
print("Edad como cadena:", edad_str)
print("Altura como entero:", altura_int)

#Operadores asignación
print("\n-- OPERADORES DE ASIGNACIÓN --\n")
number += 1
print("Edad después de incrementar:", number)
number -= 1
print("Edad después de decrementar:", number)
number *= 2
print("Edad después de multiplicar:", number)
number /= 2
print("Edad después de dividir:", number)

#Variables múltiples
print("\n-- VARIABLES MÚLTIPLES --\n")
nombre, apellido, edad = "Juan", "Pérez", 30
print(nombre)  # Juan
print(apellido)  # Pérez
print(edad)  # 30

# Método split()
print("\n-- MÉTODO SPLIT() --\n")
mensaje = "Este es un mensaje con varias palabras."
palabras = mensaje.split()
print(palabras)

frutas = "manzana,pera,naranja"
lista_frutas = frutas.split(",")
print(lista_frutas)

#Slicing
print("\n-- SLICING --\n")
mensaje = "Hola Mundo"
print("Primera palabra " + mensaje[0:4])  # "Hola"
print("Ultima palabra " + mensaje[5:10])  # "Mundo"
print("Primera palabra " + mensaje[:4])  # "Hola"
print("Ultima palabra " + mensaje[5:])  # "Mundo"
print("Primerla letra " + mensaje[0])  # "H"
print("Ultima letra " + mensaje[-1])  # "o"
