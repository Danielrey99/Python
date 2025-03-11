"""Módulo que define la clase Usuario para la API."""

class Usuario:
    """Clase para manejar usuarios en la API."""

    def __init__(self, id=None, nombre_usuario=None, contrasenha=None, rol='usuario', fecha_registro=None):
        self.id = id
        self.nombre_usuario = nombre_usuario
        self.contrasenha = contrasenha
        self.rol = rol
        self.fecha_registro = fecha_registro

    def to_dict(self):
        """
        Convierte la instancia de Usuario a un diccionario que se puede serializar fácilmente a JSON.
        'fecha_registro' formateada como cadena ISO 8601
        """
        return {
            "id": self.id,
            "nombre_usuario": self.nombre_usuario,
            "rol": self.rol,
            "fecha_registro": self.fecha_registro.isoformat() if self.fecha_registro else None,
        }
