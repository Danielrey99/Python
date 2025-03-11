"""Módulo que define la clase Usuario para la Web."""

class Usuario:
    """Clase para manejar usuarios en la Web."""

    def __init__(self, id, nombre_usuario, rol, fecha_registro=None):
        self.id = id
        self.nombre_usuario = nombre_usuario
        self.rol = rol
        self.fecha_registro = fecha_registro
