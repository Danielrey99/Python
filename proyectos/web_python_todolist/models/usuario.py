"""Módulo que define la clase Lista."""

import psycopg2
from database.db import create_connection

class Usuario:
    """Clase para manejar usuarios"""

    def __init__(self, id=None, nombre_usuario=None, contraseña=None, rol='usuario', fecha_registro=None):
        self.id = id
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.rol = rol
        self.fecha_registro = fecha_registro

    @staticmethod
    def crear(nombre_usuario, contraseña, rol='usuario'):
        """Crea un nuevo usuario."""
        conn = create_connection()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute("INSERT INTO usuarios (nombre_usuario, contraseña, rol) VALUES (%s, %s, %s) RETURNING id", (nombre_usuario, contraseña, rol))
                usuario_id = cur.fetchone()[0]
                conn.commit()
                return usuario_id
            except psycopg2.Error as e:
                print(f"Error al crear usuario: {e}")
                return None
            finally:
                if conn:
                    cur.close()
                    conn.close()

    @staticmethod
    def obtener_por_nombre_usuario(nombre_usuario):
        """Obtiene un usuario por su nombre de usuario."""
        conn = create_connection()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute("SELECT id, nombre_usuario, contraseña, rol, fecha_registro FROM usuarios WHERE nombre_usuario = %s", (nombre_usuario,))
                usuario = cur.fetchone()
                if usuario:
                    return Usuario(*usuario)
                else:
                    return None
            except psycopg2.Error as e:
                print(f"Error al obtener usuario: {e}")
                return None
            finally:
                if conn:
                    cur.close()
                    conn.close()

    @staticmethod
    def obtener_por_id(usuario_id):
        """Obtiene un usuario por su ID."""
        conn = create_connection()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute("SELECT id, nombre_usuario, contraseña, rol, fecha_registro FROM usuarios WHERE id = %s", (usuario_id,))
                usuario = cur.fetchone()
                if usuario:
                    return Usuario(*usuario)
                else:
                    return None
            except psycopg2.Error as e:
                print(f"Error al obtener usuario: {e}")
                return None
            finally:
                if conn:
                    cur.close()
                    conn.close()
