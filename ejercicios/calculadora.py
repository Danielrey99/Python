"""
Crear una calculadora con distintas funcionalidades
"""

import os
import math
import collections

flag = True
operaciones_guardadas = collections.deque(maxlen=10)

print("-- CALCULADORA --")

while flag:
    print("\n1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Exponenciación")
    print("6. Raíz cuadrada")
    print("7. Logaritmo natural")
    print("8. Logaritmo personalizado")
    print("9. Seno")
    print("10. Coseno")
    print("11. Tangente")
    print("12. Conversión Decimal - Binario - Hexadecimal - Octal")
    print("13. Conversión de Longitud")
    print("14. Conversión de Area")
    print("15. Conversión de Volumen")
    print("16. Conversión de Masa")
    print("17. Conversión de Temperatura")
    print("18. Conversión de Tiempo")
    print("19. Historial de Operaciones")
    print("20. Limpiar consola")
    print("21. Salir\n")

    try:
        opcion = input("Ingrese una opción: ")
    except ValueError:
        print("Ingrese un número válido")

    match opcion:
        case "1":
            print("\n--- Sumar ---")
            print("Ingrese dos números")
            try:
                num1 = float(input("Número 1: "))
                num2 = float(input("Número 2: "))
                resultado = f"Resultado: {num1} + {num2} = {num1 + num2}"
                print(resultado)
                operaciones_guardadas.append("\n--- Sumar ---\n" + resultado + "\n")
            except ValueError:
                print("Ingrese un número válido")

        case "2":
            print("\n--- Restar ---")
            print("Ingrese dos números")
            try:
                num1 = float(input("Número 1: "))
                num2 = float(input("Número 2: "))
                resultado = f"Resultado: {num1} - {num2} = {num1 - num2}"
                print(resultado)
                operaciones_guardadas.append("\n--- Restar ---\n" + resultado + "\n")
            except ValueError:
                print("Ingrese un número válido")

        case "3":
            print("\n--- Multiplicar ---")
            print("Ingrese dos números")
            try:
                num1 = float(input("Número 1: "))
                num2 = float(input("Número 2: "))
                resultado = f"Resultado: {num1} x {num2} = {num1 * num2}"
                print(resultado)
                operaciones_guardadas.append("\n--- Multiplicar ---\n" + resultado + "\n")
            except ValueError:
                print("Ingrese un número válido")

        case "4":
            print("\n--- Dividir ---")
            print("Ingrese dos números")
            try:
                num1 = float(input("Número 1: "))
                num2 = float(input("Número 2: "))
                resultado = (
                    f"Resultado: {num1} / {num2} = {num1 / num2}\n"
                    f"Resto: {num1 % num2}\n"
                    f"Cociente: {num1 // num2}"
                )
                print(resultado)
                operaciones_guardadas.append("\n--- Dividir ---\n" + resultado + "\n")
            except ValueError:
                print("Ingrese un número válido")
            except ZeroDivisionError:
                print("No se puede dividir por cero")

        case "5":
            print("\n--- Exponenciación ---")
            print("Ingrese dos números")
            try:
                num1 = float(input("Base: "))
                num2 = float(input("Exponente: "))
                resultado = f"Resultado: {num1}^{num2} = {num1 ** num2}"
                print(resultado)
                operaciones_guardadas.append("\n--- Exponenciación ---\n" + resultado + "\n")
            except ValueError:
                print("Ingrese un número válido")

        case "6":
            print("\n--- Raíz cuadrada ---")
            try:
                num = float(input("Número: "))
                if num < 0:
                    print("No se puede calcular la raíz cuadrada de un número negativo")
                else:
                    resultado = f"Resultado: √{num} = {math.sqrt(num)}"
                    print(resultado)
                    operaciones_guardadas.append("\n--- Raíz cuadrada ---\n" + resultado + "\n")
            except ValueError:
                print("Ingrese un número válido")

        case "7":
            print("\n--- Logaritmo natural ---")
            try:
                num = float(input("Número: "))
                if num <= 0:
                    print("El número debe ser positivo")
                else:
                    resultado = f"Resultado: ln({num}) = {math.log(num)}"
                    print(resultado)
                    operaciones_guardadas.append("\n--- Logaritmo natural ---\n" + resultado + "\n")
            except ValueError:
                print("Ingrese un número válido")

        case "8":
            print("\n--- Logaritmo personalizado ---")
            try:
                num = float(input("Número: "))
                base = float(input("Base: "))
                if num <= 0 or base <= 0 or base == 1:
                    print("El número y la base deben ser positivos, y la base no puede ser 1.")
                else:
                    resultado = f"Resultado: log{base}({num}) = {math.log(num, base)}"
                    print(resultado)
                    operaciones_guardadas.append("\n--- Logaritmo personalizado ---\n" + resultado + "\n")
            except ValueError:
                print("Ingrese un número válido")

        case "9":
            print("\n--- Seno ---")
            try:
                num = float(input("Número: "))
                resultado = f"Resultado: sen({num}) = {math.sin(num)}"
                print(resultado)
                operaciones_guardadas.append("\n--- Seno ---\n" + resultado + "\n")
            except ValueError:
                print("Ingrese un número válido")

        case "10":
            print("\n--- Coseno ---")
            try:
                num = float(input("Número: "))
                resultado = f"Resultado: cos({num}) = {math.cos(num)}"
                print(resultado)
                operaciones_guardadas.append("\n--- Coseno ---\n" + resultado + "\n")
            except ValueError:
                print("Ingrese un número válido")

        case "11":
            print("\n--- Tangente ---")
            try:
                num = float(input("Número: "))
                resultado = f"Resultado: tan({num}) = {math.tan(num)}"
                print(resultado)
                operaciones_guardadas.append("\n--- Tangente ---\n" + resultado + "\n")
            except ValueError:
                print("Ingrese un número válido")

        case "12":
            print("\n--- Conversión de números ---")
            print("1. Binario")
            print("2. Octal")
            print("3. Decimal")
            print("4. Hexadecimal\n")
            opcion_conv = input("Ingrese una opción: ")
            if opcion_conv == "1":  # Binario
                try:
                    num = int(input("Número: "), 2)
                    resultado = (
                        f"Binario: {bin(num)[2:]}\n"
                        f"Octal: {oct(num)[2:]}\n"
                        f"Decimal: {num}\n"
                        f"Hexadecimal: {hex(num)[2:]}"
                    )
                    print(f"\n{resultado}")
                    operaciones_guardadas.append("\n--- Conversión de números ---\n" + resultado + "\n")
                except ValueError:
                    print("\nIngrese un número binario válido")
            elif opcion_conv == "2":  # Octal
                try:
                    num = int(input("Número: "), 8)
                    resultado = (
                        f"Binario: {bin(num)[2:]}\n"
                        f"Octal: {oct(num)[2:]}\n"
                        f"Decimal: {num}\n"
                        f"Hexadecimal: {hex(num)[2:]}"
                    )
                    print(f"\n{resultado}")
                    operaciones_guardadas.append("\n--- Conversión de números ---\n" + resultado + "\n")
                except ValueError:
                    print("\nIngrese un número octal válido")
            elif opcion_conv == "3":  # Decimal
                try:
                    num = int(input("Número: "))
                    resultado = (
                        f"Binario: {bin(num)[2:]}\n"
                        f"Octal: {oct(num)[2:]}\n"
                        f"Decimal: {num}\n"
                        f"Hexadecimal: {hex(num)[2:]}"
                    )
                    print(f"\n{resultado}")
                    operaciones_guardadas.append("\n--- Conversión de números ---\n" + resultado + "\n")
                except ValueError:
                    print("\nIngrese un número decimal válido")
            elif opcion_conv == "4":  # Hexadecimal
                try:
                    num = int(input("Número: ").upper(), 16)
                    resultado = (
                        f"Binario: {bin(num)[2:]}\n"
                        f"Octal: {oct(num)[2:]}\n"
                        f"Decimal: {num}\n"
                        f"Hexadecimal: {hex(num)[2:]}"
                    )
                    print(f"\n{resultado}")
                    operaciones_guardadas.append("\n--- Conversión de números ---\n" + resultado + "\n")
                except ValueError:
                    print("\nIngrese un número hexadecimal válido")
            else:
                print("\nIngrese una cantidad válida")

        case "13":
            print("\n--- Conversión Longitud ---")
            print("1. Kilómetros")
            print("2. Hectómetros")
            print("3. Decámetros")
            print("4. Metros")
            print("5. Decímetros")
            print("6. Centímetros")
            print("7. Milímetros")
            print("8. Millas")
            print("9. Yardas")
            print("10. Pies")
            print("11. Pulgadas\n")
            opcion_conv = input("Ingrese una opción: ")
            try:
                cantidad = float(input("Ingrese la cantidad: "))
                resultado = None
                if opcion_conv == "1":  # Kilómetros
                    resultado = (
                        f"Km: {cantidad}\n"
                        f"hm: {cantidad * 10}\n"
                        f"dam: {cantidad * 100}\n"
                        f"m: {cantidad * 1000}\n"
                        f"dm: {cantidad * 10000}\n"
                        f"cm: {cantidad * 100000}\n"
                        f"mm: {cantidad * 1000000}\n"
                        f"mi: {cantidad * 0.621371}\n"
                        f"yd: {cantidad * 1093.61}\n"
                        f"ft: {cantidad * 3280.84}\n"
                        f"inch: {cantidad * 39370.1}\n"
                    )
                elif opcion_conv == "2":  # Hectómetros
                    resultado = (
                        f"Km: {cantidad / 10}\n"
                        f"hm: {cantidad}\n"
                        f"dam: {cantidad * 10}\n"
                        f"m: {cantidad * 100}\n"
                        f"dm: {cantidad * 1000}\n"
                        f"cm: {cantidad * 10000}\n"
                        f"mm: {cantidad * 100000}\n"
                        f"mi: {cantidad * 0.0621371}\n"
                        f"yd: {cantidad * 109.361}\n"
                        f"ft: {cantidad * 328.084}\n"
                        f"inch: {cantidad * 3937.01}\n"
                    )
                elif opcion_conv == "3":  # Decámetros
                    resultado = (
                        f"Km: {cantidad / 100}\n"
                        f"hm: {cantidad / 10}\n"
                        f"dam: {cantidad}\n"
                        f"m: {cantidad * 10}\n"
                        f"dm: {cantidad * 100}\n"
                        f"cm: {cantidad * 1000}\n"
                        f"mm: {cantidad * 10000}\n"
                        f"mi: {cantidad * 0.00621371}\n"
                        f"yd: {cantidad * 10.9361}\n"
                        f"ft: {cantidad * 32.8084}\n"
                        f"inch: {cantidad * 393.701}\n"
                    )
                elif opcion_conv == "4":  # Metros
                    resultado = (
                        f"Km: {cantidad / 1000}\n"
                        f"hm: {cantidad / 100}\n"
                        f"dam: {cantidad / 10}\n"
                        f"m: {cantidad}\n"
                        f"dm: {cantidad * 10}\n"
                        f"cm: {cantidad * 100}\n"
                        f"mm: {cantidad * 1000}\n"
                        f"mi: {cantidad * 0.000621371}\n"
                        f"yd: {cantidad * 1.09361}\n"
                        f"ft: {cantidad * 3.28084}\n"
                        f"inch: {cantidad * 39.3701}\n"
                    )
                elif opcion_conv == "5":  # Decímetros
                    resultado = (
                        f"Km: {cantidad / 10000}\n"
                        f"hm: {cantidad / 1000}\n"
                        f"dam: {cantidad / 100}\n"
                        f"m: {cantidad / 10}\n"
                        f"dm: {cantidad}\n"
                        f"cm: {cantidad * 10}\n"
                        f"mm: {cantidad * 100}\n"
                        f"mi: {cantidad * 0.0000621371}\n"
                        f"yd: {cantidad * 0.109361}\n"
                        f"ft: {cantidad * 0.328084}\n"
                        f"inch: {cantidad * 3.93701}\n"
                    )
                elif opcion_conv == "6":  # Centímetros
                    resultado = (
                        f"Km: {cantidad / 100000}\n"
                        f"hm: {cantidad / 10000}\n"
                        f"dam: {cantidad / 1000}\n"
                        f"m: {cantidad / 100}\n"
                        f"dm: {cantidad / 10}\n"
                        f"cm: {cantidad}\n"
                        f"mm: {cantidad * 10}\n"
                        f"mi: {cantidad * 0.00000621371}\n"
                        f"yd: {cantidad * 0.0109361}\n"
                        f"ft: {cantidad * 0.0328084}\n"
                        f"inch: {cantidad * 0.393701}\n"
                    )
                elif opcion_conv == "7":  # Milímetros
                    resultado = (
                        f"Km: {cantidad / 1000000}\n"
                        f"hm: {cantidad / 100000}\n"
                        f"dam: {cantidad / 10000}\n"
                        f"m: {cantidad / 1000}\n"
                        f"dm: {cantidad / 100}\n"
                        f"cm: {cantidad / 10}\n"
                        f"mm: {cantidad}\n"
                        f"mi: {cantidad * 0.000000621371}\n"
                        f"yd: {cantidad * 0.00109361}\n"
                        f"ft: {cantidad * 0.00328084}\n"
                        f"inch: {cantidad * 0.0393701}\n"
                    )
                elif opcion_conv == "8":  # Millas
                    resultado = (
                        f"Km: {cantidad / 0.621371}\n"
                        f"hm: {cantidad / 0.0621371}\n"
                        f"dam: {cantidad / 0.00621371}\n"
                        f"m: {cantidad / 0.000621371}\n"
                        f"dm: {cantidad / 0.0000621371}\n"
                        f"cm: {cantidad / 0.00000621371}\n"
                        f"mm: {cantidad / 0.000000621371}\n"
                        f"mi: {cantidad}\n"
                        f"yd: {cantidad * 1760}\n"
                        f"ft: {cantidad * 5280}\n"
                        f"inch: {cantidad * 63360}\n"
                    )
                elif opcion_conv == "9":  # Yardas
                    resultado = (
                        f"Km: {cantidad / 1093.61}\n"
                        f"hm: {cantidad / 109.361}\n"
                        f"dam: {cantidad / 10.9361}\n"
                        f"m: {cantidad / 1.09361}\n"
                        f"dm: {cantidad / 0.109361}\n"
                        f"cm: {cantidad / 0.0109361}\n"
                        f"mm: {cantidad / 0.00109361}\n"
                        f"mi: {cantidad * 0.000568182}\n"
                        f"yd: {cantidad}\n"
                        f"ft: {cantidad * 3}\n"
                        f"inch: {cantidad * 36}\n"
                    )
                elif opcion_conv == "10":  # Pies
                    resultado = (
                        f"Km: {cantidad / 3280.84}\n"
                        f"hm: {cantidad / 328.084}\n"
                        f"dam: {cantidad / 32.8084}\n"
                        f"m: {cantidad / 3.28084}\n"
                        f"dm: {cantidad / 0.328084}\n"
                        f"cm: {cantidad / 0.0328084}\n"
                        f"mm: {cantidad / 0.00328084}\n"
                        f"mi: {cantidad * 0.000189394}\n"
                        f"yd: {cantidad / 3}\n"
                        f"ft: {cantidad}\n"
                        f"inch: {cantidad * 12}\n"
                    )
                elif opcion_conv == "11":  # Pulgadas
                    resultado = (
                        f"Km: {cantidad / 39370.1}\n"
                        f"hm: {cantidad / 3937.01}\n"
                        f"dam: {cantidad / 393.701}\n"
                        f"m: {cantidad / 39.3701}\n"
                        f"dm: {cantidad / 3.93701}\n"
                        f"cm: {cantidad / 0.393701}\n"
                        f"mm: {cantidad / 0.0393701}\n"
                        f"mi: {cantidad * 0.000015783}\n"
                        f"yd: {cantidad / 36}\n"
                        f"ft: {cantidad / 12}\n"
                        f"inch: {cantidad}\n"
                    )
                else:
                    print("\nOpción inválida")
                if resultado is not None:
                    print(f"\n--- Conversión Longitud ---\n{resultado}")
                    operaciones_guardadas.append(f"\n--- Conversión Longitud ---\n{resultado}")
            except ValueError:
                print("\nIngrese una cantidad válida")

        case "14":
            print("\n--- Conversión de Área ---")
            print("1. Kilómetros cuadrados")
            print("2. héctometros cuadrados")
            print("3. Decámetros cuadrados")
            print("4. Metros cuadrados")
            print("5. Decímetros cuadrados")
            print("6. Centímetros cuadrados")
            print("7. Milímetros cuadrados")
            print("8. Millas cuadradas")
            print("9. Yardas cuadradas")
            print("10. Pies cuadrados")
            print("11. Pulgadas cuadradas\n")
            opcion_conv = input("Ingrese una opción: ")
            try:
                cantidad = float(input("Ingrese la cantidad: "))
                resultado = None
                if opcion_conv == "1":  # Kilómetros cuadrados
                    resultado = (
                        f"Km²: {cantidad}\n"
                        f"hm²: {cantidad * 100}\n"
                        f"dam²: {cantidad * 10000}\n"
                        f"m²: {cantidad * 1000000}\n"
                        f"dm²: {cantidad * 10000000}\n"
                        f"cm²: {cantidad * 10000000000}\n"
                        f"mm²: {cantidad * 1000000000000}\n"
                        f"mi²: {cantidad * 0.386102}\n"
                        f"yd²: {cantidad * 1195990.05}\n"
                        f"ft²: {cantidad * 10763910.4}\n"
                        f"inch²: {cantidad * 1550003100}\n"
                    )
                elif opcion_conv == "2":  # Hectómetros cuadrados
                    resultado = (
                        f"Km²: {cantidad / 100}\n"
                        f"hm²: {cantidad}\n"
                        f"dam²: {cantidad * 100}\n"
                        f"m²: {cantidad * 10000}\n"
                        f"dm²: {cantidad * 100000}\n"
                        f"cm²: {cantidad * 100000000}\n"
                        f"mm²: {cantidad * 10000000000}\n"
                        f"mi²: {cantidad * 0.00386102}\n"
                        f"yd²: {cantidad * 11959.9005}\n"
                        f"ft²: {cantidad * 107639.104}\n"
                        f"inch²: {cantidad * 15500031}\n"
                    )
                elif opcion_conv == "3":  # Decámetros cuadrados
                    resultado = (
                        f"Km²: {cantidad / 10000}\n"
                        f"hm²: {cantidad / 100}\n"
                        f"dam²: {cantidad}\n"
                        f"m²: {cantidad * 10}\n"
                        f"dm²: {cantidad * 100}\n"
                        f"cm²: {cantidad * 100000}\n"
                        f"mm²: {cantidad * 10000000}\n"
                        f"mi²: {cantidad * 0.0000386102}\n"
                        f"yd²: {cantidad * 119.599005}\n"
                        f"ft²: {cantidad * 1076.39104}\n"
                        f"inch²: {cantidad * 155000.31}\n"
                    )
                elif opcion_conv == "4":  # Metros cuadrados
                    resultado = (
                        f"Km²: {cantidad / 1000000}\n"
                        f"hm²: {cantidad / 10000}\n"
                        f"dam²: {cantidad / 1000}\n"
                        f"m²: {cantidad}\n"
                        f"dm²: {cantidad * 100}\n"
                        f"cm²: {cantidad * 10000}\n"
                        f"mm²: {cantidad * 1000000}\n"
                        f"mi²: {cantidad * 0.000000386102}\n"
                        f"yd²: {cantidad * 1.19599005}\n"
                        f"ft²: {cantidad * 10.7639104}\n"
                        f"inch²: {cantidad * 1550.0031}\n"
                    )
                elif opcion_conv == "5":  # Decímetros cuadrados
                    resultado = (
                        f"Km²: {cantidad / 10000000}\n"
                        f"hm²: {cantidad / 100000}\n"
                        f"dam²: {cantidad / 10000}\n"
                        f"m²: {cantidad / 100}\n"
                        f"dm²: {cantidad}\n"
                        f"cm²: {cantidad * 100}\n"
                        f"mm²: {cantidad * 10000}\n"
                        f"mi²: {cantidad * 0.0000000386102}\n"
                        f"yd²: {cantidad * 0.119599005}\n"
                        f"ft²: {cantidad * 1.07639104}\n"
                        f"inch²: {cantidad * 155.00031}\n"
                    )
                elif opcion_conv == "6":  # Centímetros cuadrados
                    resultado = (
                        f"Km²: {cantidad / 10000000000}\n"
                        f"hm²: {cantidad / 100000000}\n"
                        f"dam²: {cantidad / 10000000}\n"
                        f"m²: {cantidad / 10000}\n"
                        f"dm²: {cantidad / 100}\n"
                        f"cm²: {cantidad}\n"
                        f"mm²: {cantidad * 100}\n"
                        f"mi²: {cantidad * 0.000000000386102}\n"
                        f"yd²: {cantidad * 0.00119599005}\n"
                        f"ft²: {cantidad * 0.0107639104}\n"
                        f"inch²: {cantidad * 1.5500031}\n"
                    )
                elif opcion_conv == "7":  # Milímetros cuadrados
                    resultado = (
                        f"Km²: {cantidad / 1000000000000}\n"
                        f"hm²: {cantidad / 10000000000}\n"
                        f"dam²: {cantidad / 1000000000}\n"
                        f"m²: {cantidad / 1000000}\n"
                        f"dm²: {cantidad / 10000}\n"
                        f"cm²: {cantidad / 100}\n"
                        f"mm²: {cantidad}\n"
                        f"mi²: {cantidad * 0.000000000000386102}\n"
                        f"yd²: {cantidad * 0.00000119599005}\n"
                        f"ft²: {cantidad * 0.0000107639104}\n"
                        f"inch²: {cantidad * 0.0015500031}\n"
                    )
                elif opcion_conv == "8":  # Millas cuadradas
                    resultado = (
                        f"Km²: {cantidad / 0.386102}\n"
                        f"hm²: {cantidad / 0.00386102}\n"
                        f"dam²: {cantidad / 0.0000386102}\n"
                        f"m²: {cantidad / 0.000000386102}\n"
                        f"dm²: {cantidad / 0.00000000386102}\n"
                        f"cm²: {cantidad / 0.0000000000386102}\n"
                        f"mm²: {cantidad / 0.000000000000386102}\n"
                        f"mi²: {cantidad}\n"
                        f"yd²: {cantidad * 3097600}\n"
                        f"ft²: {cantidad * 27878400}\n"
                        f"inch²: {cantidad * 4014489600}\n"
                    )
                elif opcion_conv == "9":  # Yardas cuadradas
                    resultado = (
                        f"Km²: {cantidad / 1195990.05}\n"
                        f"hm²: {cantidad / 11959.9005}\n"
                        f"dam²: {cantidad / 119.599005}\n"
                        f"m²: {cantidad / 1.19599005}\n"
                        f"dm²: {cantidad / 0.119599005}\n"
                        f"cm²: {cantidad / 0.00119599005}\n"
                        f"mm²: {cantidad / 0.0000119599005}\n"
                        f"mi²: {cantidad * 0.000000386102}\n"
                        f"yd²: {cantidad}\n"
                        f"ft²: {cantidad * 9}\n"
                        f"inch²: {cantidad * 1296}\n"
                    )
                elif opcion_conv == "10":  # Pies cuadrados
                    resultado = (
                        f"Km²: {cantidad / 10763910.4}\n"
                        f"hm²: {cantidad / 107639.104}\n"
                        f"dam²: {cantidad / 1076.39104}\n"
                        f"m²: {cantidad / 10.7639104}\n"
                        f"dm²: {cantidad / 1.07639104}\n"
                        f"cm²: {cantidad / 0.0107639104}\n"
                        f"mm²: {cantidad / 0.000107639104}\n"
                        f"mi²: {cantidad * 0.0000000386102}\n"
                        f"yd²: {cantidad / 9}\n"
                        f"ft²: {cantidad}\n"
                        f"inch²: {cantidad * 144}\n"
                    )
                elif opcion_conv == "11":  # Pulgadas cuadradas
                    resultado = (
                        f"Km²: {cantidad / 1550003100}\n"
                        f"hm²: {cantidad / 15500031}\n"
                        f"dam²: {cantidad / 155000.31}\n"
                        f"m²: {cantidad / 1550.0031}\n"
                        f"dm²: {cantidad / 155.00031}\n"
                        f"cm²: {cantidad / 1.5500031}\n"
                        f"mm²: {cantidad / 0.15500031}\n"
                        f"mi²: {cantidad * 0.000000000386102}\n"
                        f"yd²: {cantidad / 1296}\n"
                        f"ft²: {cantidad / 144}\n"
                        f"inch²: {cantidad}\n"
                    )
                else:
                    print("\nOpción inválida")
                if resultado is not None:
                    print(f"\n--- Conversión de Área ---\n{resultado}")
                    operaciones_guardadas.append(f"\n--- Conversión de Área ---\n{resultado}")
            except ValueError:
                print("\nIngrese una cantidad válida")

        case "15":
            print("\n--- Conversión Volumen ---")
            print("1. Kilómetros cúbicos")
            print("2. Hectómetros cúbicos")
            print("3. Decámetros cúbicos")
            print("4. Metros cúbicos")
            print("5. Decímetros cúbicos")
            print("6. Centímetros cúbicos")
            print("7. Milímetros cúbicos")
            print("8. Litros")
            print("9. Millas cúbicas")
            print("10. Yardas cúbicas")
            print("11. Pies cúbicos")
            print("12. Pulgadas cúbicas\n")
            opcion_conv = input("Ingrese una opción: ")
            try:
                cantidad = float(input("Ingrese la cantidad: "))
                resultado = None
                if opcion_conv == "1":  # Kilómetros cúbicos
                    resultado = (
                        f"Km³: {cantidad}\n"
                        f"hm³: {cantidad * 1000}\n"
                        f"dam³: {cantidad * 1000000}\n"
                        f"m³: {cantidad * 1000000000}\n"
                        f"dm³: {cantidad * 1000000000000}\n"
                        f"cm³: {cantidad * 1000000000000000}\n"
                        f"mm³: {cantidad * 1000000000000000000}\n"
                        f"L: {cantidad * 1e+12}\n"
                        f"mi³: {cantidad * 0.239913}\n"
                        f"yd³: {cantidad * 1307950619}\n"
                        f"ft³: {cantidad * 35314666721}\n"
                        f"inch³: {cantidad * 6.10237e+13}\n"
                    )
                elif opcion_conv == "2":  # Hectómetros cúbicos
                    resultado = (
                        f"Km³: {cantidad / 1000}\n"
                        f"hm³: {cantidad}\n"
                        f"dam³: {cantidad * 1000}\n"
                        f"m³: {cantidad * 1000000}\n"
                        f"dm³: {cantidad * 1000000000}\n"
                        f"cm³: {cantidad * 1000000000000}\n"
                        f"mm³: {cantidad * 1000000000000000}\n"
                        f"L: {cantidad * 1e+9}\n"
                        f"mi³: {cantidad * 0.000239913}\n"
                        f"yd³: {cantidad * 1307950.619}\n"
                        f"ft³: {cantidad * 3531466.6721}\n"
                        f"inch³: {cantidad * 6.10237e+12}\n"
                    )
                elif opcion_conv == "3":  # Decámetros cúbicos
                    resultado = (
                        f"Km³: {cantidad / 1000000}\n"
                        f"hm³: {cantidad / 1000}\n"
                        f"dam³: {cantidad}\n"
                        f"m³: {cantidad * 1000}\n"
                        f"dm³: {cantidad * 1000000}\n"
                        f"cm³: {cantidad * 1000000000}\n"
                        f"mm³: {cantidad * 1000000000000}\n"
                        f"L: {cantidad * 1000000}\n"
                        f"mi³: {cantidad * 2.39913e-7}\n"
                        f"yd³: {cantidad * 1307.950619}\n"
                        f"ft³: {cantidad * 3531.4666721}\n"
                        f"inch³: {cantidad * 6.10237e+9}\n"
                    )
                elif opcion_conv == "4":  # Metros cúbicos
                    resultado = (
                        f"Km³: {cantidad / 1000000000}\n"
                        f"hm³: {cantidad / 1000000}\n"
                        f"dam³: {cantidad / 1000}\n"
                        f"m³: {cantidad}\n"
                        f"dm³: {cantidad * 1000}\n"
                        f"cm³: {cantidad * 1000000}\n"
                        f"mm³: {cantidad * 1000000000}\n"
                        f"L: {cantidad * 1000}\n"
                        f"mi³: {cantidad * 2.39913e-10}\n"
                        f"yd³: {cantidad * 1.307950619}\n"
                        f"ft³: {cantidad * 35.314666721}\n"
                        f"inch³: {cantidad * 6.10237e+8}\n"
                    )
                elif opcion_conv == "5":  # Decímetros cúbicos
                    resultado = (
                        f"Km³: {cantidad / 1000000000000}\n"
                        f"hm³: {cantidad / 1000000000}\n"
                        f"dam³: {cantidad / 1000000}\n"
                        f"m³: {cantidad / 1000}\n"
                        f"dm³: {cantidad}\n"
                        f"cm³: {cantidad * 1000}\n"
                        f"mm³: {cantidad * 1000000}\n"
                        f"L: {cantidad}\n"
                        f"mi³: {cantidad * 2.39913e-13}\n"
                        f"yd³: {cantidad * 0.001307950619}\n"
                        f"ft³: {cantidad * 0.035314666721}\n"
                        f"inch³: {cantidad * 61.0237}\n"
                    )
                elif opcion_conv == "6":  # Centímetros cúbicos
                    resultado = (
                        f"Km³: {cantidad / 1000000000000000}\n"
                        f"hm³: {cantidad / 1000000000000}\n"
                        f"dam³: {cantidad / 1000000000}\n"
                        f"m³: {cantidad / 1000000}\n"
                        f"dm³: {cantidad / 1000}\n"
                        f"cm³: {cantidad}\n"
                        f"mm³: {cantidad * 1000}\n"
                        f"L: {cantidad / 1000}\n"
                        f"mi³: {cantidad * 2.39913e-16}\n"
                        f"yd³: {cantidad * 1.307950619e-6}\n"
                        f"ft³: {cantidad * 3.5314666721e-5}\n"
                        f"inch³: {cantidad * 0.0610237}\n"
                    )
                elif opcion_conv == "7":  # Milímetros cúbicos
                    resultado = (
                        f"Km³: {cantidad / 1000000000000000000}\n"
                        f"hm³: {cantidad / 1000000000000000}\n"
                        f"dam³: {cantidad / 1000000000000}\n"
                        f"m³: {cantidad / 1000000000}\n"
                        f"dm³: {cantidad / 1000000}\n"
                        f"cm³: {cantidad / 1000}\n"
                        f"mm³: {cantidad}\n"
                        f"L: {cantidad / 1000000}\n"
                        f"mi³: {cantidad * 2.39913e-19}\n"
                        f"yd³: {cantidad * 1.307950619e-9}\n"
                        f"ft³: {cantidad * 3.5314666721e-8}\n"
                        f"inch³: {cantidad * 6.10237e-5}\n"
                    )
                elif opcion_conv == "8":  # Litros
                    resultado = (
                        f"Km³: {cantidad / 1e+12}\n"
                        f"hm³: {cantidad / 1e+9}\n"
                        f"dam³: {cantidad / 1000000}\n"
                        f"m³: {cantidad / 1000}\n"
                        f"dm³: {cantidad}\n"
                        f"cm³: {cantidad * 1000}\n"
                        f"mm³: {cantidad * 1000000}\n"
                        f"L: {cantidad}\n"
                        f"mi³: {cantidad * 2.39913e-13}\n"
                        f"yd³: {cantidad * 0.001307950619}\n"
                        f"ft³: {cantidad * 0.035314666721}\n"
                        f"inch³: {cantidad * 61.0237}\n"
                    )
                elif opcion_conv == "9":  # Millas cúbicas
                    resultado = (
                        f"Km³: {cantidad / 0.239913}\n"
                        f"hm³: {cantidad / 0.000239913}\n"
                        f"dam³: {cantidad / 2.39913e-7}\n"
                        f"m³: {cantidad / 2.39913e-10}\n"
                        f"dm³: {cantidad / 2.39913e-13}\n"
                        f"cm³: {cantidad / 2.39913e-16}\n"
                        f"mm³: {cantidad / 2.39913e-19}\n"
                        f"L: {cantidad / 2.39913e-13}\n"
                        f"mi³: {cantidad}\n"
                        f"yd³: {cantidad * 5451776000}\n"
                        f"ft³: {cantidad * 147197952000}\n"
                        f"inch³: {cantidad * 2.54358e+14}\n"
                    )
                elif opcion_conv == "10":  # Yardas cúbicas
                    resultado = (
                        f"Km³: {cantidad / 1307950619}\n"
                        f"hm³: {cantidad / 1307950.619}\n"
                        f"dam³: {cantidad / 1307.950619}\n"
                        f"m³: {cantidad / 1.307950619}\n"
                        f"dm³: {cantidad / 0.001307950619}\n"
                        f"cm³: {cantidad / 1.307950619e-6}\n"
                        f"mm³: {cantidad / 1.307950619e-9}\n"
                        f"L: {cantidad / 0.001307950619}\n"
                        f"mi³: {cantidad * 1.83438e-10}\n"
                        f"yd³: {cantidad}\n"
                        f"ft³: {cantidad * 27}\n"
                        f"inch³: {cantidad * 46656}\n"
                    )
                elif opcion_conv == "11":  # Pies cúbicos
                    resultado = (
                        f"Km³: {cantidad / 35314666721}\n"
                        f"hm³: {cantidad / 3531466.6721}\n"
                        f"dam³: {cantidad / 3531.4666721}\n"
                        f"m³: {cantidad / 35.314666721}\n"
                        f"dm³: {cantidad / 0.035314666721}\n"
                        f"cm³: {cantidad / 3.5314666721e-5}\n"
                        f"mm³: {cantidad / 3.5314666721e-8}\n"
                        f"L: {cantidad / 0.035314666721}\n"
                        f"mi³: {cantidad * 6.7942e-12}\n"
                        f"yd³: {cantidad / 27}\n"
                        f"ft³: {cantidad}\n"
                        f"inch³: {cantidad * 1728}\n"
                    )
                elif opcion_conv == "12":  # Pulgadas cúbicas
                    resultado = (
                        f"Km³: {cantidad / 6.10237e+13}\n"
                        f"hm³: {cantidad / 6.10237e+12}\n"
                        f"dam³: {cantidad / 6.10237e+9}\n"
                        f"m³: {cantidad / 6.10237e+8}\n"
                        f"dm³: {cantidad / 61.0237}\n"
                        f"cm³: {cantidad / 0.0610237}\n"
                        f"mm³: {cantidad / 6.10237e-5}\n"
                        f"L: {cantidad / 61.0237}\n"
                        f"mi³: {cantidad * 3.9317e-15}\n"
                        f"yd³: {cantidad / 46656}\n"
                        f"ft³: {cantidad / 1728}\n"
                        f"inch³: {cantidad}\n"
                    )
                else:
                    print("\nOpción inválida")
                if resultado is not None:
                    print(f"\n--- Conversión Volumen ---\n{resultado}")
                    operaciones_guardadas.append(f"\n--- Conversión Volumen ---\n{resultado}")
            except ValueError:
                print("\nIngrese una cantidad válida")

        case "16":
            print("\n--- Conversión Masa ---")
            print("1. Kilogramo")
            print("2. Hectogramo")
            print("3. Decagramo")
            print("4. Gramo")
            print("5. Decigramo")
            print("6. Centigramo")
            print("7. Miligramo")
            print("8. Tonelada")
            print("9. Libra")
            print("10. Onza\n")
            opcion_conv = input("Ingrese una opción: ")
            try:
                cantidad = float(input("Ingrese la cantidad: "))
                resultado = None
                if opcion_conv == "1":  # Kilogramo
                    resultado = (
                        f"kg: {cantidad}\n"
                        f"hg: {cantidad * 10}\n"
                        f"dag: {cantidad * 100}\n"
                        f"g: {cantidad * 1000}\n"
                        f"dg: {cantidad * 10000}\n"
                        f"cg: {cantidad * 100000}\n"
                        f"mg: {cantidad * 1000000}\n"
                        f"ton: {cantidad / 1000}\n"
                        f"lb: {cantidad * 2.20462}\n"
                        f"oz: {cantidad * 35.274}\n"
                    )
                elif opcion_conv == "2":  # Hectogramo
                    resultado = (
                        f"kg: {cantidad / 10}\n"
                        f"hg: {cantidad}\n"
                        f"dag: {cantidad * 10}\n"
                        f"g: {cantidad * 100}\n"
                        f"dg: {cantidad * 1000}\n"
                        f"cg: {cantidad * 10000}\n"
                        f"mg: {cantidad * 100000}\n"
                        f"ton: {cantidad / 10000}\n"
                        f"lb: {cantidad * 0.220462}\n"
                        f"oz: {cantidad * 3.5274}\n"
                    )
                elif opcion_conv == "3":  # Decagramo
                    resultado = (
                        f"kg: {cantidad / 100}\n"
                        f"hg: {cantidad / 10}\n"
                        f"dag: {cantidad}\n"
                        f"g: {cantidad * 10}\n"
                        f"dg: {cantidad * 100}\n"
                        f"cg: {cantidad * 1000}\n"
                        f"mg: {cantidad * 10000}\n"
                        f"ton: {cantidad / 100000}\n"
                        f"lb: {cantidad * 0.0220462}\n"
                        f"oz: {cantidad * 0.35274}\n"
                    )
                elif opcion_conv == "4":  # Gramo
                    resultado = (
                        f"kg: {cantidad / 1000}\n"
                        f"hg: {cantidad / 100}\n"
                        f"dag: {cantidad / 10}\n"
                        f"g: {cantidad}\n"
                        f"dg: {cantidad * 10}\n"
                        f"cg: {cantidad * 100}\n"
                        f"mg: {cantidad * 1000}\n"
                        f"ton: {cantidad / 1000000}\n"
                        f"lb: {cantidad * 0.00220462}\n"
                        f"oz: {cantidad * 0.035274}\n"
                    )
                elif opcion_conv == "5":  # Decigramo
                    resultado = (
                        f"kg: {cantidad / 10000}\n"
                        f"hg: {cantidad / 1000}\n"
                        f"dag: {cantidad / 100}\n"
                        f"g: {cantidad / 10}\n"
                        f"dg: {cantidad}\n"
                        f"cg: {cantidad * 10}\n"
                        f"mg: {cantidad * 100}\n"
                        f"ton: {cantidad / 10000000}\n"
                        f"lb: {cantidad * 0.000220462}\n"
                        f"oz: {cantidad * 0.0035274}\n"
                    )
                elif opcion_conv == "6":  # Centigramo
                    resultado = (
                        f"kg: {cantidad / 100000}\n"
                        f"hg: {cantidad / 10000}\n"
                        f"dag: {cantidad / 1000}\n"
                        f"g: {cantidad / 100}\n"
                        f"dg: {cantidad / 10}\n"
                        f"cg: {cantidad}\n"
                        f"mg: {cantidad * 10}\n"
                        f"ton: {cantidad / 100000000}\n"
                        f"lb: {cantidad * 0.0000220462}\n"
                        f"oz: {cantidad * 0.00035274}\n"
                    )
                elif opcion_conv == "7":  # Miligramo
                    resultado = (
                        f"kg: {cantidad / 1000000}\n"
                        f"hg: {cantidad / 100000}\n"
                        f"dag: {cantidad / 10000}\n"
                        f"g: {cantidad / 1000}\n"
                        f"dg: {cantidad / 100}\n"
                        f"cg: {cantidad / 10}\n"
                        f"mg: {cantidad}\n"
                        f"ton: {cantidad / 1000000000}\n"
                        f"lb: {cantidad * 0.00000220462}\n"
                        f"oz: {cantidad * 0.000035274}\n"
                    )
                elif opcion_conv == "8":  # Tonelada
                    resultado = (
                        f"kg: {cantidad * 1000}\n"
                        f"hg: {cantidad * 10000}\n"
                        f"dag: {cantidad * 100000}\n"
                        f"g: {cantidad * 1000000}\n"
                        f"dg: {cantidad * 10000000}\n"
                        f"cg: {cantidad * 100000000}\n"
                        f"mg: {cantidad * 1000000000}\n"
                        f"ton: {cantidad}\n"
                        f"lb: {cantidad * 2204.62}\n"
                        f"oz: {cantidad * 35274}\n"
                    )
                elif opcion_conv == "9":  # Libra
                    resultado = (
                        f"kg: {cantidad / 2.20462}\n"
                        f"hg: {cantidad / 0.220462}\n"
                        f"dag: {cantidad / 0.0220462}\n"
                        f"g: {cantidad / 0.00220462}\n"
                        f"dg: {cantidad / 0.000220462}\n"
                        f"cg: {cantidad / 0.0000220462}\n"
                        f"mg: {cantidad / 0.00000220462}\n"
                        f"ton: {cantidad / 2204.62}\n"
                        f"lb: {cantidad}\n"
                        f"oz: {cantidad * 16}\n"
                    )
                elif opcion_conv == "10":  # Onza
                    resultado = (
                        f"kg: {cantidad / 35.274}\n"
                        f"hg: {cantidad / 3.5274}\n"
                        f"dag: {cantidad / 0.35274}\n"
                        f"g: {cantidad / 0.035274}\n"
                        f"dg: {cantidad / 0.0035274}\n"
                        f"cg: {cantidad / 0.00035274}\n"
                        f"mg: {cantidad / 0.000035274}\n"
                        f"ton: {cantidad / 35274}\n"
                        f"lb: {cantidad / 16}\n"
                        f"oz: {cantidad}\n"
                    )
                else:
                    print("\nOpción inválida")
                if resultado is not None:
                    print(f"\n--- Conversión Masa ---\n{resultado}")
                    operaciones_guardadas.append(f"\n--- Conversión Masa ---\n{resultado}")
            except ValueError:
                print("\nIngrese una cantidad válida")

        case "17":
            print("\n--- Conversión Temperatura ---")
            print("1. Celsius")
            print("2. Fahrenheit")
            print("3. Kelvin\n")
            opcion_conv = input("Ingrese una opción: ")
            try:
                cantidad = float(input("Ingrese la cantidad: "))
                resultado = None
                if opcion_conv == "1":  # Celsius
                    resultado = (
                        f"Celsius: {cantidad}\n"
                        f"Fahrenheit: {(cantidad * 9/5) + 32}\n"
                        f"Kelvin: {cantidad + 273.15}\n"
                    )
                elif opcion_conv == "2":  # Fahrenheit
                    resultado = (
                        f"Celsius: {(cantidad - 32) * 5/9}\n"
                        f"Fahrenheit: {cantidad}\n"
                        f"Kelvin: {(cantidad - 32) * 5/9 + 273.15}\n"
                    )
                elif opcion_conv == "3":  # Kelvin
                    resultado = (
                        f"Celsius: {cantidad - 273.15}\n"
                        f"Fahrenheit: {(cantidad - 273.15) * 9/5 + 32}\n"
                        f"Kelvin: {cantidad}\n"
                    )
                else:
                    print("\nOpción inválida")
                if resultado is not None:
                    print(f"\n--- Conversión Temperatura ---\n{resultado}")
                    operaciones_guardadas.append(f"\n--- Conversión Temperatura ---\n{resultado}")
            except ValueError:
                print("\nIngrese una cantidad válida")

        case "18":
            print("\n--- Conversión Tiempo ---")
            print("1. Día")
            print("2. Hora")
            print("3. Minuto")
            print("4. Segundo\n")
            opcion_conv = input("Ingrese una opción: ")
            try:
                cantidad = float(input("Ingrese la cantidad: "))
                resultado = None
                if opcion_conv == "1":  # Día
                    resultado = (
                        f"Día: {cantidad}\n"
                        f"Hora: {cantidad * 24}\n"
                        f"Minuto: {cantidad * 1440}\n"
                        f"Segundo: {cantidad * 86400}\n"
                    )
                elif opcion_conv == "2":  # Hora
                    resultado = (
                        f"Día: {cantidad / 24}\n"
                        f"Hora: {cantidad}\n"
                        f"Minuto: {cantidad * 60}\n"
                        f"Segundo: {cantidad * 3600}\n"
                    )
                elif opcion_conv == "3":  # Minuto
                    resultado = (
                        f"Día: {cantidad / 1440}\n"
                        f"Hora: {cantidad / 60}\n"
                        f"Minuto: {cantidad}\n"
                        f"Segundo: {cantidad * 60}\n"
                    )
                elif opcion_conv == "4":  # Segundo
                    resultado = (
                        f"Día: {cantidad / 86400}\n"
                        f"Hora: {cantidad / 3600}\n"
                        f"Minuto: {cantidad / 60}\n"
                        f"Segundo: {cantidad}\n"
                    )
                else:
                    print("\nOpción inválida")
                if resultado is not None:
                    print(f"\n--- Conversión Tiempo ---\n{resultado}")
                    operaciones_guardadas.append(f"\n--- Conversión Tiempo ---\n{resultado}")
            except ValueError:
                print("\nIngrese una cantidad válida")

        case "19":
            print("\n--- Historial de Operaciones ---\n")
            for operacion in operaciones_guardadas:
                print(operacion)

        case "20":
            os.system("cls")

        case "21":
            os.system("cls")
            flag = False

        case _:
            print("Opción no válida")

    if opcion != "20" and opcion != "21":
        continuar = input("\n¿Desea realizar otra operación? (s/n): ")
        if continuar.lower() == "n":
            flag = False
            os.system("cls")
