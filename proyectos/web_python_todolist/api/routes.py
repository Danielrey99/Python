"""Módulo para definir las rutas de la API."""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from .services import (
    crear_usuario,
    obtener_usuario_por_nombre,
    obtener_usuario_por_id,
    crear_lista,
    obtener_listas_por_usuario,
    obtener_listas_asociadas,
)

class RequestHandler(BaseHTTPRequestHandler):
    """
    Manejador de solicitudes HTTP para la API.
    Esta clase extiende `BaseHTTPRequestHandler` para proporcionar
    funcionalidad para manejar solicitudes GET y POST a la API.
    """
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
            usuario_id = crear_usuario(data['nombre_usuario'], data['contrasenha'])
            if usuario_id:
                self.send_response(201) # Creado
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'id': usuario_id}).encode('utf-8'))
            else:
                self.send_response(409)  # Nombre de usuario duplicado
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Nombre de usuario duplicado'}).encode('utf-8'))
        elif self.path == '/listas':
            lista_id = crear_lista(data['nombre_lista'], data['descripcion'], data['usuario_id'])
            if lista_id:
                self.send_response(201) # Creado
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'id': lista_id}).encode('utf-8'))
            else:
                self.send_response(500)  # Error interno del servidor
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Error al crear la lista'}).encode('utf-8'))
        else:
            self.send_response(404) # Solicitud incorrecta
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Ruta no encontrada'}).encode('utf-8'))

    def do_GET(self):
        """
        Maneja las solicitudes GET a la API.
        Las respuestas se envían en formato JSON.
        """
        if self.path.startswith('/usuarios/id/'):
            usuario_id = int(self.path.split('/')[-1])
            usuario = obtener_usuario_por_id(usuario_id)
            if usuario:
                self.send_response(200) # OK
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(usuario.__dict__).encode('utf-8'))
            else:
                self.send_response(404) # Solicitud incorrecta
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Usuario no encontrado'}).encode('utf-8'))
        elif self.path.startswith('/usuarios/'):
            nombre_usuario = self.path.split('/')[-1]
            usuario = obtener_usuario_por_nombre(nombre_usuario)
            if usuario:
                self.send_response(200) # OK
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(usuario.__dict__).encode('utf-8'))
            else:
                self.send_response(404) # Solicitud incorrecta
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Usuario no encontrado'}).encode('utf-8'))
        elif self.path.startswith('/listas/'):
            usuario_id = int(self.path.split('/')[-1])
            listas = obtener_listas_por_usuario(usuario_id)
            if listas:
                self.send_response(200) # OK
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps([lista.__dict__ for lista in listas]).encode('utf-8'))
            else:
                self.send_response(404) # Solicitud incorrecta
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Listas no encontradas'}).encode('utf-8'))
        elif self.path.startswith('/usuario_lista/'):
            usuario_id = int(self.path.split('/')[-1])
            listas = obtener_listas_asociadas(usuario_id)
            if listas:
                self.send_response(200) # OK
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps([lista.__dict__ for lista in listas]).encode('utf-8'))
            else:
                self.send_response(404) # Solicitud incorrecta
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Listas no encontradas'}).encode('utf-8'))
        else:
            self.send_response(404) # Solicitud incorrecta
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Ruta no encontrada'}).encode('utf-8'))

def run_api(port=8000):
    """Función para iniciar el servidor de la API."""
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f'Iniciando servidor en el puerto {port}...')
    httpd.serve_forever()

# El servidor solo se inicia cuando el script se ejecuta directamente
if __name__ == '__main__':
    run_api()
