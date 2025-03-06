"""
Este módulo muestra ejemplos básicos de clases y objetos en Python.
"""

from abc import ABC, abstractmethod

# 1. Definición básica de una clase
print("\n-- DEFINICIÓN BÁSICA DE UNA CLASE --\n")

class Persona:
    # Constructor (método especial __init__)
    def __init__(self, nombre, edad): # El constructor inicializa los atributos de la clase
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad      # Atributo de instancia

    # Método de instancia
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

# Instancia de la clase Persona
persona1 = Persona("Juan", 25)
persona1.mostrar_info()  # Llamar al método para mostrar la información

# 2. Atributos de clase y de instancia
print("\n-- ATRIBUTOS DE CLASE Y DE INSTANCIA --\n")

class Coche:
    # Atributo de clase (compartido por todas las instancias)
    ruedas = 4

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ruedas: {self.ruedas}")

# Instancias de la clase Coche
coche1 = Coche("Toyota", "Corolla")
coche2 = Coche("Ford", "Mustang")

coche1.mostrar_info()
coche2.mostrar_info()

# Cambiar un atributo de clase
Coche.ruedas = 6
print("\nDespués de cambiar el atributo de clase:")
coche1.mostrar_info()
coche2.mostrar_info()

# 3. Herencia
print("\n-- HERENCIA --\n")

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

# Método que debe ser implementado por las subclases
    def hacer_sonido(self):
        raise NotImplementedError("Las subclases deben implementar este método.")

# Perro hereda de Animal
class Perro(Animal):

# Implementación del método para hacer sonido.
    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Guau!")

class Gato(Animal):

    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Miau!")

# Instancias de las clases derivadas
perro = Perro("Rex")
gato = Gato("Mimi")

perro.hacer_sonido()
gato.hacer_sonido()

# 4. Composicion
print("\n-- COMPOSICION --\n")
class Motor:
    def encender(self):
        print("Motor encendido.")

class Vehiculo:
    def __init__(self):
        self.motor = Motor()  # Composición

    def encender(self):
        self.motor.encender()

vehiculo = Vehiculo()
vehiculo.encender()  # Motor encendido.

# 5. Métodos especiales (Dunder methods)
print("\n-- MÉTODOS ESPECIALES (DUNDER METHODS) --\n")
print("Coordenada")

class Coordenada:
    def __init__(self, x, y):

        self.x = x
        self.y = y

    # Método especial para representar el objeto como string
    def __str__(self):
        return f"Coordenada({self.x}, {self.y})"

    # Método especial para sumar dos coordenadas
    def __add__(self, otro):
        return Coordenada(self.x + otro.x, self.y + otro.y)

    # Método especial para comparar dos coordenadas
    def __eq__(self, otro):
        return self.x == otro.x and self.y == otro.y

# Crear instancias de la clase Coordenada
coordenada1 = Coordenada(1, 2)
coordenada2 = Coordenada(3, 4)

print(coordenada1)
print(coordenada2)

coordenada3 = coordenada1 + coordenada2  # Usa el método __add__
print(coordenada3)

print(coordenada1 == coordenada2)  # False (usa el método __eq__)

print("\nMiLista")
class MiLista:
    def __init__(self, elementos):
        self.elementos = elementos

    def __len__(self):
        return len(self.elementos)

    def __getitem__(self, indice):
        return self.elementos[indice]

    def __setitem__(self, indice, valor):
        self.elementos[indice] = valor

lista = MiLista([1, 2, 3])
print(len(lista))  # 3
print(lista[1])    # 2
lista[1] = 99
print(lista[1])    # 99

# 6. Métodos estáticos y de clase
print("\n-- MÉTODOS ESTÁTICOS Y DE CLASE --\n")

class Matematica:

    # Método estático (no necesita acceso a la instancia o la clase)
    @staticmethod
    def sumar(a, b):
        return a + b

    # Método de clase (tiene acceso a la clase pero no a la instancia)
    @classmethod
    def describir(cls):
        return f"Esta es la clase {cls.__name__}"

print(Matematica.sumar(5, 3))  # 8
print(Matematica.describir())  # Esta es la clase Matematica

# 7. Encapsulamiento (atributos privados)
print("\n-- 6. ENCAPSULAMIENTO (ATRIBUTOS PRIVADOS) --\n")

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado (no se puede acceder directamente)

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

    def obtener_saldo(self):
        return self.__saldo

