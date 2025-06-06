"""Módulo para la lógica de negocio de la API."""

import os
import psycopg2
import bcrypt
import jwt
from dotenv import load_dotenv
from api.models.usuario import Usuario
from api.models.lista import Lista
from api.database.db import create_connection

load_dotenv()
SECRET_KEY =os.getenv("JWT_KET")

def generar_token(usuario_id, nombre_usuario, rol):
    """Genera un nuevo token JWT."""
    payload = {
        'id': usuario_id,
        'nombre_usuario': nombre_usuario,
        'rol': rol,
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

# Usuarios
def crear_usuario(nombre_usuario, contrasenha):
    """Crea un nuevo usuario en la base de datos con contraseña encriptada."""
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            # Encriptar la contraseña
            contrasenha_encriptada = bcrypt.hashpw(contrasenha.encode('utf-8'), bcrypt.gensalt())
            cur.execute("INSERT INTO usuarios (nombre_usuario, contrasenha, rol) VALUES (%s, %s, %s) RETURNING id", (nombre_usuario, contrasenha_encriptada, 'usuario'))
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
    """Elimina un usuario de la base de datos, sus relaciones y las listas no compartidas."""
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT lista_id FROM usuario_lista WHERE usuario_id = %s", (usuario_id,))
            listas_usuario = cur.fetchall()
            for lista_id in listas_usuario:
                cur.execute("SELECT COUNT(*) FROM usuario_lista WHERE lista_id = %s", (lista_id[0],))
                count = cur.fetchone()[0]
                if count == 1:  # Si solo este usuario está asociado a la lista
                    cur.execute("DELETE FROM listas WHERE id = %s", (lista_id[0],))
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

def obtener_usuario_por_nombre(nombre_usuario, contrasenha_ingresada):
    """Obtiene un usuario por su nombre desde la base de datos, verificando la contraseña y genera un token."""
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            # Obtener la contraseña encriptada de la base de datos
            cur.execute("SELECT id, nombre_usuario, contrasenha, rol, fecha_registro FROM usuarios WHERE nombre_usuario = %s", (nombre_usuario,))
            usuario_db = cur.fetchone()
            if usuario_db:
                usuario_id, nombre_usuario_db, contrasenha_db, rol, fecha_registro = usuario_db
                # Verificar la contraseña
                if bcrypt.checkpw(contrasenha_ingresada.encode('utf-8'), contrasenha_db.tobytes()):
                    # Generar token JWT
                    token = generar_token(usuario_id, nombre_usuario_db, rol)
                    # Contraseña correcta, obtener los datos del usuario sin la contraseña
                    return Usuario(id=usuario_id, nombre_usuario=nombre_usuario_db, contrasenha=None, rol=rol, fecha_registro=fecha_registro), token
                else:
                    return None, None # Contraseña incorrecta
            else:
                return  None, None # Usuario no encontrado
        except psycopg2.Error as e:
            print(f"Error al obtener usuario: {e}")
            return  None, None
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
    """Cambia el nombre de usuario de un usuario y genera un nuevo token."""
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("UPDATE usuarios SET nombre_usuario = %s WHERE id = %s RETURNING rol", (nuevo_nombre, usuario_id))
            rol = cur.fetchone()[0]
            conn.commit()
            token = generar_token(usuario_id, nuevo_nombre, rol)
            return token, True
        except psycopg2.Error as e:
            print(f"Error al cambiar el nombre de usuario: {e}")
            conn.rollback()
            return None, False
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
            # Obtener la contraseña encriptada actual de la base de datos
            cur.execute("SELECT contrasenha FROM usuarios WHERE id = %s", (usuario_id,))
            contrasenha_db = cur.fetchone()[0]
            # Convertir memoryview a bytes
            contrasenha_db_bytes = bytes(contrasenha_db)
            # Verificar la contraseña actual
            if not bcrypt.checkpw(contrasenha_actual.encode('utf-8'), contrasenha_db_bytes):
                return False  # Contraseña actual incorrecta
            # Encriptar la nueva contraseña
            contrasenha_nueva_encriptada = bcrypt.hashpw(contrasenha_nueva.encode('utf-8'), bcrypt.gensalt())
            # Actualiza la contraseña en la base de datos
            cur.execute("UPDATE usuarios SET contrasenha = %s WHERE id = %s", (contrasenha_nueva_encriptada, usuario_id))
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
    """Cambia el rol de un usuario y genera un nuevo token."""
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("UPDATE usuarios SET rol = %s WHERE id = %s RETURNING nombre_usuario", (nuevo_rol, usuario_id))
            nombre_usuario = cur.fetchone()[0]
            conn.commit()
            token = generar_token(usuario_id, nombre_usuario, nuevo_rol)
            return token, True
        except psycopg2.Error as e:
            print(f"Error al cambiar el rol de usuario: {e}")
            conn.rollback()
            return None, False
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

def eliminar_lista(lista_id, usuario_id):
    """Elimina una lista de la base de datos y sus relaciones, verificando permisos."""
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            # Verificar si el usuario tiene permiso para eliminar la lista
            cur.execute("""
                SELECT 1
                FROM usuario_lista
                WHERE lista_id = %s AND usuario_id = %s
            """, (lista_id, usuario_id))
            if cur.fetchone():
                # Eliminar las relaciones en usuario_lista
                cur.execute("DELETE FROM usuario_lista WHERE lista_id = %s", (lista_id,))
                # Eliminar la lista
                cur.execute("DELETE FROM listas WHERE id = %s", (lista_id,))
                conn.commit()
                return True
            else:
                return False
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
                SELECT l.id, l.nombre_lista, l.fecha_creacion
                FROM listas l
                JOIN usuario_lista ul ON l.id = ul.lista_id
                WHERE ul.usuario_id = %s
                AND NOT EXISTS (
                    SELECT 1
                    FROM usuario_lista ul2
                    WHERE ul2.lista_id = l.id AND ul2.usuario_id != %s
                )
            """, (usuario_id, usuario_id))
            listas = [Lista(id=lista[0], nombre_lista=lista[1], descripcion=None, fecha_creacion=lista[2]) for lista in cur.fetchall()]
            return listas
        except psycopg2.Error as e:
            print(f"Error al obtener listas: {e}")
            return None
        finally:
            if conn:
                cur.close()
                conn.close()

def obtener_lista_por_id(lista_id, usuario_id):
    """Obtiene una lista por su ID desde la base de datos, verificando permisos e indicando si está compartida."""
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("""
                SELECT l.id, l.nombre_lista, l.descripcion, l.fecha_creacion,
                    EXISTS (
                        SELECT 1
                        FROM usuario_lista ul
                        WHERE ul.lista_id = l.id AND ul.usuario_id != %s
                    ) AS es_compartida
                FROM listas l
                JOIN usuario_lista ul2 ON l.id = ul2.lista_id
                WHERE l.id = %s AND ul2.usuario_id = %s
            """, (usuario_id, lista_id, usuario_id))
            lista_data = cur.fetchone()
            if lista_data:
                lista = Lista(id=lista_data[0], nombre_lista=lista_data[1], descripcion=lista_data[2], fecha_creacion=lista_data[3])
                es_compartida = lista_data[4]
                return lista, es_compartida
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

def actualizar_lista(lista_id, nombre_lista, descripcion, usuario_id):
    """Actualiza el nombre y la descripción de una lista existente, verificando permisos."""
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("""
                UPDATE listas
                SET nombre_lista = %s, descripcion = %s
                WHERE id = %s AND
                id in (select lista_id from usuario_lista where usuario_id = %s)
            """, (nombre_lista, descripcion, lista_id, usuario_id))
            conn.commit()
            if cur.rowcount > 0:
                return True
            else:
                return False
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

# Verificar Token
def verificar_token(token):
    """Verifica un token JWT y devuelve los datos del usuario si es válido."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None # Token expirado
    except jwt.InvalidTokenError:
        return None # Token inválido
