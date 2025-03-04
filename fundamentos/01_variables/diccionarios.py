"""
Este módulo muestra ejemplos básicos de diccionarios en Python.
"""

print("\n-- Diccionarios --\n")

# Crear un diccionario
persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid"
}

# Acceder a valores por clave
print(persona["nombre"])  # Salida: Juan
print(persona["edad"])    # Salida: 25
print(persona["ciudad"])  # Salida: Madrid

# Modificar un valor
persona["edad"] = 26
print(persona["edad"])    # Salida: 26

# Agregar un nuevo par clave-valor
persona["profesion"] = "Ingeniero"
print(persona)  # Salida: {'nombre': 'Juan', 'edad': 26, 'ciudad': 'Madrid', 'profesion': 'Ingeniero'}

# Métodos comunes de diccionarios

# 1. keys(): Obtener todas las claves
print("\n-- keys() --")
claves = persona.keys()
print(claves)  # Salida: dict_keys(['nombre', 'edad', 'ciudad', 'profesion'])

# 2. values(): Obtener todos los valores
print("\n-- values() --")
valores = persona.values()
print(valores)  # Salida: dict_values(['Juan', 26, 'Madrid', 'Ingeniero'])

# 3. items(): Obtener todos los pares clave-valor
print("\n-- items() --")
items = persona.items()
print(items)  # Salida: dict_items([('nombre', 'Juan'), ('edad', 26), ('ciudad', 'Madrid'), ('profesion', 'Ingeniero')])

# 4. get(): Obtener el valor de una clave (con valor predeterminado si la clave no existe)
print("\n-- get() --")
nombre = persona.get("nombre", "Desconocido")
print(nombre)  # Salida: Juan

profesion = persona.get("profesion", "Desconocido")
print(profesion)  # Salida: Ingeniero

telefono = persona.get("telefono", "No disponible")
print(telefono)  # Salida: No disponible

# 5. pop(): Eliminar y devolver el valor de una clave
print("\n-- pop() --")
edad = persona.pop("edad")
print(edad)  # Salida: 26
print(persona)  # Salida: {'nombre': 'Juan', 'ciudad': 'Madrid', 'profesion': 'Ingeniero'}

# 6. popitem(): Eliminar y devolver el último par clave-valor insertado
print("\n-- popitem() --")
ultimo_item = persona.popitem()
print(ultimo_item)  # Salida: ('profesion', 'Ingeniero')
print(persona)  # Salida: {'nombre': 'Juan', 'ciudad': 'Madrid'}

# 7. update(): Actualizar el diccionario con pares clave-valor de otro diccionario
print("\n-- update() --")
persona.update({"edad": 27, "telefono": "123456789"})
print(persona)  # Salida: {'nombre': 'Juan', 'ciudad': 'Madrid', 'edad': 27, 'telefono': '123456789'}

# 8. clear(): Eliminar todos los elementos del diccionario
print("\n-- clear() --")
persona.clear()
print(persona)  # Salida: {}

# 9. Verificar si una clave existe en el diccionario
print("\n-- Verificar existencia de clave --")
persona = {"nombre": "Ana", "edad": 30}
if "nombre" in persona:
    print("La clave 'nombre' existe")  # Salida: La clave 'nombre' existe

if "profesion" not in persona:
    print("La clave 'profesion' no existe")  # Salida: La clave 'profesion' no existe

# 10. Recorrer un diccionario con un bucle for
print("\n-- Recorrer diccionario --")
persona = {"nombre": "Carlos", "edad": 35, "ciudad": "Barcelona"}

# Recorrer claves
print("Recorrer claves:")
for clave in persona:
    print(clave)  # Salida: nombre, edad, ciudad

# Recorrer valores
print("\nRecorrer valores:")
for valor in persona.values():
    print(valor)  # Salida: Carlos, 35, Barcelona

# Recorrer pares clave-valor
print("\nRecorrer pares clave-valor:")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
# Salida:
# nombre: Carlos
# edad: 35
# ciudad: Barcelona

# 11. Diccionarios anidados
print("\n-- Diccionarios anidados --")
estudiantes = {
    "Juan": {
        "edad": 20,
        "curso": "Matemáticas"
    },
    "Ana": {
        "edad": 22,
        "curso": "Física"
    }
}

# Acceder a valores en diccionarios anidados
print(estudiantes["Juan"]["edad"])  # Salida: 20
print(estudiantes["Ana"]["curso"])  # Salida: Física

# 12. Copiar un diccionario
print("\n-- Copiar diccionario --")
copia_persona = persona.copy()
print(copia_persona)  # Salida: {'nombre': 'Carlos', 'edad': 35, 'ciudad': 'Barcelona'}

# 13. Crear un diccionario con fromkeys()
print("\n-- fromkeys() --")
claves = ["nombre", "edad", "ciudad"]
valores_predeterminados = None
nuevo_diccionario = dict.fromkeys(claves, valores_predeterminados)
print(nuevo_diccionario)  # Salida: {'nombre': None, 'edad': None, 'ciudad': None}