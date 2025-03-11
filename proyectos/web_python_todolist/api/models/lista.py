"""Módulo que define la clase Lista para la API."""

class Lista:
    """Clase para manejar listas en la API."""

    def __init__(self, id=None, nombre_lista=None, descripcion=None, fecha_creacion=None):
        """Inicializa una instancia de la clase Lista."""
        self.id = id
        self.nombre_lista = nombre_lista
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion
