"""Módulo para la lógica de negocio de la API."""

import psycopg2
from api.models.usuario import Usuario
from api.models.lista import Lista
from api.database.db import create_connection

def crear_usuario(nombre_usuario, contrasenha):
    """Crea un nuevo usuario en la base de datos."""
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO usuarios (nombre_usuario, contrasenha, rol) VALUES (%s, %s, %s) RETURNING id", (nombre_usuario, contrasenha, 'usuario'))
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

def obtener_usuario_por_nombre(nombre_usuario):
    """Obtiene un usuario por su nombre de usuario desde la base de datos."""
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT id, nombre_usuario, contrasenha, rol, fecha_registro FROM usuarios WHERE nombre_usuario = %s", (nombre_usuario,))
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

def obtener_usuario_por_id(usuario_id):
    """Obtiene un usuario por su ID desde la base de datos."""
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT id, nombre_usuario, contrasenha, rol, fecha_registro FROM usuarios WHERE id = %s", (usuario_id,))
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

def crear_lista(nombre_lista, descripcion, usuario_id):
    """Crea una nueva lista en la base de datos y la asocia al usuario."""
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO listas (nombre_lista, descripcion) VALUES (%s, %s) RETURNING id", (nombre_lista, descripcion))
            lista_id = cur.fetchone()[0]
            # Crear la relación usuario-lista
            cur.execute("INSERT INTO usuario_lista (usuario_id, lista_id) VALUES (%s, %s)", (usuario_id, lista_id))
            conn.commit()
            return lista_id
        except psycopg2.Error as e:
            print(f"Error al crear lista: {e}")
            conn.rollback()
            return None
        finally:
            if conn:
                cur.close()
                conn.close()

def obtener_listas_por_usuario(usuario_id):
    """Obtiene todas las listas de un usuario desde la base de datos."""
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("""
                SELECT listas.id, listas.nombre_lista, listas.descripcion, listas.fecha_creacion
                FROM listas
                JOIN usuario_lista ON listas.id = usuario_lista.lista_id
                WHERE usuario_lista.usuario_id = %s
            """, (usuario_id,))
            listas = [Lista(*lista) for lista in cur.fetchall()]
            return listas
        except psycopg2.Error as e:
            print(f"Error al obtener listas: {e}")
            return None
        finally:
            if conn:
                cur.close()
                conn.close()
