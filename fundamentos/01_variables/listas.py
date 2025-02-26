"""
Este módulo muestra ejemplos básicos de listas en Python.
"""

#Lista numeros
print("\n-- LISTA NUMEROS --\n")
lista_numeros = [10, 20, 30, 40, 50]
lista_numeros.append(60)

print(lista_numeros)
print(lista_numeros[0:3])
print("Ultima posicion " + str(lista_numeros[-1]))
print(f"Ultima posicion {lista_numeros[5]}")
print(f"Primera posicion {lista_numeros[0]}")
print(f"Longitud lista numeros {len(lista_numeros)}")

elemento_eliminado = lista_numeros.pop()  # Elimina y retorna el último elemento (60)
print(f"Elemento eliminado con pop(): {elemento_eliminado}")
print(f"Lista de números después de pop(): {lista_numeros}")

#Lista strings
print("\n-- LISTA STRINGS --\n")
lista_strings = ["Hola", "Mundo", "Python"]
lista_strings.append("Fundamentos")

print(lista_strings)
print(lista_strings[0])
print("Ultima posicion " + lista_strings[-1])
print("Ultima posicion " + lista_strings[3])
print("Primera posicion " + lista_strings[0])
print(f"Longitud lista_strings {len(lista_strings)}")

elemento_eliminado = lista_strings.pop(1)  # Elimina y retorna el elemento en el índice 1 ("Mundo")
print(f"Elemento eliminado con pop(): {elemento_eliminado}")
print(f"Lista de strings después de pop(): {lista_strings}")

#Lista heterogénea
print("\n-- LISTA HETEROGENEA --\n")
lista_python = [1, "Hola", 3.14, True]
lista_python.append(50)

print("Ultima posicion " + str(lista_python[-1]))
print("Ultima posicion " + str(lista_python[4]))
print("Primera posicion " + str(lista_python[0]))
print(f"Longitud lista_python {len(lista_python)}")

elemento_eliminado = lista_python.pop(2)  # Elimina y retorna el elemento en el índice 2 (3.14)
print(f"Elemento eliminado con pop(): {elemento_eliminado}")
print(f"Lista heterogénea después de pop(): {lista_python}")

# Tuplas (inmutables)
print("\n-- TUPLAS --\n")
tupla_ejemplo = (10, "Python", 3.14, False)  # Los paréntesis son opcionales pero recomendados

print(tupla_ejemplo)
print(f"Primeros dos elementos: {tupla_ejemplo[0:2]}")
print(f"Último elemento: {tupla_ejemplo[-1]}")
print(f"Primer elemento: {tupla_ejemplo[0]}")
print(f"Longitud tupla: {len(tupla_ejemplo)}")

# Listas 2D
print("\n-- LISTAS 2D --\n")
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[0][0])   # 1 (fila 0, columna 0)
print(matriz[1][2])   # 6 (fila 1, columna 2)
print(matriz[-1][-1]) # 9 (última fila, última columna)
