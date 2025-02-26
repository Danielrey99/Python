"""
Este módulo muestra ejemplos básicos de bucles while en Python.
"""

# While
print("\n-- WHILE --\n")
numero = 0
while numero < 10:
    print(numero)
    numero += 1

# While con exit
print("\n-- WHILE CON EXIT --\n")
texto = ""
while texto.lower() != "exit":
    texto = input("Introduce un texto: ")
    print("Has introducido: " + texto)
    print("Introduce 'exit' para salir")
print("Fin del bucle")

# While con break
print("\n-- WHILE CON BREAK --\n")
while True:
    texto = input("Introduce un texto: ")
    print("Has introducido: " + texto)
    print("Introduce 'exit' para salir")
    if texto.lower() == "exit":
        print("Fin del bucle")
        break

# While con continue
print("\n-- WHILE CON CONTINUE --\n")
numero = 0

while numero < 10:
    numero += 1
    # Si es par, salta a la siguiente iteración
    if numero % 2 == 0:
        continue
    print(f"Número impar: {numero}")
print("Fin del bucle.")

# While con else
print("\n-- WHILE CON ELSE --\n")
while numero < 10:
    numero += 1
    if numero % 2 == 0:
        print(f"Número par: {numero}")
    else:
        print(f"Número impar: {numero}")
print("Fin del bucle.")
