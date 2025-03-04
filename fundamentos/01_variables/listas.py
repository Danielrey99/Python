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
print(f"Posicion 5 {lista_numeros[5]}")
print(f"Primera posicion {lista_numeros[0]}")
print(f"Longitud lista numeros {len(lista_numeros)}")
print(f"Primeros 3 elementos {lista_numeros[:3]}")
print(f"3 ultimos elementos {lista_numeros[3:]}")
print(f"Del elemento 1 al 2 {lista_numeros[1:3]}")
print(f"Toma un elemento, salta el siguiente y así sucesivamente {lista_numeros[::2]}")
print(f"Lo mismo pero empenzando en la posicion 1 {lista_numeros[1::2]}")
print(f"Lo mismo pero seleccionando solo 2 elementos {lista_numeros[1:2:2]}")

elemento_eliminado = lista_numeros.pop()  # Elimina y retorna el último elemento (60)
# Otra forma de eliminar -> del lista_numeros[0]
print(f"Elemento eliminado con pop(): {elemento_eliminado}")
print(f"Lista de números después de pop(): {lista_numeros}")

uno, dos, tres, cuatro, cinco = lista_numeros
print("Lista desempaquetada: " + uno, dos, tres, cuatro, cinco)

primero, *otros, ultimo = lista_numeros
print("Lista desempaquetada solo primero y ultimio: " + primero, ultimo)

lista_desordenada = [7, 6, 3, 8, 2, 1]
print(f"Lista desordenada: {lista_desordenada}")
print(f"Lista ordenada: {lista_desordenada.sort()}")
print(f"Lista ordenada al revés: {lista_desordenada.sort(reverse=True)}")
# sorted(lista_desordenada) -> devuelve nueva lista

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
print(f"Posicion Python en la lista de strings: {lista_strings.index("Python")}")

elemento_eliminado = lista_strings.pop(1)  # Elimina y retorna el elemento en el índice 1 ("Mundo")
print(f"Elemento eliminado con pop(): {elemento_eliminado}")
print(f"Lista de strings después de pop(): {lista_strings}")

lista_strings.insert(3, "Prueba") # Inserta Prueba en la posicion 3
print(f"Lista string despues del insert: {lista_strings}")

lista_strings.remove("Prueba") # Elimina el string especifico
print(f"Lista string despues del remove: {lista_strings}")

lista_strings.clear() # Vaciar lista
print(f"Lista string despues del clear: {lista_strings}")

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

# Lista creada con range
print("\n-- LISTA CREADA CON RANGE --\n")
rango = list(range(10))
rango2 = list(range(10, 20))

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
