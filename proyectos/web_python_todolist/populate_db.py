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
    usuario1_id = crear_usuario("Ana García", "Ana12345")
    usuario2_id = crear_usuario("Carlos López", "Carlos678")
    usuario3_id = crear_usuario("Sofía Martínez", "Sofia90Ab")
    admin_id = crear_usuario("admin", "adminpass")
    cambiar_rol_usuario(admin_id, "admin")

    if not all([usuario1_id, usuario2_id, usuario3_id, admin_id]):
        print("Error al crear usuarios.")
        return

    # Crear listas para Ana García
    crear_lista("Compras Semanales", "- Leche\n- Huevos\n- Pan\n- Cebolla\n- Manzanas\n- Pollo\n- Pasta\n- Tomates\n- Arroz\n- Yogur\n- Detergente\n- Papel higiénico\n- Jabón\n- Champú\n- Servilletas", usuario1_id)
    crear_lista("Recetas para el Mes", "- Lasaña de verduras\n- Pollo al curry\n- Salmón a la plancha\n- Ensalada César\n- Tarta de manzana\n- Sopa de calabaza\n- Pizza casera\n- Arroz con leche\n- Croquetas de jamón\n- Paella de marisco", usuario1_id)
    crear_lista("Libros para Leer", "- Cien años de soledad (Gabriel García Márquez)\n- 1984 (George Orwell)\n- El señor de los anillos (J.R.R. Tolkien)\n- Orgullo y prejuicio (Jane Austen)\n- Matar a un ruiseñor (Harper Lee)\n- Don Quijote de la Mancha (Miguel de Cervantes)\n- Crimen y castigo (Fiódor Dostoyevski)\n- El gran Gatsby (F. Scott Fitzgerald)", usuario1_id)
    crear_lista("Viaje a Roma", "- Vuelos: Salida 15/07, Regreso 22/07\n- Hotel: Hotel Artemide\n- Lugares: Coliseo, Fontana di Trevi, Vaticano, Foro Romano\n- Restaurantes: Trattoria Da Enzo al 29, Armando al Pantheon", usuario1_id)
    crear_lista("Regalos de Cumpleaños", "- Juan: Libro de historia\n- María: Perfume\n- Pedro: Auriculares inalámbricos\n- Laura: Set de pintura", usuario1_id)

    # Crear listas para Carlos López
    crear_lista("Tareas de Jardinería", "- Cortar el césped\n- Podar los arbustos\n- Regar las plantas\n- Limpiar la piscina", usuario2_id)
    crear_lista("Proyectos de Bricolaje", "- Pintar la sala de estar\n- Reparar la puerta del garaje\n- Construir una estantería\n- Instalar luces en el jardín", usuario2_id)
    crear_lista("Películas para Ver", "- El padrino\n- Ciudadano Kane\n- Casablanca\n- La lista de Schindler\n- El mago de Oz\n- Cantando bajo la lluvia", usuario2_id)
    crear_lista("Entrenamiento Semanal", "- Lunes: Cardio (30 min)\n- Martes: Pesas (1 hora)\n- Miércoles: Descanso\n- Jueves: Yoga (45 min)\n- Viernes: Natación (1 hora)", usuario2_id)
    crear_lista("Ideas de Negocio", "- Tienda online de productos artesanales\n- Consultoría de marketing digital\n- Clases de cocina a domicilio\n- Aplicación para organizar eventos", usuario2_id)

    # Crear listas para Sofía Martínez
    crear_lista("Planificación de Eventos", "- Fiesta de cumpleaños de Laura: 25/08, Salón de eventos 'La Fiesta'\n- Cena de empresa: 15/12, Restaurante 'El Rincón'\n- Boda de Ana y Juan: 05/09, Hacienda 'Los Olivos'", usuario3_id)
    crear_lista("Cursos Online", "- Marketing digital (Coursera)\n- Programación en Python (Udemy)\n- Fotografía profesional (Domestika)\n- Diseño gráfico (Platzi)", usuario3_id)
    crear_lista("Destinos de Viaje", "- Japón: Tokio, Kioto, Osaka\n- Italia: Roma, Florencia, Venecia\n- Grecia: Atenas, Santorini, Mykonos\n- Tailandia: Bangkok, Chiang Mai, Phuket", usuario3_id)
    crear_lista("Lista de Música", "- Rock: Queen, Led Zeppelin, The Beatles\n- Pop: Michael Jackson, Madonna, ABBA\n- Clásica: Beethoven, Mozart, Bach\n- Electrónica: Daft Punk, The Chemical Brothers, Kraftwerk", usuario3_id)
    crear_lista("Ideas para Decoración", "- Estilo minimalista: Colores neutros, muebles sencillos\n- Estilo rústico: Madera, piedra, colores cálidos\n- Estilo moderno: Líneas rectas, colores vibrantes\n- Estilo bohemio: Plantas, textiles coloridos, muebles vintage", usuario3_id)

    # Crear listas compartidas
    lista_compartida_todos_id = crear_lista("Lista de Anuncios", "- Reunión general: 10/06, 10:00 AM\n- Fecha límite para entrega de proyectos: 30/06\n- Celebración de aniversario de la empresa: 15/07", admin_id)
    lista_compartida_ana_carlos_id = crear_lista("Proyecto Conjunto", "- Fase 1: Investigación de mercado (Ana)\n- Fase 2: Desarrollo del producto (Carlos)\n- Fase 3: Lanzamiento del producto (Ana y Carlos)", usuario1_id)
    lista_compartida_carlos_sofia_id = crear_lista("Planificación de Viaje Grupal", "- Destino: Barcelona\n- Fechas: 01/08 - 08/08\n- Actividades: Visita a la Sagrada Familia, Parque Güell, Playa de la Barceloneta\n- Presupuesto: 1000€ por persona", usuario2_id)

    # Compartir listas
    compartir_lista(lista_compartida_todos_id, usuario1_id)
    compartir_lista(lista_compartida_todos_id, usuario2_id)
    compartir_lista(lista_compartida_todos_id, usuario3_id)

    compartir_lista(lista_compartida_ana_carlos_id, usuario2_id)

    compartir_lista(lista_compartida_carlos_sofia_id, usuario3_id)

    print("Base de datos poblada con éxito.")

if __name__ == "__main__":
    populate_database()
