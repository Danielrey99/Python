"""Script para poblar la base de datos con datos de prueba."""

from api.services import (
    crear_usuario,
    crear_lista,
    compartir_lista,
    cambiar_rol_usuario,
)

def populate_database():
    """Puebla la base de datos con usuarios y listas de prueba."""

    # Crear usuarios
    usuario1_id = crear_usuario("usuario1", "pass1")
    usuario2_id = crear_usuario("usuario2", "pass2")
    usuario3_id = crear_usuario("usuario3", "pass3")
    admin_id = crear_usuario("admin", "adminpass")
    cambiar_rol_usuario(admin_id, "admin")

    if not all([usuario1_id, usuario2_id, usuario3_id, admin_id]):
        print("Error al crear usuarios.")
        return

    # Crear listas
    lista1_id = crear_lista("Lista de Compras", "Compras para la semana", usuario1_id)
    lista2_id = crear_lista("Tareas del Hogar", "Limpieza y mantenimiento", usuario2_id)
    lista3_id = crear_lista("Proyectos de Trabajo", "Tareas pendientes", usuario3_id)
    lista4_id = crear_lista("Lista Compartida", "Compartida con todos", usuario1_id)

    if not all([lista1_id, lista2_id, lista3_id, lista4_id]):
        print("Error al crear listas.")
        return

    # Compartir listas
    compartir_lista(lista4_id, usuario2_id)
    compartir_lista(lista4_id, usuario3_id)

    print("Base de datos poblada con éxito.")

if __name__ == "__main__":
    populate_database()
