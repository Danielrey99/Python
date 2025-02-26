"""
Este módulo muestra ejemplos básicos de bucles for en Python.
"""

#Variables
lista_numeros = [1, 2, 3, 4, 5]

#For
print("\n-- FOR RANGE --\n")
for x in range(10):
    print(x)

print("\n-- FOR SPECIFIC RANGE --\n")
for y in range(5, 10):
    print(y)

#For con else
print("\n-- FOR CON ELSE --\n")
buscar = 4
for i in lista_numeros:
    print(i)
    if i == buscar:
        print("Número encontrado:", i)
        break
else:
    print("Número no encontrado")

#Iterar lista
print("\n-- ITERAR LISTA --\n")
print("\n-- FOR LISTA --\n")
for numero in lista_numeros:
    print(f"Numero: {numero}, Posición: {lista_numeros.index(numero)}")

#Iterar string
print("\n-- ITERAR STRING --\n")
mensaje = "Hola Mundo"
for letra in mensaje:
    print(letra)
