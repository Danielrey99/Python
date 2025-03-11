"""
Módulo de pruebas unitarias para verificar la conexión de la API a la base de datos PostgreSQL.
"""

import unittest
from api.database.db import create_connection

class TestDatabaseConnection(unittest.TestCase):
    """Clase que contiene las pruebas para la conexión a la base de datos."""

    def test_conexion_exitosa(self):
        """Prueba que la conexión a la base de datos sea exitosa."""
        conn = create_connection()
        # Verifica que la conexión no sea None
        self.assertIsNotNone(conn, "La conexión a la base de datos falló.")
        if conn:
            conn.close()

    def test_cierre_conexion(self):
        """Prueba que la conexión se cierre correctamente."""
        conn = create_connection()
        self.assertIsNotNone(conn, "La conexión a la base de datos falló.")
        conn.close()
        # Verifica que la conexión esté cerrada
        self.assertTrue(conn.closed, "La conexión no se cerró correctamente.")

if __name__ == '__main__':
    unittest.main()
