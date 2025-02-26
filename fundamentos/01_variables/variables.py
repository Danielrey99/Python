"""
Este módulo muestra ejemplos básicos de variables
"""

import math

print("Hola Mundo " * 2)

# Variables
number = 25
text = "Hola Mundo"
decimal = 1.75
flag = True
long_text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Suspendisse bibendum malesuada tincidunt. 
Aenean condimentum libero eget nisl scelerisque convallis. 
Aliquam nulla nisi, gravida sed ullamcorper eget, ultrices vel odio. 
Fusce mattis lacus id nulla vestibulum, at eleifend nisi mattis. 
"""

print("\n-- VARIABLES --\n")
print(f"number: {str(number)} type: {type(number)}")
print(f"text: {text} type: {type(text)}")
print(f"Decimal: {str(decimal)} type: {type(decimal)}")
print(f"Flag: {str(flag)} type: {type(flag)}")
print(f"Long text: {long_text} type: {type(long_text)}")

# Conversión de tipos
print("\n-- CONVERSIÓN DE TIPOS --\n")
edad_str = str(number)
altura_int = int(decimal)
altura_float = float(decimal)
numero_bool = bool(0)
numero_bool2 = bool(1)
string_bool = bool("")
string_bool2 = bool("Hola")
none_bool = bool(None)
print("Edad como cadena:", edad_str)
print("Altura como entero:", altura_int)
print("Altura como flotante:", altura_float)
print("Número 0 como booleano:", numero_bool)
print("Número 1 como booleano:", numero_bool2)
print("Cadena vacía como booleano:", string_bool)
print("Cadena con texto como booleano:", string_bool2)
print("None como booleano:", none_bool)

# Metodos
print("\n-- MÉTODOS STRING --\n")
lower_text = text.lower()
upper_text = text.upper()
print("Texto en minúsculas:", lower_text)
print("Texto en mayúsculas:", upper_text)
print("Primer letra en mayúsculas:", text.capitalize())
print("Primera letra de cada palabra en mayúsculas:", text.title())
print("Contar caracteres:", text.count("o"))
print("Cantidad de caracteres:", len(text))
print("Reemplazar texto:", text.replace("Mundo", "Python"))
print("Buscar texto:", text.find("Mundo"))
print("Buscar texto:", text.find("Python"))
print("Contiene texto:", "Mundo" in text)
print("No contiene texto:", "Python" not in text)

# Secuencias de escape
print("\n-- SECUENCIAS DE ESCAPE --\n")
print("Hola\nMundo")
print("Hola\tMundo")
print("Hola\\Mundo")
print("Hola\"Mundo\"")
print("Hola\'Mundo\'")

# Operadores asignación
print("\n-- OPERADORES DE ASIGNACIÓN --\n")
number += 1
print("Edad después de incrementar:", number)
number -= 1
print("Edad después de decrementar:", number)
number *= 2
print("Edad después de multiplicar:", number)
number /= 2
print("Edad después de dividir:", number)

# Variables múltiples
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

# Slicing
print("\n-- SLICING --\n")
mensaje = "Hola Mundo"
print("Primera palabra " + mensaje[0:4])  # "Hola"
print("Ultima palabra " + mensaje[5:10])  # "Mundo"
print("Primera palabra " + mensaje[:4])  # "Hola"
print("Ultima palabra " + mensaje[5:])  # "Mundo"
print("Primerla letra " + mensaje[0])  # "H"
print("Ultima letra " + mensaje[-1])  # "o"

# Numeros
print("\n-- NÚMEROS --\n")

print("Suma:", 5 + 3) # 8
print("Resta:", 5 - 3) # 2
print("Multiplicación:", 5 * 3) # 15
print("División:", 5 / 3) # 1.6666666666666667
print("División entera:", 5 // 3) # 1
print("Módulo:", 5 % 3) # 2
print("Potencia:", 5 ** 3) # 125

numero_imaginaio = 2 + 3j # 2 + 3i (raiz cuadrada de -1)
print("Número imaginario:", numero_imaginaio)

# Funciones numeros
print("\n-- FUNCIONES NÚMEROS --\n")
print("Valor absoluto:", abs(-5)) # 5
print("Redondeo:", round(5.4)) # 5
print("Redondeo:", round(5.5)) # 6
print("Redondeo:", round(5.6)) # 6

print("\n-- FUNCIONES MATH --\n")
print("Máximo:", max(5, 3, 8)) # 8
print("Mínimo:", min(5, 3, 8)) # 3

print("Cercano a entero más grande:", math.ceil(5.3)) # 6
print("Cercano a entero más pequeño:", math.floor(5.3)) # 5

print("Es un numero: ", math.isnan(5)) # False
print("Es un numero: ", math.isnan(float('nan'))) # True

print("Suma:", sum([5, 3, 8])) # 16
print("Raíz cuadrada:", math.sqrt(25)) # 5.0
print("Potencia:", math.pow(5, 3)) # 125.0
print("Exponencial:", math.exp(5)) # 148.4131591025766
print("Factorial:", math.factorial(5)) # 120

print("Valor absoluto:", math.fabs(-5)) # 5.0
print("Redondeo:", math.ceil(5.3)) # 6
print("Redondeo:", math.floor(5.3)) # 5
print("Truncar:", math.trunc(5.3)) # 5
print("Truncar:", math.trunc(-5.3)) # -5

print("Seno:", math.sin(math.radians(90))) # 1.0
print("Coseno:", math.cos(math.radians(0))) # 1.0
print("Tangente:", math.tan(math.radians(45))) # 1.0
print("Logaritmo:", math.log(100, 10)) # 2.0

print("Grados a radianes:", math.radians(180)) # 3.141592653589793
print("Radianes a grados:", math.degrees(math.pi)) # 180.0

print("Hipotenusa:", math.hypot(3, 4)) # 5.0
print("Ángulo:", math.atan2(4, 3)) # 0.9272952180016122

print("Pi:", math.pi) # 3.141592653589793
print("Euler:", math.e) # 2.718281828459045

# Comparadores
print("\n-- COMPARADORES --\n")
print("Igualdad 5=3:", 5 == 3) # False
print("Desigualdad 5!=3:", 5 != 3) # True
print("Mayor 5>3:", 5 > 3) # True
print("Menor 5<3:", 5 < 3) # False
print("Mayor o igual 5>=3:", 5 >= 3) # True
print("Menor o igual 5<=3:", 5 <= 3) # False
print("Igualdad de objetos:", "Hola" is "Hola") # True
print("Igualdad de objetos:", "Hola" is not "Hola") # False
print("Igualdad de valores:", "Hola" == "Hola") # True
print("Igualdad de numero y string:", 5 == "5") # False
print("Igualdad de numero y string:", 5 == int("5")) # True
print("Igualdad de numero y string:", 5 == float("5")) # True
print("Igualdad de booleanos:", True == 1) # True
print("Igualdad de booleanos:", False == 0) # True
