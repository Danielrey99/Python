# tests/test_models.py
"""
Módulo de pruebas unitarias para los modelos.
"""

import unittest
from models.usuario import Usuario
from models.lista import Lista
from models.usuario_lista import UsuarioLista
from database.db import create_connection

class TestModelos(unittest.TestCase):
    """Clase que contiene las pruebas unitarias para los modelos."""

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
        """Prueba la creación de un nuevo usuario."""
        usuario_id = Usuario.crear("test_user", "password123")
        self.assertIsNotNone(usuario_id)
        self.cur.execute("SELECT * FROM usuarios WHERE id = %s", (usuario_id,))
        usuario = self.cur.fetchone()
        self.assertIsNotNone(usuario)
        self.assertEqual(usuario[1], "test_user")

    def test_obtener_usuario_por_nombre(self):
        """Prueba la obtención de un usuario por su nombre de usuario."""
        Usuario.crear("test_user", "password123")
        usuario = Usuario.obtener_por_nombre_usuario("test_user")
        self.assertIsNotNone(usuario)
        self.assertEqual(usuario.nombre_usuario, "test_user")

    def test_obtener_usuario_por_id(self):
        """Prueba la obtención de un usuario por su ID."""
        usuario_id = Usuario.crear("test_user", "password123")
        usuario = Usuario.obtener_por_id(usuario_id)
        self.assertIsNotNone(usuario)
        self.assertEqual(usuario.id, usuario_id)

    def test_crear_lista(self):
        """Prueba la creación de una nueva lista."""
        usuario_id = Usuario.crear("test_user", "password123")
        lista_id = Lista.crear("Lista de prueba", "Descripción de prueba", usuario_id)
        self.assertIsNotNone(lista_id)
        self.cur.execute("SELECT * FROM listas WHERE id = %s", (lista_id,))
        lista = self.cur.fetchone()
        self.assertIsNotNone(lista)
        self.assertEqual(lista[1], "Lista de prueba")

    def test_obtener_listas_por_usuario(self):
        """Prueba la obtención de listas por usuario."""
        usuario_id = Usuario.crear("test_user", "password123")
        Lista.crear("Lista 1", "Descripción 1", usuario_id)
        Lista.crear("Lista 2", "Descripción 2", usuario_id)
        listas = Lista.obtener_por_usuario_id(usuario_id)
        self.assertEqual(len(listas), 2)

    def test_crear_usuario_lista(self):
        """Prueba la asociación de un usuario a una lista."""
        usuario_id = Usuario.crear("test_user", "password123")
        lista_id = Lista.crear("Lista de prueba", "Descripción de prueba", usuario_id)
        result = UsuarioLista.crear(usuario_id, lista_id)
        self.assertTrue(result)
        self.cur.execute("SELECT * FROM usuario_lista WHERE usuario_id = %s AND lista_id = %s", (usuario_id, lista_id))
        usuario_lista = self.cur.fetchone()
        self.assertIsNotNone(usuario_lista)

    def test_obtener_listas_asociadas(self):
        """Prueba la obtención de listas asociadas a un usuario."""
        usuario_id = Usuario.crear("test_user", "password123")
        lista_id = Lista.crear("Lista de prueba", "Descripción de prueba", usuario_id)
        UsuarioLista.crear(usuario_id, lista_id)
        listas = UsuarioLista.obtener_listas_por_usuario_id(usuario_id)
        self.assertEqual(len(listas), 1)
        self.assertEqual(listas[0].id, lista_id)

if __name__ == '__main__':
    unittest.main()
