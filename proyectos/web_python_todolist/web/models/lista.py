"""Módulo que define la clase Lista para la Web."""

class Lista:
    """Clase para manejar listas en la Web."""

    def __init__(self, id, nombre_lista, descripcion, usuario_id, fecha_creacion=None):
        self.id = id
        self.nombre_lista = nombre_lista
        self.descripcion = descripcion
        self.usuario_id = usuario_id
        self.fecha_creacion = fecha_creacion
