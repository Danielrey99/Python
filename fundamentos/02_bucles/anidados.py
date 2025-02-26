"""
Este módulo muestra ejemplos básicos de bucles anidados en Python.
"""

# Bucle for anidado
print("\n-- BUCLE FOR ANIDADO --\n")
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matriz:")

for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        print(f"Fila {fila}, Columna {columna}: {matriz[fila][columna]}")

# Bucle for anidado con enumerate
print("\n-- BUCLE FOR ANIDADO CON ENUMERATE --\n")
for fila_indice, fila in enumerate(matriz):
    for columna_indice, elemento in enumerate(fila):
        print(f"Fila {fila_indice}, Columna {columna_indice}: {elemento}")
