"""
Este módulo muestra ejemplos básicos de constantes en Python.
"""

# Constantes
print("\n-- CONSTANTES --\n")
PI = 3.1416
GRAVEDAD_TIERRA = 9.81  # m/s²
VELOCIDAD_LUZ = 299792458  # m/s

radio = 5
area_circulo = PI * (radio ** 2)
print(f"Área del círculo: {area_circulo:.2f}")

masa = 70
fuerza_peso = masa * GRAVEDAD_TIERRA
print(f"Fuerza peso en la Tierra: {fuerza_peso} N")
