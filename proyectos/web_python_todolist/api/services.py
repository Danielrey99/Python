"""Módulo para la lógica de negocio de la API."""

import psycopg2
from api.models.usuario import Usuario
from api.models.lista import Lista
from api.database.db import create_connection

# Usuarios
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

def eliminar_usuario(usuario_id):
    """Elimina un usuario de la base de datos y sus relaciones."""
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM usuario_lista WHERE usuario_id = %s", (usuario_id,))
            cur.execute("DELETE FROM usuarios WHERE id = %s", (usuario_id,))
            conn.commit()
            return True
        except psycopg2.Error as e:
            print(f"Error al eliminar usuario: {e}")
            conn.rollback()
            return False
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

def obtener_todos_usuarios():
    """Obtiene todos los usuarios de la base de datos, excluyendo contraseñas."""
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT id, nombre_usuario, rol, fecha_registro FROM usuarios")
            usuarios = [Usuario(id=usuario[0], nombre_usuario=usuario[1], contrasenha=None, rol=usuario[2], fecha_registro=usuario[3]) for usuario in cur.fetchall()]
            return usuarios
        except psycopg2.Error as e:
            print(f"Error al obtener todos los usuarios: {e}")
            return None
        finally:
            if conn:
                cur.close()
                conn.close()

def cambiar_nombre_usuario(usuario_id, nuevo_nombre):
    """Cambia el nombre de usuario de un usuario."""
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("UPDATE usuarios SET nombre_usuario = %s WHERE id = %s", (nuevo_nombre, usuario_id))
            conn.commit()
            return True
        except psycopg2.Error as e:
            print(f"Error al cambiar el nombre de usuario: {e}")
            conn.rollback()
            return False
        finally:
            if conn:
                cur.close()
                conn.close()

def cambiar_contrasenha(usuario_id, contrasenha_actual, contrasenha_nueva):
    """Cambia la contraseña de un usuario."""
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            # Verifica la contraseña actual
            cur.execute("SELECT contrasenha FROM usuarios WHERE id = %s", (usuario_id,))
            contrasenha_db = cur.fetchone()[0]
            if contrasenha_db != contrasenha_actual:
                return False  # Contraseña actual incorrecta
            # Actualiza la contraseña
            cur.execute("UPDATE usuarios SET contrasenha = %s WHERE id = %s", (contrasenha_nueva, usuario_id))
            conn.commit()
            return True
        except psycopg2.Error as e:
            print(f"Error al cambiar la contraseña: {e}")
            conn.rollback()
            return False
        finally:
            if conn:
                cur.close()
                conn.close()

def cambiar_rol_usuario(usuario_id, nuevo_rol):
    """Cambia el rol de un usuario."""
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("UPDATE usuarios SET rol = %s WHERE id = %s", (nuevo_rol, usuario_id))
            conn.commit()
            return True
        except psycopg2.Error as e:
            print(f"Error al cambiar el rol de usuario: {e}")
            conn.rollback()
            return False
        finally:
            if conn:
                cur.close()
                conn.close()

# Lsitas
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

def eliminar_lista(lista_id):
    """Elimina una lista de la base de datos y sus relaciones."""
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM usuario_lista WHERE lista_id = %s", (lista_id,))
            cur.execute("DELETE FROM listas WHERE id = %s", (lista_id,))
            conn.commit()
            return True
        except psycopg2.Error as e:
            print(f"Error al eliminar lista: {e}")
            conn.rollback()
            return False
        finally:
            if conn:
                cur.close()
                conn.close()

def obtener_listas_por_usuario(usuario_id):
    """Obtiene todas las listas de un usuario desde la base de datos, sin descripciones."""
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("""
                SELECT listas.id, listas.nombre_lista, listas.fecha_creacion
                FROM listas
                JOIN usuario_lista ON listas.id = usuario_lista.lista_id
                WHERE usuario_lista.usuario_id = %s
            """, (usuario_id,))
            listas = [Lista(id=lista[0], nombre_lista=lista[1], descripcion=None, fecha_creacion=lista[2]) for lista in cur.fetchall()]
            return listas
        except psycopg2.Error as e:
            print(f"Error al obtener listas: {e}")
            return None
        finally:
            if conn:
                cur.close()
                conn.close()

def obtener_lista_por_id(lista_id):
    """Obtiene una lista por su ID desde la base de datos."""
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT id, nombre_lista, descripcion, fecha_creacion FROM listas WHERE id = %s", (lista_id,))
            lista = cur.fetchone()
            if lista:
                return Lista(*lista)
            else:
                return None
        except psycopg2.Error as e:
            print(f"Error al obtener lista: {e}")
            return None
        finally:
            if conn:
                cur.close()
                conn.close()

def obtener_listas_compartidas(usuario_id):
    """Obtiene todas las listas compartidas con un usuario desde la base de datos, sin descripciones."""
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("""
                SELECT listas.id, listas.nombre_lista, listas.fecha_creacion
                FROM listas
                JOIN usuario_lista ON listas.id = usuario_lista.lista_id
                WHERE usuario_lista.usuario_id = %s
            """, (usuario_id,))
            listas = [Lista(id=lista[0], nombre_lista=lista[1], descripcion=None, fecha_creacion=lista[2]) for lista in cur.fetchall()]
            return listas
        except psycopg2.Error as e:
            print(f"Error al obtener listas compartidas: {e}")
            return None
        finally:
            if conn:
                cur.close()
                conn.close()

def actualizar_lista(lista_id, nombre_lista, descripcion):
    """Actualiza el nombre y la descripción de una lista existente."""
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("UPDATE listas SET nombre_lista = %s, descripcion = %s WHERE id = %s", (nombre_lista, descripcion, lista_id))
            conn.commit()
            return True
        except psycopg2.Error as e:
            print(f"Error al actualizar lista: {e}")
            conn.rollback()
            return False
        finally:
            if conn:
                cur.close()
                conn.close()

def compartir_lista(lista_id, usuario_id_compartir):
    """Comparte una lista con otro usuario."""
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO usuario_lista (usuario_id, lista_id) VALUES (%s, %s)", (usuario_id_compartir, lista_id))
            conn.commit()
            return True
        except psycopg2.Error as e:
            print(f"Error al compartir lista: {e}")
            conn.rollback()
            return False
        finally:
            if conn:
                cur.close()
                conn.close()
