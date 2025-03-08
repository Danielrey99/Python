"""Módulo que define la clase Lista."""

import psycopg2
from database.db import create_connection

class Lista:
    """Clase para manejar usuarios"""

    def __init__(self, id=None, nombre_lista=None, descripcion=None, usuario_id=None, fecha_creacion=None):
        """Inicializa una instancia de la clase Lista."""
        self.id = id
        self.nombre_lista = nombre_lista
        self.descripcion = descripcion
        self.usuario_id = usuario_id
        self.fecha_creacion = fecha_creacion

    @staticmethod
    def crear(nombre_lista, descripcion, usuario_id):
        """Crea una nueva lista."""
        conn = create_connection()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute("INSERT INTO listas (nombre_lista, descripcion, usuario_id) VALUES (%s, %s, %s) RETURNING id", (nombre_lista, descripcion, usuario_id))
                lista_id = cur.fetchone()[0]
                conn.commit()
                return lista_id
            except psycopg2.Error as e:
                print(f"Error al crear lista: {e}")
                return None
            finally:
                if conn:
                    cur.close()
                    conn.close()

    @staticmethod
    def obtener_por_usuario_id(usuario_id):
        """Obtiene todas las listas de un usuario."""
        conn = create_connection()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute("SELECT id, nombre_lista, descripcion, usuario_id, fecha_creacion FROM listas WHERE usuario_id = %s", (usuario_id,))
                listas = [Lista(*lista) for lista in cur.fetchall()]
                return listas
            except psycopg2.Error as e:
                print(f"Error al obtener listas: {e}")
                return None
            finally:
                if conn:
                    cur.close()
                    conn.close()