# Instancia de la clase CuentaBancaria
cuenta = CuentaBancaria("Ana", 1000)

cuenta.depositar(500)
print(f"Saldo actual: {cuenta.obtener_saldo()}")  # Saldo actual: 1500

# Intentar acceder al atributo privado (generará un error)
# print(cuenta.__saldo)  # AttributeError: 'CuentaBancaria' object has no attribute '__saldo'

# 8. Polimorfismo
print("\n-- POLIMORFISMO --\n")

class Figura:

    def area(self):
        raise NotImplementedError("Las subclases deben implementar este método.")

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * (self.radio ** 2)

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

# Instancias de las clases derivadas
cuadrado = Cuadrado(5)
circulo = Circulo(3)
triangulo = Triangulo(4, 6)

# Calcular el área de cada figura
print(f"Área del cuadrado: {cuadrado.area()}")
print(f"Área del círculo: {circulo.area()}")
print(f"Área del triángulo: {triangulo.area()}")

# Demostración del polimorfismo
figuras = [cuadrado, circulo, triangulo]

for figura in figuras:
    print(f"Área de la figura: {figura.area()}")

# 9. Getters y Setters
print("\n-- GETTERS Y SETTERS --\n")
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre  # Atributo público
        self.__precio = precio  # Atributo privado

    # Getter para el precio
    @property
    def precio(self):
        return self.__precio

    # Setter para el precio
    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self.__precio = nuevo_precio
        else:
            raise ValueError("El precio no puede ser negativo.")

    # Método para mostrar la información del producto
    def mostrar_info(self):
        print(f"Producto: {self.nombre}, Precio: ${self.__precio:.2f}")

# Instancia de la clase Producto
producto1 = Producto("Laptop", 1200.50)

# Acceder al precio usando el getter
print(f"Precio actual: ${producto1.precio:.2f}")

# Modificar el precio usando el setter
producto1.precio = 1100.75  # Cambia el precio
print(f"Nuevo precio: ${producto1.precio:.2f}")

# Intentar asignar un precio negativo (generará un error)
try:
    producto1.precio = -500
except ValueError as e:
    print(e)

# Mostrar la información del producto
producto1.mostrar_info()

# 10. Clase abstracta
print("\n-- CLASE ABSTRACTA --\n")

class DispositivoElectronico(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # Método abstracto que debe ser implementado por las subclases
    @abstractmethod
    def mostrar_info(self):
        pass

    # Método concreto (no abstracto)
    def encender(self):
        print(f"{self.marca} {self.modelo} está encendido.")

# Subclase
class TelefonoMovil(DispositivoElectronico):
    def __init__(self, marca, modelo, sistema_operativo):
        super().__init__(marca, modelo)
        self.sistema_operativo = sistema_operativo

    # Implementación del método abstracto
    def mostrar_info(self):
        print(f"Teléfono Móvil: {self.marca} {self.modelo}, SO: {self.sistema_operativo}")

# Subclase
class Laptop(DispositivoElectronico):
    def __init__(self, marca, modelo, ram):
        super().__init__(marca, modelo)
        self.ram = ram

    # Implementación del método abstracto
    def mostrar_info(self):
        print(f"Laptop: {self.marca} {self.modelo}, RAM: {self.ram} GB")

# Subclase
class Tablet(DispositivoElectronico):
    def __init__(self, marca, modelo, tamaño_pantalla):
        super().__init__(marca, modelo)
        self.tamaño_pantalla = tamaño_pantalla

    # Implementación del método abstracto
    def mostrar_info(self):
        print(f"Tablet: {self.marca} {self.modelo}, Pantalla: {self.tamaño_pantalla} pulgadas")

# Instancias de las subclases
telefono = TelefonoMovil("Samsung", "Galaxy S21", "Android")
laptop = Laptop("Dell", "XPS 13", 16)
tablet = Tablet("Apple", "iPad Pro", 12.9)

# Llamar a los métodos
telefono.mostrar_info()
laptop.mostrar_info()
tablet.mostrar_info()

# Llamar a un método concreto heredado de la clase abstracta
telefono.encender()
laptop.encender()
tablet.encender()

# Crear una instancia de la clase abstracta (generará un error)
#try:
#    dispositivo = DispositivoElectronico("Marca", "Modelo")
#except TypeError as e:
#    print(e)
