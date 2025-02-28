"""
Este módulo muestra un ejemplo básico del uso match case.
"""

print("-- MATCH CASE --")

print("\n1. Contar palabras")
print("2. Contar carácteres")
print("3. Reemplazar carácter\n")

opcion = input("Ingrese una opción: ")

match opcion:
    case "1":
        texto = input("Ingrese el texto a procesar: ")
        print("\n")

        palabras = texto.split()
        print(f"El texto tiene {len(palabras)} palabras.")
    case "2":
        texto = input("Ingrese el texto a procesar: ")
        print("\n")

        print(f"El texto tiene {len(texto)} caracteres.")
    case "3":
        texto = input("Ingrese el texto a procesar: ")
        print("\n")

        caracter_viejo = input("Ingrese el carácter a reemplazar: ")
        caracter_nuevo = input("Ingrese el carácter nuevo: ")
        texto_reemplazado = texto.replace(caracter_viejo, caracter_nuevo)
        print(f"Texto con reemplazo: {texto_reemplazado}")
    case _:
        print("Opción inválida. Por favor, seleccione 1, 2 o 3.")
