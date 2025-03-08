"""
Módulo para gestionar la conexión a la base de datos PostgreSQL.

Este módulo proporciona una función para crear una conexión a la base de datos
utilizando variables de entorno para almacenar las credenciales de acceso.
"""

import os
import psycopg2
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

def create_connection():
    """
    Crea y retorna una conexión a la base de datos PostgreSQL.
    """
    try:
        # Obtener parámetros de conexión desde las variables de entorno
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
