"""
Este módulo muestra ejemplos básicos de bucles if en Python.
"""

#Variables
age = 10
text = "Hola Mundo"
flag = True
lista_strings = ["Hola", "Mundo", "Python"]

#If
print("\n-- IF --\n")
if flag:
    print(text + str(age))

#If Else
print("\n-- IF ELSE --\n")
if age > 17:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

#If ternario
print("\n-- IF TERNARIO --\n")
result = "Es mayor de edad" if age >= 18 else "Es menor de edad"
print(result)

#Else If
print("\n-- ELSE IF --\n")
if age == 10:
    print("La edad es 10")
elif age == 20:
    print("La edad es 20")
else:
    print("ELa edad es no es 10 ni 20")

#Operadores lógicos
print("\n-- OPERADORES LÓGICOS --\n")
if age > 0 and age < 100:
    print("La edad es correcta")
else:
    print("La edad no es correcta")

if age < 0 or age > 100:
    print("La edad es incorrecta")
else:
    print("La edad es correcta")

if age != 10:
    print("La edad no es 10")
else:
    print("La edad es 10")

if age >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

if 18 <= age < 65:
    print("Es adulto")

if age == 10 or not flag:
    print("La edad es 10 o flag es False")

if age == 10 and (flag or age > 0):
    print("La edad es 10 y flag es True o la edad es mayor a 0")

#Operador de pertenencia
exists = "o" in text
not_exist = "x" in text
print(f"exists o: {exists} - No exists x: {not_exist}")

# Comprobar un string en una lista
if "Python" in lista_strings:
    print(f"Posicion Python en lista: {lista_strings.index("Python")}")
else:
    print("No existe Python en la lista de string")
