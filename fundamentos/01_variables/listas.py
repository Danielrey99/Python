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
print(f"Lista desempaquetada: {uno} {dos} {tres} {cuatro} {cinco}")

primero, *otros, ultimo = lista_numeros
print(f"Lista desempaquetada solo primero y ultimio: {primero} {ultimo}")

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


# Sets (colección desordenada de elementos únicos)
print("\n-- SETS --\n")
# Set con llaves
mi_set = {1, 2, 3, 4, 5}
print("Set con llaves:", mi_set)

# Set con la función set()
otro_set = set([4, 5, 6, 7])
print("Set con set():", otro_set)

# Un set no permite duplicados
set_con_duplicados = {1, 2, 2, 3, 4, 4, 5}
print("Set sin duplicados:", set_con_duplicados)

# Agregar elementos
mi_set.add(6)
print("Set después de agregar 6:", mi_set)

# Eliminar elementos
mi_set.remove(3)
print("Set después de eliminar 3:", mi_set)

# Intentar eliminar un elemento que no existe genera un error
# mi_set.remove(8)  # Descomentar para ver el error

# Eliminar un elemento sin error si no existe
mi_set.discard(8)
print("Set después de discard(8):", mi_set)

# Unión: elementos en ambos sets
union = mi_set.union(otro_set)
print("Unión:", union)

# Intersección: elementos comunes en ambos sets
interseccion = mi_set.intersection(otro_set)
print("Intersección:", interseccion)

# Diferencia: elementos en el primer set pero no en el segundo
diferencia = mi_set.difference(otro_set)
print("Diferencia:", diferencia)

# Diferencia simétrica: elementos que están en un set u otro, pero no en ambos
diferencia_simetrica = mi_set.symmetric_difference(otro_set)
print("Diferencia simétrica:", diferencia_simetrica)

# Verificar si un elemento está en un set
print("¿Está 4 en mi_set?", 4 in mi_set)
print("¿Está 8 en mi_set?", 8 in mi_set)

# Iterar un set
print("Iteración sobre mi_set:")
for elemento in mi_set:
    print(elemento)

# Un frozenset es un set inmutable, lo que significa que no puedes modificarlo después de crearlo.
frozenset_ejemplo = frozenset([1, 2, 3])
print("Frozenset:", frozenset_ejemplo)

# Intentar agregar o eliminar elementos de un frozenset genera un error
# frozenset_ejemplo.add(4)  # Descomentar para ver el error

# Conjuntos como subconjuntos y superconjuntos
setA = {1, 2, 3, 4, 5}
setB = {1, 2, 3}
setC = {6, 7, 8}

print(f"¿SetB es un subconjunto de setA? {setB.issubset(setA)}")
print(f"¿SetA es un superconjunto de setB? {setA.issuperset(setB)}")
print(f"¿setC y setA son conjuntos disjuntos? {setC.isdisjoint(setA)}")
