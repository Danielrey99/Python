"""
Crear una calculadora con distintas funcionalidades
"""
# Sistema de expresiones complejas (5 + 3) * (10 / 2^2)
# Historial guarda las 10 últimas operaciones
# Conversion de monedas
# Geometría (Área y perímetro de figuras geométricas)
# -circulo, cuadrado, rectángulo, triángulo, trapecio, rombo, romboide, polígono regular
# Numeros primos


import os
import math

flag = True

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
    print("19. Limpiar consola")
    print("20. Salir\n")

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
                print(f"Resultado: {num1} + {num2} = {num1 + num2}")
            except ValueError:
                print("Ingrese un número válido")

        case "2":
            print("\n--- Restar ---")
            print("Ingrese dos números")
            try:
                num1 = float(input("Número 1: "))
                num2 = float(input("Número 2: "))
                print(f"Resultado: {num1} - {num2} = {num1 - num2}")
            except ValueError:
                print("Ingrese un número válido")

        case "3":
            print("\n--- Multiplicar ---")
            print("Ingrese dos números")
            try:
                num1 = float(input("Número 1: "))
                num2 = float(input("Número 2: "))
                print(f"Resultado: {num1} x {num2} = {num1 * num2}")
            except ValueError:
                print("Ingrese un número válido")

        case "4":
            print("\n--- Dividir ---")
            print("Ingrese dos números")
            try:
                num1 = float(input("Número 1: "))
                num2 = float(input("Número 2: "))
                print(f"Resultado: {num1} / {num2} = {num1 / num2}")
                print(f"Resto: {num1 % num2}")
                print(f"Cociente: {num1 // num2}")
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
                print(f"Resultado: {num1}^{num2} = {num1 ** num2}")
            except ValueError:
                print("Ingrese un número válido")

        case "6":
            print("\n--- Raíz cuadrada ---")
            try:
                num = float(input("Número: "))
                if num < 0:
                    print("No se puede calcular la raíz cuadrada de un número negativo")
                else:
                    print(f"Resultado: √{num} = {math.sqrt(num)}")
            except ValueError:
                print("Ingrese un número válido")

        case "7":
            print("\n--- Logaritmo natural ---")
            try:
                num = float(input("Número: "))
                if num <= 0:
                    print("El número debe ser positivo")
                else:
                    print(f"Resultado: ln({num}) = {math.log(num)}")
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
                    print(f"Resultado: log{base}({num}) = {math.log(num, base)}")
            except ValueError:
                print("Ingrese un número válido")

        case "9":
            print("\n--- Seno ---")
            try:
                num = float(input("Número: "))
                print(f"Resultado: sen({num}) = {math.sin(num)}")
            except ValueError:
                print("Ingrese un número válido")

        case "10":
            print("\n--- Coseno ---")
            try:
                num = float(input("Número: "))
                print(f"Resultado: cos({num}) = {math.cos(num)}")
            except ValueError:
                print("Ingrese un número válido")

        case "11":
            print("\n--- Tangente ---")
            try:
                num = float(input("Número: "))
                print(f"Resultado: tan({num}) = {math.tan(num)}")
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
                    print(f"\nBinario: {bin(num)}")
                    print(f"Octal: {oct(num)}")
                    print(f"Decimal: {num}")
                    print(f"Hexadecimal: {hex(num)}")
                except ValueError:
                    print("\nIngrese un número binario válido")
            elif opcion_conv == "2":  # Octal
                try:
                    num = int(input("Número: "), 8)
                    print(f"\nBinario: {bin(num)}")
                    print(f"Octal: {oct(num)}")
                    print(f"Decimal: {num}")
                    print(f"Hexadecimal: {hex(num)}")
                except ValueError:
                    print("\nIngrese un número octal válido")
            elif opcion_conv == "3":  # Decimal
                try:
                    num = int(input("Número: "))
                    print(f"\nBinario: {bin(num)}")
                    print(f"Octal: {oct(num)}")
                    print(f"Decimal: {num}")
                    print(f"Hexadecimal: {hex(num)}")
                except ValueError:
                    print("\nIngrese un número decimal válido")
            elif opcion_conv == "4":  # Hexadecimal
                try:
                    num = int(input("Número: "), 16)
                    print(f"\nBinario: {bin(num)}")
                    print(f"Octal: {oct(num)}")
                    print(f"Decimal: {num}")
                    print(f"Hexadecimal: {hex(num)}")
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
                if opcion_conv == "1":  # Kilómetros
                    print(f"\nKm: {cantidad}")
                    print(f"hm: {cantidad * 10}")
                    print(f"dam: {cantidad * 100}")
                    print(f"m: {cantidad * 1000}")
                    print(f"dm: {cantidad * 10000}")
                    print(f"cm: {cantidad * 100000}")
                    print(f"mm: {cantidad * 1000000}")
                    print(f"mi: {cantidad * 0.621371}")
                    print(f"yd: {cantidad * 1093.61}")
                    print(f"ft: {cantidad * 3280.84}")
                    print(f"inch: {cantidad * 39370.1}")
                elif opcion_conv == "2":  # Hectómetros
                    print(f"\nKm: {cantidad / 10}")
                    print(f"hm: {cantidad}")
                    print(f"dam: {cantidad * 10}")
                    print(f"m: {cantidad * 100}")
                    print(f"dm: {cantidad * 1000}")
                    print(f"cm: {cantidad * 10000}")
                    print(f"mm: {cantidad * 100000}")
                    print(f"mi: {cantidad * 0.0621371}")
                    print(f"yd: {cantidad * 109.361}")
                    print(f"ft: {cantidad * 328.084}")
                    print(f"inch: {cantidad * 3937.01}")
                elif opcion_conv == "3":  # Decámetros
                    print(f"\nKm: {cantidad / 100}")
                    print(f"hm: {cantidad / 10}")
                    print(f"dam: {cantidad}")
                    print(f"m: {cantidad * 10}")
                    print(f"dm: {cantidad * 100}")
                    print(f"cm: {cantidad * 1000}")
                    print(f"mm: {cantidad * 10000}")
                    print(f"mi: {cantidad * 0.00621371}")
                    print(f"yd: {cantidad * 10.9361}")
                    print(f"ft: {cantidad * 32.8084}")
                    print(f"inch: {cantidad * 393.701}")
                elif opcion_conv == "4":  # Metros
                    print(f"\nKm: {cantidad / 1000}")
                    print(f"hm: {cantidad / 100}")
                    print(f"dam: {cantidad / 10}")
                    print(f"m: {cantidad}")
                    print(f"dm: {cantidad * 10}")
                    print(f"cm: {cantidad * 100}")
                    print(f"mm: {cantidad * 1000}")
                    print(f"mi: {cantidad * 0.000621371}")
                    print(f"yd: {cantidad * 1.09361}")
                    print(f"ft: {cantidad * 3.28084}")
                    print(f"inch: {cantidad * 39.3701}")
                elif opcion_conv == "5":  # Decímetros
                    print(f"\nKm: {cantidad / 10000}")
                    print(f"hm: {cantidad / 1000}")
                    print(f"dam: {cantidad / 100}")
                    print(f"m: {cantidad / 10}")
                    print(f"dm: {cantidad}")
                    print(f"cm: {cantidad * 10}")
                    print(f"mm: {cantidad * 100}")
                    print(f"mi: {cantidad * 0.0000621371}")
                    print(f"yd: {cantidad * 0.109361}")
                    print(f"ft: {cantidad * 0.328084}")
                    print(f"inch: {cantidad * 3.93701}")
                elif opcion_conv == "6":  # Centímetros
                    print(f"\nKm: {cantidad / 100000}")
                    print(f"hm: {cantidad / 10000}")
                    print(f"dam: {cantidad / 1000}")
                    print(f"m: {cantidad / 100}")
                    print(f"dm: {cantidad / 10}")
                    print(f"cm: {cantidad}")
                    print(f"mm: {cantidad * 10}")
                    print(f"mi: {cantidad * 0.00000621371}")
                    print(f"yd: {cantidad * 0.0109361}")
                    print(f"ft: {cantidad * 0.0328084}")
                    print(f"inch: {cantidad * 0.393701}")
                elif opcion_conv == "7":  # Milímetros
                    print(f"\nKm: {cantidad / 1000000}")
                    print(f"hm: {cantidad / 100000}")
                    print(f"dam: {cantidad / 10000}")
                    print(f"m: {cantidad / 1000}")
                    print(f"dm: {cantidad / 100}")
                    print(f"cm: {cantidad / 10}")
                    print(f"mm: {cantidad}")
                    print(f"mi: {cantidad * 0.000000621371}")
                    print(f"yd: {cantidad * 0.00109361}")
                    print(f"ft: {cantidad * 0.00328084}")
                    print(f"inch: {cantidad * 0.0393701}")
                elif opcion_conv == "8":  # Millas
                    print(f"\nKm: {cantidad / 0.621371}")
                    print(f"hm: {cantidad / 0.0621371}")
                    print(f"dam: {cantidad / 0.00621371}")
                    print(f"m: {cantidad / 0.000621371}")
                    print(f"dm: {cantidad / 0.0000621371}")
                    print(f"cm: {cantidad / 0.00000621371}")
                    print(f"mm: {cantidad / 0.000000621371}")
                    print(f"mi: {cantidad}")
                    print(f"yd: {cantidad * 1760}")
                    print(f"ft: {cantidad * 5280}")
                    print(f"inch: {cantidad * 63360}")
                elif opcion_conv == "9":  # Yardas
                    print(f"\nKm: {cantidad / 1093.61}")
                    print(f"hm: {cantidad / 109.361}")
                    print(f"dam: {cantidad / 10.9361}")
                    print(f"m: {cantidad / 1.09361}")
                    print(f"dm: {cantidad / 0.109361}")
                    print(f"cm: {cantidad / 0.0109361}")
                    print(f"mm: {cantidad / 0.00109361}")
                    print(f"mi: {cantidad * 0.000568182}")
                    print(f"yd: {cantidad}")
                    print(f"ft: {cantidad * 3}")
                    print(f"inch: {cantidad * 36}")
                elif opcion_conv == "10":  # Pies
                    print(f"\nKm: {cantidad / 3280.84}")
                    print(f"hm: {cantidad / 328.084}")
                    print(f"dam: {cantidad / 32.8084}")
                    print(f"m: {cantidad / 3.28084}")
                    print(f"dm: {cantidad / 0.328084}")
                    print(f"cm: {cantidad / 0.0328084}")
                    print(f"mm: {cantidad / 0.00328084}")
                    print(f"mi: {cantidad * 0.000189394}")
                    print(f"yd: {cantidad / 3}")
                    print(f"ft: {cantidad}")
                    print(f"inch: {cantidad * 12}")
                elif opcion_conv == "11":  # Pulgadas
                    print(f"\nKm: {cantidad / 39370.1}")
                    print(f"hm: {cantidad / 3937.01}")
                    print(f"dam: {cantidad / 393.701}")
                    print(f"m: {cantidad / 39.3701}")
                    print(f"dm: {cantidad / 3.93701}")
                    print(f"cm: {cantidad / 0.393701}")
                    print(f"mm: {cantidad / 0.0393701}")
                    print(f"mi: {cantidad * 0.000015783}")
                    print(f"yd: {cantidad / 36}")
                    print(f"ft: {cantidad / 12}")
                    print(f"inch: {cantidad}")
                else:
                    print("\nOpción inválida")
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
                if opcion_conv == "1":  # Kilómetros cuadrados
                    print(f"\nKm²: {cantidad}")
                    print(f"hm²: {cantidad * 100}")
                    print(f"dam²: {cantidad * 10000}")
                    print(f"m²: {cantidad * 1000000}")
                    print(f"dm²: {cantidad * 10000000}")
                    print(f"cm²: {cantidad * 10000000000}")
                    print(f"mm²: {cantidad * 1000000000000}")
                    print(f"mi²: {cantidad * 0.386102}")
                    print(f"yd²: {cantidad * 1195990.05}")
                    print(f"ft²: {cantidad * 10763910.4}")
                    print(f"inch²: {cantidad * 1550003100}")
                elif opcion_conv == "2":  # Hectómetros cuadrados
                    print(f"\nKm²: {cantidad / 100}")
                    print(f"hm²: {cantidad}")
                    print(f"dam²: {cantidad * 100}")
                    print(f"m²: {cantidad * 10000}")
                    print(f"dm²: {cantidad * 100000}")
                    print(f"cm²: {cantidad * 100000000}")
                    print(f"mm²: {cantidad * 10000000000}")
                    print(f"mi²: {cantidad * 0.00386102}")
                    print(f"yd²: {cantidad * 11959.9005}")
                    print(f"ft²: {cantidad * 107639.104}")
                    print(f"inch²: {cantidad * 15500031}")
                elif opcion_conv == "3":  # Decámetros cuadrados
                    print(f"\nKm²: {cantidad / 10000}")
                    print(f"hm²: {cantidad / 100}")
                    print(f"dam²: {cantidad}")
                    print(f"m²: {cantidad * 10}")
                    print(f"dm²: {cantidad * 100}")
                    print(f"cm²: {cantidad * 100000}")
                    print(f"mm²: {cantidad * 10000000}")
                    print(f"mi²: {cantidad * 0.0000386102}")
                    print(f"yd²: {cantidad * 119.599005}")
                    print(f"ft²: {cantidad * 1076.39104}")
                    print(f"inch²: {cantidad * 155000.31}")
                elif opcion_conv == "4":  # Metros cuadrados
                    print(f"\nKm²: {cantidad / 1000000}")
                    print(f"hm²: {cantidad / 10000}")
                    print(f"dam²: {cantidad / 1000}")
                    print(f"m²: {cantidad}")
                    print(f"dm²: {cantidad * 100}")
                    print(f"cm²: {cantidad * 10000}")
                    print(f"mm²: {cantidad * 1000000}")
                    print(f"mi²: {cantidad * 0.000000386102}")
                    print(f"yd²: {cantidad * 1.19599005}")
                    print(f"ft²: {cantidad * 10.7639104}")
                    print(f"inch²: {cantidad * 1550.0031}")
                elif opcion_conv == "5":  # Decímetros cuadrados
                    print(f"\nKm²: {cantidad / 10000000}")
                    print(f"hm²: {cantidad / 100000}")
                    print(f"dam²: {cantidad / 10000}")
                    print(f"m²: {cantidad / 100}")
                    print(f"dm²: {cantidad}")
                    print(f"cm²: {cantidad * 100}")
                    print(f"mm²: {cantidad * 10000}")
                    print(f"mi²: {cantidad * 0.0000000386102}")
                    print(f"yd²: {cantidad * 0.119599005}")
                    print(f"ft²: {cantidad * 1.07639104}")
                    print(f"inch²: {cantidad * 155.00031}")
                elif opcion_conv == "6":  # Centímetros cuadrados
                    print(f"\nKm²: {cantidad / 10000000000}")
                    print(f"hm²: {cantidad / 100000000}")
                    print(f"dam²: {cantidad / 10000000}")
                    print(f"m²: {cantidad / 10000}")
                    print(f"dm²: {cantidad / 100}")
                    print(f"cm²: {cantidad}")
                    print(f"mm²: {cantidad * 100}")
                    print(f"mi²: {cantidad * 0.000000000386102}")
                    print(f"yd²: {cantidad * 0.00119599005}")
                    print(f"ft²: {cantidad * 0.0107639104}")
                    print(f"inch²: {cantidad * 1.5500031}")
                elif opcion_conv == "7":  # Milímetros cuadrados
                    print(f"\nKm²: {cantidad / 1000000000000}")
                    print(f"hm²: {cantidad / 10000000000}")
                    print(f"dam²: {cantidad / 1000000000}")
                    print(f"m²: {cantidad / 1000000}")
                    print(f"dm²: {cantidad / 10000}")
                    print(f"cm²: {cantidad / 100}")
                    print(f"mm²: {cantidad}")
                    print(f"mi²: {cantidad * 0.000000000000386102}")
                    print(f"yd²: {cantidad * 0.00000119599005}")
                    print(f"ft²: {cantidad * 0.0000107639104}")
                    print(f"inch²: {cantidad * 0.0015500031}")
                elif opcion_conv == "8":  # Millas cuadradas
                    print(f"\nKm²: {cantidad / 0.386102}")
                    print(f"hm²: {cantidad / 0.00386102}")
                    print(f"dam²: {cantidad / 0.0000386102}")
                    print(f"m²: {cantidad / 0.000000386102}")
                    print(f"dm²: {cantidad / 0.00000000386102}")
                    print(f"cm²: {cantidad / 0.0000000000386102}")
                    print(f"mm²: {cantidad / 0.000000000000386102}")
                    print(f"mi²: {cantidad}")
                    print(f"yd²: {cantidad * 3097600}")
                    print(f"ft²: {cantidad * 27878400}")
                    print(f"inch²: {cantidad * 4014489600}")
                elif opcion_conv == "9":  # Yardas cuadradas
                    print(f"\nKm²: {cantidad / 1195990.05}")
                    print(f"hm²: {cantidad / 11959.9005}")
                    print(f"dam²: {cantidad / 119.599005}")
                    print(f"m²: {cantidad / 1.19599005}")
                    print(f"dm²: {cantidad / 0.119599005}")
                    print(f"cm²: {cantidad / 0.00119599005}")
                    print(f"mm²: {cantidad / 0.0000119599005}")
                    print(f"mi²: {cantidad * 0.000000386102}")
                    print(f"yd²: {cantidad}")
                    print(f"ft²: {cantidad * 9}")
                    print(f"inch²: {cantidad * 1296}")
                elif opcion_conv == "10":  # Pies cuadrados
                    print(f"\nKm²: {cantidad / 10763910.4}")
                    print(f"hm²: {cantidad / 107639.104}")
                    print(f"dam²: {cantidad / 1076.39104}")
                    print(f"m²: {cantidad / 10.7639104}")
                    print(f"dm²: {cantidad / 1.07639104}")
                    print(f"cm²: {cantidad / 0.0107639104}")
                    print(f"mm²: {cantidad / 0.000107639104}")
                    print(f"mi²: {cantidad * 0.0000000386102}")
                    print(f"yd²: {cantidad / 9}")
                    print(f"ft²: {cantidad}")
                    print(f"inch²: {cantidad * 144}")
                elif opcion_conv == "11":  # Pulgadas cuadradas
                    print(f"\nKm²: {cantidad / 1550003100}")
                    print(f"hm²: {cantidad / 15500031}")
                    print(f"dam²: {cantidad / 155000.31}")
                    print(f"m²: {cantidad / 1550.0031}")
                    print(f"dm²: {cantidad / 155.00031}")
                    print(f"cm²: {cantidad / 1.5500031}")
                    print(f"mm²: {cantidad / 0.15500031}")
                    print(f"mi²: {cantidad * 0.000000000386102}")
                    print(f"yd²: {cantidad / 1296}")
                    print(f"ft²: {cantidad / 144}")
                    print(f"inch²: {cantidad}")
                else:
                    print("\nOpción inválida")
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
                if opcion_conv == "1":  # Kilómetros cúbicos
                    print(f"\nKm³: {cantidad}")
                    print(f"hm³: {cantidad * 1000}")
                    print(f"dam³: {cantidad * 1000000}")
                    print(f"m³: {cantidad * 1000000000}")
                    print(f"dm³: {cantidad * 1000000000000}")
                    print(f"cm³: {cantidad * 1000000000000000}")
                    print(f"mm³: {cantidad * 1000000000000000000}")
                    print(f"L: {cantidad * 1e+12}")
                    print(f"mi³: {cantidad * 0.239913}")
                    print(f"yd³: {cantidad * 1307950619}")
                    print(f"ft³: {cantidad * 35314666721}")
                    print(f"inch³: {cantidad * 6.10237e+13}")
                elif opcion_conv == "2":  # Hectómetros cúbicos
                    print(f"\nKm³: {cantidad / 1000}")
                    print(f"hm³: {cantidad}")
                    print(f"dam³: {cantidad * 1000}")
                    print(f"m³: {cantidad * 1000000}")
                    print(f"dm³: {cantidad * 1000000000}")
                    print(f"cm³: {cantidad * 1000000000000}")
                    print(f"mm³: {cantidad * 1000000000000000}")
                    print(f"L: {cantidad * 1e+9}")
                    print(f"mi³: {cantidad * 0.000239913}")
                    print(f"yd³: {cantidad * 1307950.619}")
                    print(f"ft³: {cantidad * 3531466.6721}")
                    print(f"inch³: {cantidad * 6.10237e+12}")
                elif opcion_conv == "3":  # Decámetros cúbicos
                    print(f"\nKm³: {cantidad / 1000000}")
                    print(f"hm³: {cantidad / 1000}")
                    print(f"dam³: {cantidad}")
                    print(f"m³: {cantidad * 1000}")
                    print(f"dm³: {cantidad * 1000000}")
                    print(f"cm³: {cantidad * 1000000000}")
                    print(f"mm³: {cantidad * 1000000000000}")
                    print(f"L: {cantidad * 1000000}")
                    print(f"mi³: {cantidad * 2.39913e-7}")
                    print(f"yd³: {cantidad * 1307.950619}")
                    print(f"ft³: {cantidad * 3531.4666721}")
                    print(f"inch³: {cantidad * 6.10237e+9}")
                elif opcion_conv == "4":  # Metros cúbicos
                    print(f"\nKm³: {cantidad / 1000000000}")
                    print(f"hm³: {cantidad / 1000000}")
                    print(f"dam³: {cantidad / 1000}")
                    print(f"m³: {cantidad}")
                    print(f"dm³: {cantidad * 1000}")
                    print(f"cm³: {cantidad * 1000000}")
                    print(f"mm³: {cantidad * 1000000000}")
                    print(f"L: {cantidad * 1000}")
                    print(f"mi³: {cantidad * 2.39913e-10}")
                    print(f"yd³: {cantidad * 1.307950619}")
                    print(f"ft³: {cantidad * 35.314666721}")
                    print(f"inch³: {cantidad * 6.10237e+8}")
                elif opcion_conv == "5":  # Decímetros cúbicos
                    print(f"\nKm³: {cantidad / 1000000000000}")
                    print(f"hm³: {cantidad / 1000000000}")
                    print(f"dam³: {cantidad / 1000000}")
                    print(f"m³: {cantidad / 1000}")
                    print(f"dm³: {cantidad}")
                    print(f"cm³: {cantidad * 1000}")
                    print(f"mm³: {cantidad * 1000000}")
                    print(f"L: {cantidad}")
                    print(f"mi³: {cantidad * 2.39913e-13}")
                    print(f"yd³: {cantidad * 0.001307950619}")
                    print(f"ft³: {cantidad * 0.035314666721}")
                    print(f"inch³: {cantidad * 61.0237}")
                elif opcion_conv == "6":  # Centímetros cúbicos
                    print(f"\nKm³: {cantidad / 1000000000000000}")
                    print(f"hm³: {cantidad / 1000000000000}")
                    print(f"dam³: {cantidad / 1000000000}")
                    print(f"m³: {cantidad / 1000000}")
                    print(f"dm³: {cantidad / 1000}")
                    print(f"cm³: {cantidad}")
                    print(f"mm³: {cantidad * 1000}")
                    print(f"L: {cantidad / 1000}")
                    print(f"mi³: {cantidad * 2.39913e-16}")
                    print(f"yd³: {cantidad * 1.307950619e-6}")
                    print(f"ft³: {cantidad * 3.5314666721e-5}")
                    print(f"inch³: {cantidad * 0.0610237}")
                elif opcion_conv == "7":  # Milímetros cúbicos
                    print(f"\nKm³: {cantidad / 1000000000000000000}")
                    print(f"hm³: {cantidad / 1000000000000000}")
                    print(f"dam³: {cantidad / 1000000000000}")
                    print(f"m³: {cantidad / 1000000000}")
                    print(f"dm³: {cantidad / 1000000}")
                    print(f"cm³: {cantidad / 1000}")
                    print(f"mm³: {cantidad}")
                    print(f"L: {cantidad / 1000000}")
                    print(f"mi³: {cantidad * 2.39913e-19}")
                    print(f"yd³: {cantidad * 1.307950619e-9}")
                    print(f"ft³: {cantidad * 3.5314666721e-8}")
                    print(f"inch³: {cantidad * 6.10237e-5}")
                elif opcion_conv == "8":  # Litros
                    print(f"\nKm³: {cantidad / 1e+12}")
                    print(f"hm³: {cantidad / 1e+9}")
                    print(f"dam³: {cantidad / 1000000}")
                    print(f"m³: {cantidad / 1000}")
                    print(f"dm³: {cantidad}")
                    print(f"cm³: {cantidad * 1000}")
                    print(f"mm³: {cantidad * 1000000}")
                    print(f"L: {cantidad}")
                    print(f"mi³: {cantidad * 2.39913e-13}")
                    print(f"yd³: {cantidad * 0.001307950619}")
                    print(f"ft³: {cantidad * 0.035314666721}")
                    print(f"inch³: {cantidad * 61.0237}")
                elif opcion_conv == "9":  # Millas cúbicas
                    print(f"\nKm³: {cantidad / 0.239913}")
                    print(f"hm³: {cantidad / 0.000239913}")
                    print(f"dam³: {cantidad / 2.39913e-7}")
                    print(f"m³: {cantidad / 2.39913e-10}")
                    print(f"dm³: {cantidad / 2.39913e-13}")
                    print(f"cm³: {cantidad / 2.39913e-16}")
                    print(f"mm³: {cantidad / 2.39913e-19}")
                    print(f"L: {cantidad / 2.39913e-13}")
                    print(f"mi³: {cantidad}")
                    print(f"yd³: {cantidad * 5451776000}")
                    print(f"ft³: {cantidad * 147197952000}")
                    print(f"inch³: {cantidad * 2.54358e+14}")
                elif opcion_conv == "10":  # Yardas cúbicas
                    print(f"\nKm³: {cantidad / 1307950619}")
                    print(f"hm³: {cantidad / 1307950.619}")
                    print(f"dam³: {cantidad / 1307.950619}")
                    print(f"m³: {cantidad / 1.307950619}")
                    print(f"dm³: {cantidad / 0.001307950619}")
                    print(f"cm³: {cantidad / 1.307950619e-6}")
                    print(f"mm³: {cantidad / 1.307950619e-9}")
                    print(f"L: {cantidad / 0.001307950619}")
                    print(f"mi³: {cantidad * 1.83438e-10}")
                    print(f"yd³: {cantidad}")
                    print(f"ft³: {cantidad * 27}")
                    print(f"inch³: {cantidad * 46656}")
                elif opcion_conv == "11":  # Pies cúbicos
                    print(f"\nKm³: {cantidad / 35314666721}")
                    print(f"hm³: {cantidad / 3531466.6721}")
                    print(f"dam³: {cantidad / 3531.4666721}")
                    print(f"m³: {cantidad / 35.314666721}")
                    print(f"dm³: {cantidad / 0.035314666721}")
                    print(f"cm³: {cantidad / 3.5314666721e-5}")
                    print(f"mm³: {cantidad / 3.5314666721e-8}")
                    print(f"L: {cantidad / 0.035314666721}")
                    print(f"mi³: {cantidad * 6.7942e-12}")
                    print(f"yd³: {cantidad / 27}")
                    print(f"ft³: {cantidad}")
                    print(f"inch³: {cantidad * 1728}")
                elif opcion_conv == "12":  # Pulgadas cúbicas
                    print(f"\nKm³: {cantidad / 6.10237e+13}")
                    print(f"hm³: {cantidad / 6.10237e+12}")
                    print(f"dam³: {cantidad / 6.10237e+9}")
                    print(f"m³: {cantidad / 6.10237e+8}")
                    print(f"dm³: {cantidad / 61.0237}")
                    print(f"cm³: {cantidad / 0.0610237}")
                    print(f"mm³: {cantidad / 6.10237e-5}")
                    print(f"L: {cantidad / 61.0237}")
                    print(f"mi³: {cantidad * 3.9317e-15}")
                    print(f"yd³: {cantidad / 46656}")
                    print(f"ft³: {cantidad / 1728}")
                    print(f"inch³: {cantidad}")
                else:
                    print("\nOpción inválida")
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
                if opcion_conv == "1":  # Kilogramo
                    print(f"\nkg: {cantidad}")
                    print(f"hg: {cantidad * 10}")
                    print(f"dag: {cantidad * 100}")
                    print(f"g: {cantidad * 1000}")
                    print(f"dg: {cantidad * 10000}")
                    print(f"cg: {cantidad * 100000}")
                    print(f"mg: {cantidad * 1000000}")
                    print(f"ton: {cantidad / 1000}")
                    print(f"lb: {cantidad * 2.20462}")
                    print(f"oz: {cantidad * 35.274}")
                elif opcion_conv == "2":  # Hectogramo
                    print(f"\nkg: {cantidad / 10}")
                    print(f"hg: {cantidad}")
                    print(f"dag: {cantidad * 10}")
                    print(f"g: {cantidad * 100}")
                    print(f"dg: {cantidad * 1000}")
                    print(f"cg: {cantidad * 10000}")
                    print(f"mg: {cantidad * 100000}")
                    print(f"ton: {cantidad / 10000}")
                    print(f"lb: {cantidad * 0.220462}")
                    print(f"oz: {cantidad * 3.5274}")
                elif opcion_conv == "3":  # Decagramo
                    print(f"\nkg: {cantidad / 100}")
                    print(f"hg: {cantidad / 10}")
                    print(f"dag: {cantidad}")
                    print(f"g: {cantidad * 10}")
                    print(f"dg: {cantidad * 100}")
                    print(f"cg: {cantidad * 1000}")
                    print(f"mg: {cantidad * 10000}")
                    print(f"ton: {cantidad / 100000}")
                    print(f"lb: {cantidad * 0.0220462}")
                    print(f"oz: {cantidad * 0.35274}")
                elif opcion_conv == "4":  # Gramo
                    print(f"\nkg: {cantidad / 1000}")
                    print(f"hg: {cantidad / 100}")
                    print(f"dag: {cantidad / 10}")
                    print(f"g: {cantidad}")
                    print(f"dg: {cantidad * 10}")
                    print(f"cg: {cantidad * 100}")
                    print(f"mg: {cantidad * 1000}")
                    print(f"ton: {cantidad / 1000000}")
                    print(f"lb: {cantidad * 0.00220462}")
                    print(f"oz: {cantidad * 0.035274}")
                elif opcion_conv == "5":  # Decigramo
                    print(f"\nkg: {cantidad / 10000}")
                    print(f"hg: {cantidad / 1000}")
                    print(f"dag: {cantidad / 100}")
                    print(f"g: {cantidad / 10}")
                    print(f"dg: {cantidad}")
                    print(f"cg: {cantidad * 10}")
                    print(f"mg: {cantidad * 100}")
                    print(f"ton: {cantidad / 10000000}")
                    print(f"lb: {cantidad * 0.000220462}")
                    print(f"oz: {cantidad * 0.0035274}")
                elif opcion_conv == "6":  # Centigramo
                    print(f"\nkg: {cantidad / 100000}")
                    print(f"hg: {cantidad / 10000}")
                    print(f"dag: {cantidad / 1000}")
                    print(f"g: {cantidad / 100}")
                    print(f"dg: {cantidad / 10}")
                    print(f"cg: {cantidad}")
                    print(f"mg: {cantidad * 10}")
                    print(f"ton: {cantidad / 100000000}")
                    print(f"lb: {cantidad * 0.0000220462}")
                    print(f"oz: {cantidad * 0.00035274}")
                elif opcion_conv == "7":  # Miligramo
                    print(f"\nkg: {cantidad / 1000000}")
                    print(f"hg: {cantidad / 100000}")
                    print(f"dag: {cantidad / 10000}")
                    print(f"g: {cantidad / 1000}")
                    print(f"dg: {cantidad / 100}")
                    print(f"cg: {cantidad / 10}")
                    print(f"mg: {cantidad}")
                    print(f"ton: {cantidad / 1000000000}")
                    print(f"lb: {cantidad * 0.00000220462}")
                    print(f"oz: {cantidad * 0.000035274}")
                elif opcion_conv == "8":  # Tonelada
                    print(f"\nkg: {cantidad * 1000}")
                    print(f"hg: {cantidad * 10000}")
                    print(f"dag: {cantidad * 100000}")
                    print(f"g: {cantidad * 1000000}")
                    print(f"dg: {cantidad * 10000000}")
                    print(f"cg: {cantidad * 100000000}")
                    print(f"mg: {cantidad * 1000000000}")
                    print(f"ton: {cantidad}")
                    print(f"lb: {cantidad * 2204.62}")
                    print(f"oz: {cantidad * 35274}")
                elif opcion_conv == "9":  # Libra
                    print(f"\nkg: {cantidad / 2.20462}")
                    print(f"hg: {cantidad / 0.220462}")
                    print(f"dag: {cantidad / 0.0220462}")
                    print(f"g: {cantidad / 0.00220462}")
                    print(f"dg: {cantidad / 0.000220462}")
                    print(f"cg: {cantidad / 0.0000220462}")
                    print(f"mg: {cantidad / 0.00000220462}")
                    print(f"ton: {cantidad / 2204.62}")
                    print(f"lb: {cantidad}")
                    print(f"oz: {cantidad * 16}")
                elif opcion_conv == "10":  # Onza
                    print(f"\nkg: {cantidad / 35.274}")
                    print(f"hg: {cantidad / 3.5274}")
                    print(f"dag: {cantidad / 0.35274}")
                    print(f"g: {cantidad / 0.035274}")
                    print(f"dg: {cantidad / 0.0035274}")
                    print(f"cg: {cantidad / 0.00035274}")
                    print(f"mg: {cantidad / 0.000035274}")
                    print(f"ton: {cantidad / 35274}")
                    print(f"lb: {cantidad / 16}")
                    print(f"oz: {cantidad}")
                else:
                    print("\nOpción inválida")
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
                if opcion_conv == "1":  # Celsius
                    print(f"\nCelsius: {cantidad}")
                    print(f"Fahrenheit: {(cantidad * 9/5) + 32}")
                    print(f"Kelvin: {cantidad + 273.15}")
                elif opcion_conv == "2":  # Fahrenheit
                    print(f"\nCelsius: {(cantidad - 32) * 5/9}")
                    print(f"Fahrenheit: {cantidad}")
                    print(f"Kelvin: {(cantidad - 32) * 5/9 + 273.15}")
                elif opcion_conv == "3":  # Kelvin
                    print(f"\nCelsius: {cantidad - 273.15}")
                    print(f"Fahrenheit: {(cantidad - 273.15) * 9/5 + 32}")
                    print(f"Kelvin: {cantidad}")
                else:
                    print("\nOpción inválida")
            except ValueError:
                print("\nIngrese una cantidad válida")

        case "18":
            print("\n--- Conversión Tiempo ---")
            print("1. Día")
            print("2. Hora")
            print("3. Minuto")
            print("3. Segundo\n")
            opcion_conv = input("Ingrese una opción: ")
            try:
                cantidad = float(input("Ingrese la cantidad: "))
                if opcion_conv == "1":  # Día
                    print(f"\nDía: {cantidad}")
                    print(f"Hora: {cantidad * 24}")
                    print(f"Minuto: {cantidad * 1440}")
                    print(f"Segundo: {cantidad * 86400}")
                elif opcion_conv == "2":  # Hora
                    print(f"\nDía: {cantidad / 24}")
                    print(f"Hora: {cantidad}")
                    print(f"Minuto: {cantidad * 60}")
                    print(f"Segundo: {cantidad * 3600}")
                elif opcion_conv == "3":  # Minuto
                    print(f"\nDía: {cantidad / 1440}")
                    print(f"Hora: {cantidad / 60}")
                    print(f"Minuto: {cantidad}")
                    print(f"Segundo: {cantidad * 60}")
                elif opcion_conv == "4":  # Segundo
                    print(f"\nDía: {cantidad / 86400}")
                    print(f"Hora: {cantidad / 3600}")
                    print(f"Minuto: {cantidad / 60}")
                    print(f"Segundo: {cantidad}")
                else:
                    print("\nOpción inválida")
            except ValueError:
                print("\nIngrese una cantidad válida")

        case "19":
            os.system("cls")

        case "20":
            os.system("cls")
            flag = False

        case _:
            print("Opción no válida")

    if opcion != "19" and opcion != "20":
        continuar = input("\n¿Desea realizar otra operación? (s/n): ")
        if continuar.lower() == "n":
            flag = False
            os.system("cls")
