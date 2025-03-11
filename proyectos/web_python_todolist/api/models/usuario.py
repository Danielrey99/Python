"""Módulo que define la clase Usuario para la API."""

class Usuario:
    """Clase para manejar usuarios en la API."""

    def __init__(self, id=None, nombre_usuario=None, contrasenha=None, rol='usuario', fecha_registro=None):
        self.id = id
        self.nombre_usuario = nombre_usuario
        self.contrasenha = contrasenha
        self.rol = rol
        self.fecha_registro = fecha_registro
