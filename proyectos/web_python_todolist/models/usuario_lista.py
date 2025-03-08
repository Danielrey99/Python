"""Módulo que define la clase UsuarioLista."""

import psycopg2
from database.db import create_connection
from .lista import Lista

class UsuarioLista:
    """Clase que representa la asociación entre usuarios y listas."""

    def __init__(self, usuario_id, lista_id):
        self.usuario_id = usuario_id
        self.lista_id = lista_id

    @staticmethod
    def crear(usuario_id, lista_id):
        """Asocia un usuario a una lista."""
        conn = create_connection()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute("INSERT INTO usuario_lista (usuario_id, lista_id) VALUES (%s, %s)", (usuario_id, lista_id))
                conn.commit()
                return True
            except psycopg2.Error as e:
                print(f"Error al asociar usuario y lista: {e}")
                return False
            finally:
                if conn:
                    cur.close()
                    conn.close()

    @staticmethod
    def obtener_listas_por_usuario_id(usuario_id):
        """Obtiene las listas asociadas a un usuario."""
        conn = create_connection()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute("""
                    SELECT listas.id, listas.nombre_lista, listas.descripcion, listas.usuario_id, listas.fecha_creacion
                    FROM listas
                    JOIN usuario_lista ON listas.id = usuario_lista.lista_id
                    WHERE usuario_lista.usuario_id = %s
                """, (usuario_id,))
                listas = [Lista(*lista) for lista in cur.fetchall()]
                return listas
            except psycopg2.Error as e:
                print(f"Error al obtener listas asociadas: {e}")
                return None
            finally:
                if conn:
                    cur.close()
                    conn.close()
