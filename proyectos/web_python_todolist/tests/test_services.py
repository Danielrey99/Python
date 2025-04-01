"""
Módulo de pruebas unitarias para los servicios de la API.
"""

import unittest
from api.database.db import create_connection
from api.services import (
    crear_usuario,
    obtener_usuario_por_nombre,
    eliminar_usuario,
    obtener_todos_usuarios,
    cambiar_contrasenha,
    crear_lista,
    obtener_listas_por_usuario,
    obtener_lista_por_id,
    actualizar_lista,
    eliminar_lista,
    compartir_lista,
    obtener_listas_compartidas,
    cambiar_nombre_usuario,
    cambiar_rol_usuario,
)

class TestApiServices(unittest.TestCase):
    """Clase que contiene las pruebas unitarias para los servicios de la API."""

    def setUp(self):
        """Configuración inicial para cada prueba."""
        self.conn = create_connection()
        self.cur = self.conn.cursor()
        # Contador para nombres de usuario únicos
        self.usuario_counter = 0

    def tearDown(self):
        """Limpieza después de cada prueba."""
        # Limpiar las tablas y reiniciar las secuencias en un solo comando
        self.cur.execute("TRUNCATE TABLE usuarios, listas, usuario_lista RESTART IDENTITY CASCADE")
        self.conn.commit()
        self.cur.close()
        self.conn.close()

# Usuarios
    def test_crear_usuario(self):
        """Prueba la creación de un nuevo usuario a través del servicio."""
        usuario_id = crear_usuario("test_user", "password123")
        self.assertIsNotNone(usuario_id)
        self.cur.execute("SELECT * FROM usuarios WHERE id = %s", (usuario_id,))
        usuario = self.cur.fetchone()
        self.assertIsNotNone(usuario)
        self.assertEqual(usuario[1], "test_user")

    def test_obtener_usuario_por_nombre(self):
        """Prueba la obtención de un usuario por su nombre a través del servicio."""
        crear_usuario("test_user", "password123")
        usuario, token = obtener_usuario_por_nombre("test_user", "password123")
        self.assertIsNotNone(usuario)
        self.assertEqual(usuario.nombre_usuario, "test_user")
        self.assertIsNotNone(token)  # Verifica que se devuelva el token
        usuario_incorrecto, token_incorrecto = obtener_usuario_por_nombre("test_user", "wrong_password")
        self.assertIsNone(usuario_incorrecto)
        self.assertIsNone(token_incorrecto)
        usuario_no_encontrado, token_no_encontrado = obtener_usuario_por_nombre("non_existent_user", "password")
        self.assertIsNone(usuario_no_encontrado)
        self.assertIsNone(token_no_encontrado)

    def test_eliminar_usuario(self):
        """Prueba la eliminación de un usuario a través del servicio."""
        usuario_id = crear_usuario("test_user", "password123")
        eliminado = eliminar_usuario(usuario_id)
        self.assertTrue(eliminado)
        usuario = obtener_usuario_por_nombre("test_user", "password123")
        self.assertIsNone(usuario)

    def test_obtener_todos_usuarios(self):
        """Prueba la obtención de todos los usuarios a través del servicio."""
        crear_usuario("user1", "pass1")
        crear_usuario("user2", "pass2")
        usuarios = obtener_todos_usuarios()
        self.assertEqual(len(usuarios), 2)

    def test_cambiar_contrasenha(self):
        """Prueba el cambio de contraseña de un usuario a través del servicio."""
        usuario_id = crear_usuario("test_user", "password123")
        cambiado = cambiar_contrasenha(usuario_id, "password123", "new_password")
        self.assertTrue(cambiado)
        usuario, token = obtener_usuario_por_nombre("test_user", "new_password")
        self.assertEqual(usuario.contrasenha, "new_password")
        cambiado_incorrecto = cambiar_contrasenha(usuario_id, "password123", "another_password")
        self.assertFalse(cambiado_incorrecto)

    def test_cambiar_nombre_usuario(self):
        """Prueba el cambio de nombre de usuario de un usuario."""
        usuario_id = crear_usuario("test_user", "password123")
        cambiado = cambiar_nombre_usuario(usuario_id, "new_user_name")
        self.assertTrue(cambiado)
        usuario = obtener_usuario_por_nombre("new_user_name", "password123")
        self.assertIsNotNone(usuario)
        usuario_no_encontrado = obtener_usuario_por_nombre("test_user", "password123")
        self.assertIsNone(usuario_no_encontrado)

    def test_cambiar_rol_usuario(self):
        """Prueba el cambio de rol de un usuario."""
        usuario_id = crear_usuario("test_user", "password123")
        cambiado = cambiar_rol_usuario(usuario_id, "admin")
        self.assertTrue(cambiado)
        self.cur.execute("SELECT rol FROM usuarios WHERE id = %s", (usuario_id,))
        rol = self.cur.fetchone()[0]
        self.assertEqual(rol, "admin")

