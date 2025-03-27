"""Módulo para definir las rutas de la API."""

from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import json
import signal
import sys
import threading
from .services import (
    crear_usuario,
    eliminar_usuario,
    obtener_usuario_por_nombre,
    obtener_todos_usuarios,
    cambiar_nombre_usuario,
    cambiar_contrasenha,
    cambiar_rol_usuario,
    crear_lista,
    eliminar_lista,
    obtener_listas_por_usuario,
    obtener_lista_por_id,
    obtener_listas_compartidas,
    actualizar_lista,
    compartir_lista
)

class RequestHandler(BaseHTTPRequestHandler):
    """
    Manejador de solicitudes HTTP para la API.
    Esta clase extiende `BaseHTTPRequestHandler` para proporcionar
    funcionalidad para manejar solicitudes GET y POST a la API.
    """
    def send_cors_headers(self):
        """Envía los encabezados CORS necesarios."""
        self.send_header('Access-Control-Allow-Origin', 'http://localhost:5173')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def do_OPTIONS(self):
        """Maneja las solicitudes OPTIONS (preflight)."""
        self.send_response(204)  # No Content
        self.send_cors_headers()
        self.end_headers()

    def do_GET(self):
        """
        Maneja las solicitudes GET a la API.
        Las respuestas se envían en formato JSON.
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.send_cors_headers()
            self.end_headers()
            ruta_base = os.path.dirname(__file__)  # Obtiene la ruta de 'routes.py'
            ruta_html = os.path.join(ruta_base, 'index.html')
            with open(ruta_html, 'rb') as f:
                self.wfile.write(f.read())
        elif self.path == '/usuarios':
            # Obtener todos los usuarios
            usuarios = obtener_todos_usuarios()
            if usuarios:
                self.send_response(200) # OK
                self.send_header('Content-type', 'application/json')
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps([usuario.to_dict() for usuario in usuarios]).encode('utf-8'))
            else:
                self.send_response(500) # Internal Server Error
                self.send_header('Content-type', 'application/json')
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Error al obtener usuarios'}).encode('utf-8'))
        elif self.path.startswith('/listas/compartidas/'):
            # Obtener listas compartidas con un usuario
            usuario_id = int(self.path.split('/')[-1])
            listas = obtener_listas_compartidas(usuario_id)
            if listas:
                self.send_response(200) # OK
                self.send_header('Content-type', 'application/json')
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps([lista.to_dict() for lista in listas]).encode('utf-8'))
            else:
                self.send_response(404) # Not Found
                self.send_header('Content-type', 'application/json')
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Listas compartidas no encontradas'}).encode('utf-8'))
        elif self.path.startswith('/listas/id/'):
            # Obtener lista por ID
            lista_id = int(self.path.split('/')[-1])
            lista = obtener_lista_por_id(lista_id)
            if lista:
                self.send_response(200) # OK
                self.send_header('Content-type', 'application/json')
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps(lista.to_dict()).encode('utf-8'))
            else:
                self.send_response(404) # Not Found
                self.send_header('Content-type', 'application/json')
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Lista no encontrada'}).encode('utf-8'))
        elif self.path.startswith('/listas/'):
            # Obtener listas de un usuario
            usuario_id = int(self.path.split('/')[-1])
            listas = obtener_listas_por_usuario(usuario_id)
            if listas:
                self.send_response(200) # OK
                self.send_header('Content-type', 'application/json')
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps([lista.to_dict() for lista in listas]).encode('utf-8'))
            else:
                self.send_response(404) # Not Found
                self.send_header('Content-type', 'application/json')
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Listas no encontradas'}).encode('utf-8'))
        else:
            self.send_response(404) # Not Found
            self.send_header('Content-type', 'application/json')
            self.send_cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Ruta no encontrada'}).encode('utf-8'))

    def do_POST(self):
        """
        Maneja las solicitudes POST a la API.
        Los datos de la solicitud se esperan en formato JSON.
        Las respuestas se envían en formato JSON.
        """
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))

        if self.path == '/usuarios':
            # Crear un nuevo usuario
            usuario_id = crear_usuario(data['nombre_usuario'], data['contrasenha'])
            if usuario_id:
                self.send_response(201) # Created
                self.send_header('Content-type', 'application/json')
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({'id': usuario_id}).encode('utf-8'))
            else:
                self.send_response(400)  # Bad Request (nombre de usuario duplicado)
                self.send_header('Content-type', 'application/json')
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Nombre de usuario duplicado'}).encode('utf-8'))
        elif self.path == '/login':
            # Iniciar sesión
            nombre_usuario = data.get('nombre_usuario')
            contrasenha_ingresada = data.get('contrasenha')
            usuario = obtener_usuario_por_nombre(nombre_usuario, contrasenha_ingresada)
            if usuario:
                self.send_response(200) # OK
                self.send_header('Content-type', 'application/json')
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps(usuario.to_dict()).encode('utf-8'))
            else:
                self.send_response(401) # Unauthorized
                self.send_header('Content-type', 'application/json')
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Credenciales incorrectas'}).encode('utf-8'))
        elif self.path.startswith('/listas/compartir'):
            # Compartir una lista con un usuario
            lista_id = data['lista_id']
            usuario_id_compartir = data['usuario_id_compartir']
            if compartir_lista(lista_id, usuario_id_compartir):
                self.send_response(200) # OK
                self.send_header('Content-type', 'application/json')
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Lista compartida'}).encode('utf-8'))
            else:
                self.send_response(500) # Internal Server Error
                self.send_header('Content-type', 'application/json')
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Error al compartir la lista'}).encode('utf-8'))
        elif self.path == '/listas':
            # Crear una nueva lista
            lista_id = crear_lista(data['nombre_lista'], data['descripcion'], data['usuario_id'])
            if lista_id:
                self.send_response(201) # Created
                self.send_header('Content-type', 'application/json')
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({'id': lista_id}).encode('utf-8'))
            else:
                self.send_response(500) # Internal Server Error
                self.send_header('Content-type', 'application/json')
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Error al crear la lista'}).encode('utf-8'))
        else:
            self.send_response(404) # Not Found
            self.send_header('Content-type', 'application/json')
            self.send_cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Ruta no encontrada'}).encode('utf-8'))

    def do_PUT(self):
        """
        Maneja las solicitudes PUT a la API.
        Los datos de la solicitud se esperan en formato JSON.
        Las respuestas se envían en formato JSON.
        """
        content_length = int(self.headers['Content-Length'])
        put_data = self.rfile.read(content_length)
        data = json.loads(put_data.decode('utf-8'))

        if self.path.startswith('/usuarios/cambiar_nombre/'):
            # Cambiar el nombre de usuario
            usuario_id = int(self.path.split('/')[-1])
            nuevo_nombre = data['nuevo_nombre']
            if cambiar_nombre_usuario(usuario_id, nuevo_nombre):
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Nombre de usuario actualizado'}).encode('utf-8'))
            else:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Error al actualizar el nombre de usuario'}).encode('utf-8'))
        elif self.path.startswith('/usuarios/cambiar_rol/'):
            # Cambiar el rol de usuario
            usuario_id = int(self.path.split('/')[-1])
            nuevo_rol = data['nuevo_rol']
            if cambiar_rol_usuario(usuario_id, nuevo_rol):
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Rol de usuario actualizado'}).encode('utf-8'))
            else:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Error al actualizar el rol de usuario'}).encode('utf-8'))
        elif self.path.startswith('/usuarios/cambiar_contrasenha/'):
            # Cambiar la contraseña de un usuario
            usuario_id = int(self.path.split('/')[-1])
            if cambiar_contrasenha(usuario_id, data['contrasenha_actual'], data['contrasenha_nueva']):
                self.send_response(200) # OK
                self.send_header('Content-type', 'application/json')
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Contraseña actualizada'}).encode('utf-8'))
            else:
                self.send_response(401) # Unauthorized
                self.send_header('Content-type', 'application/json')
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Contraseña actual incorrecta'}).encode('utf-8'))
        elif self.path.startswith('/listas/actualizar/'):
            # Actualizar una lista
            lista_id = int(self.path.split('/')[-1])
            if actualizar_lista(lista_id, data['nombre_lista'], data['descripcion']):
                self.send_response(200) # OK
                self.send_header('Content-type', 'application/json')
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Lista actualizada'}).encode('utf-8'))
            else:
                self.send_response(500) # Internal Server Error
                self.send_header('Content-type', 'application/json')
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Error al actualizar lista'}).encode('utf-8'))
        else:
            self.send_response(404) # Not Found
            self.send_header('Content-type', 'application/json')
            self.send_cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Ruta no encontrada'}).encode('utf-8'))

    def do_DELETE(self):
        """
        Maneja las solicitudes DELETE a la API.
        Las respuestas se envían en formato JSON.
        """
        if self.path.startswith('/usuarios/eliminar/'):
            # Eliminar un usuario
            usuario_id = int(self.path.split('/')[-1])
            if eliminar_usuario(usuario_id):
                self.send_response(200) # OK
                self.send_header('Content-type', 'application/json')
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Usuario eliminado'}).encode('utf-8'))
            else:
                self.send_response(500) # Internal Server Error
                self.send_header('Content-type', 'application/json')
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Error al eliminar usuario'}).encode('utf-8'))
        elif self.path.startswith('/listas/eliminar/'):
            # Eliminar una lista
            lista_id = int(self.path.split('/')[-1])
            if eliminar_lista(lista_id):
                self.send_response(200) # OK
                self.send_header('Content-type', 'application/json')
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Lista eliminada'}).encode('utf-8'))
            else:
                self.send_response(500) # Internal Server Error
                self.send_header('Content-type', 'application/json')
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Error al eliminar lista'}).encode('utf-8'))
        else:
            self.send_response(404) # Not Found
            self.send_header('Content-type', 'application/json')
            self.send_cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Ruta no encontrada'}).encode('utf-8'))

def run_api(port=8000):
    """Función para iniciar el servidor de la API con manejo de cierre."""
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f'Iniciando servidor en el puerto {port}...')

    # Ejecutar el servidor en un hilo separado
    server_thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    server_thread.start()

    # Manejo de señales para cerrar correctamente
    def shutdown_handler(signal_received, frame):
        print("\nSeñal de cierre recibida. Apagando el servidor...")
        httpd.shutdown()  # Detiene el bucle de `serve_forever()`
        httpd.server_close()  # Libera el socket del servidor
        print("Servidor apagado correctamente.")
        sys.exit(0)  # Cerrar el proceso completamente

    # Capturar señales de interrupción (Ctrl + C) y SIGTERM (kill)
    signal.signal(signal.SIGINT, shutdown_handler)
    signal.signal(signal.SIGTERM, shutdown_handler)

    # Mantener el hilo principal vivo
    try:
        while True:
            pass
    except KeyboardInterrupt:
        shutdown_handler(None, None)
