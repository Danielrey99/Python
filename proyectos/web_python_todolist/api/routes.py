"""Módulo para definir las rutas de la API."""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from .services import (
    crear_usuario,
    obtener_usuario_por_nombre,
    actualizar_usuario,
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
)

class RequestHandler(BaseHTTPRequestHandler):
    """
    Manejador de solicitudes HTTP para la API.
    Esta clase extiende `BaseHTTPRequestHandler` para proporcionar
    funcionalidad para manejar solicitudes GET y POST a la API.
    """
def do_GET(self):
    """
    Maneja las solicitudes GET a la API.
    Las respuestas se envían en formato JSON.
    """
    if self.path == '/usuarios/todos':
        # Obtener todos los usuarios
        usuarios = obtener_todos_usuarios()
        if usuarios:
            self.send_response(200) # OK
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps([usuario.to_dict() for usuario in usuarios]).encode('utf-8'))
        else:
            self.send_response(500) # Internal Server Error
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Error al obtener usuarios'}).encode('utf-8'))
    elif self.path.startswith('/usuarios/'):
        # Obtener usuario por nombre
        nombre_usuario = self.path.split('/')[-1]
        usuario = obtener_usuario_por_nombre(nombre_usuario)
        if usuario:
            self.send_response(200) # OK
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(usuario.to_dict()).encode('utf-8'))
        else:
            self.send_response(404) # Not Found
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Usuario no encontrado'}).encode('utf-8'))
    elif self.path.startswith('/listas/compartidas/'):
        # Obtener listas compartidas con un usuario
        usuario_id = int(self.path.split('/')[-1])
        listas = obtener_listas_compartidas(usuario_id)
        if listas:
            self.send_response(200) # OK
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps([lista.to_dict() for lista in listas]).encode('utf-8'))
        else:
            self.send_response(404) # Not Found
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Listas compartidas no encontradas'}).encode('utf-8'))
    elif self.path.startswith('/listas/id/'):
        # Obtener lista por ID
        lista_id = int(self.path.split('/')[-1])
        lista = obtener_lista_por_id(lista_id)
        if lista:
            self.send_response(200) # OK
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(lista.to_dict()).encode('utf-8'))
        else:
            self.send_response(404) # Not Found
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Lista no encontrada'}).encode('utf-8'))
    elif self.path.startswith('/listas/'):
        # Obtener listas de un usuario
        usuario_id = int(self.path.split('/')[-1])
        listas = obtener_listas_por_usuario(usuario_id)
        if listas:
            self.send_response(200) # OK
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps([lista.to_dict() for lista in listas]).encode('utf-8'))
        else:
            self.send_response(404) # Not Found
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Listas no encontradas'}).encode('utf-8'))
    else:
        self.send_response(404) # Not Found
        self.send_header('Content-type', 'application/json')
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
            self.end_headers()
            self.wfile.write(json.dumps({'id': usuario_id}).encode('utf-8'))
        else:
            self.send_response(400)  # Bad Request (nombre de usuario duplicado)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Nombre de usuario duplicado'}).encode('utf-8'))
    elif self.path.startswith('/listas/compartir/'):
        # Compartir una lista con un usuario
        lista_id = int(self.path.split('/')[-2])
        usuario_id_compartir = int(self.path.split('/')[-1])
        if compartir_lista(lista_id, usuario_id_compartir):
            self.send_response(200) # OK
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Lista compartida'}).encode('utf-8'))
        else:
            self.send_response(500) # Internal Server Error
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Error al compartir la lista'}).encode('utf-8'))
    elif self.path == '/listas':
        # Crear una nueva lista
        lista_id = crear_lista(data['nombre_lista'], data['descripcion'], data['usuario_id'])
        if lista_id:
            self.send_response(201) # Created
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'id': lista_id}).encode('utf-8'))
        else:
            self.send_response(500) # Internal Server Error
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Error al crear la lista'}).encode('utf-8'))
    else:
        self.send_response(404) # Not Found
        self.send_header('Content-type', 'application/json')
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

    if self.path.startswith('/usuarios/actualizar/'):
        # Actualizar un usuario
        usuario_id = int(self.path.split('/')[-1])
        if actualizar_usuario(usuario_id, data['nombre_usuario'], data['contrasenha'], data['rol']):
            self.send_response(200) # OK
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Usuario actualizado'}).encode('utf-8'))
        else:
            self.send_response(500) # Internal Server Error
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Error al actualizar usuario'}).encode('utf-8'))
    elif self.path.startswith('/usuarios/cambiar_contrasenha/'):
        # Cambiar la contraseña de un usuario
        usuario_id = int(self.path.split('/')[-1])
        if cambiar_contrasenha(usuario_id, data['contrasenha_actual'], data['contrasenha_nueva']):
            self.send_response(200) # OK
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Contraseña actualizada'}).encode('utf-8'))
        else:
            self.send_response(401) # Unauthorized
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Contraseña actual incorrecta'}).encode('utf-8'))
    elif self.path.startswith('/listas/actualizar/'):
        # Actualizar una lista
        lista_id = int(self.path.split('/')[-1])
        if actualizar_lista(lista_id, data['nombre_lista'], data['descripcion']):
            self.send_response(200) # OK
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Lista actualizada'}).encode('utf-8'))
        else:
            self.send_response(500) # Internal Server Error
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Error al actualizar lista'}).encode('utf-8'))
    else:
        self.send_response(404) # Not Found
        self.send_header('Content-type', 'application/json')
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
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Usuario eliminado'}).encode('utf-8'))
        else:
            self.send_response(500) # Internal Server Error
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Error al eliminar usuario'}).encode('utf-8'))
    elif self.path.startswith('/listas/eliminar/'):
        # Eliminar una lista
        lista_id = int(self.path.split('/')[-1])
        if eliminar_lista(lista_id):
            self.send_response(200) # OK
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Lista eliminada'}).encode('utf-8'))
        else:
            self.send_response(500) # Internal Server Error
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Error al eliminar lista'}).encode('utf-8'))
    else:
        self.send_response(404) # Not Found
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