# Listas
    def test_crear_lista(self):
        """Prueba la creación de una nueva lista a través del servicio."""
        usuario_id = crear_usuario("test_user", "password123")
        lista_id = crear_lista("Lista de prueba", "Descripción de prueba", usuario_id)
        self.assertIsNotNone(lista_id)
        self.cur.execute("SELECT * FROM listas WHERE id = %s", (lista_id,))
        lista = self.cur.fetchone()
        self.assertIsNotNone(lista)
        self.assertEqual(lista[1], "Lista de prueba")

    def test_obtener_listas_por_usuario(self):
        """Prueba la obtención de listas por usuario a través del servicio."""
        usuario_id = crear_usuario("test_user", "password123")
        crear_lista("Lista 1", "Descripción 1", usuario_id)
        crear_lista("Lista 2", "Descripción 2", usuario_id)
        listas = obtener_listas_por_usuario(usuario_id)
        self.assertEqual(len(listas), 2)

    def test_obtener_lista_por_id(self):
        """Prueba la obtención de una lista por su ID a través del servicio."""
        usuario_id = crear_usuario("test_user", "password123")
        lista_id = crear_lista("Lista de prueba", "Descripción de prueba", usuario_id)
        lista = obtener_lista_por_id(lista_id)
        self.assertIsNotNone(lista)
        self.assertEqual(lista.nombre_lista, "Lista de prueba")

    def test_actualizar_lista(self):
        """Prueba la actualización de una lista a través del servicio."""
        usuario_id = crear_usuario("test_user", "password123")
        lista_id = crear_lista("Lista de prueba", "Descripción de prueba", usuario_id)
        actualizado = actualizar_lista(lista_id, "Lista actualizada", "Nueva descripción")
        self.assertTrue(actualizado)
        lista = obtener_lista_por_id(lista_id)
        self.assertEqual(lista.nombre_lista, "Lista actualizada")

    def test_eliminar_lista(self):
        """Prueba la eliminación de una lista a través del servicio."""
        usuario_id = crear_usuario("test_user", "password123")
        lista_id = crear_lista("Lista de prueba", "Descripción de prueba", usuario_id)
        eliminado = eliminar_lista(lista_id)
        self.assertTrue(eliminado)
        lista = obtener_lista_por_id(lista_id)
        self.assertIsNone(lista)

    def test_compartir_lista(self):
        """Prueba la compartición de una lista con otro usuario a través del servicio."""
        usuario_id1 = crear_usuario("user1", "pass1")
        usuario_id2 = crear_usuario("user2", "pass2")
        lista_id = crear_lista("Lista compartida", "Descripción", usuario_id1)
        compartido = compartir_lista(lista_id, usuario_id2)
        self.assertTrue(compartido)
        listas_compartidas = obtener_listas_compartidas(usuario_id2)
        self.assertEqual(len(listas_compartidas), 1)

    def test_obtener_listas_compartidas(self):
        """Prueba la obtención de listas compartidas con un usuario a través del servicio."""
        usuario_id1 = crear_usuario("user1", "pass1")
        usuario_id2 = crear_usuario("user2", "pass2")
        lista_id = crear_lista("Lista compartida", "Descripción", usuario_id1)
        compartir_lista(lista_id, usuario_id2)
        listas_compartidas = obtener_listas_compartidas(usuario_id2)
        self.assertEqual(len(listas_compartidas), 1)

if __name__ == '__main__':
    unittest.main()
