"""
Módulo de pruebas unitarias para los servicios de la API.
"""

import unittest
from api.services import (
    crear_usuario,
    obtener_usuario_por_nombre,
    obtener_usuario_por_id,
    crear_lista,
    obtener_listas_por_usuario,
    obtener_listas_asociadas,
)
from api.database.db import create_connection

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
        usuario = obtener_usuario_por_nombre("test_user")
        self.assertIsNotNone(usuario)
        self.assertEqual(usuario.nombre_usuario, "test_user")

    def test_obtener_usuario_por_id(self):
        """Prueba la obtención de un usuario por su ID a través del servicio."""
        usuario_id = crear_usuario("test_user", "password123")
        usuario = obtener_usuario_por_id(usuario_id)
        self.assertIsNotNone(usuario)
        self.assertEqual(usuario.id, usuario_id)

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

    def test_obtener_listas_asociadas(self):
        """Prueba la obtención de listas asociadas a un usuario a través del servicio."""
        usuario_id = crear_usuario("test_user", "password123")
        lista_id = crear_lista("Lista de prueba", "Descripción de prueba", usuario_id)
        listas = obtener_listas_asociadas(usuario_id)
        self.assertEqual(len(listas), 1)
        self.assertEqual(listas[0].id, lista_id)

if __name__ == '__main__':
    unittest.main()
