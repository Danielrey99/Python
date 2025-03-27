const API_URL = 'http://localhost:8000'; // Ajusta la URL si es necesario

// Función genérica para manejar solicitudes fetch
async function handleResponse(response) {
    if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.message || 'Error en la solicitud');
    }
    return response.json();
}

// Usuarios
export async function obtenerUsuarios() {
    const response = await fetch(`${API_URL}/usuarios`);
    return handleResponse(response);
}

export async function crearUsuario(nombre_usuario, contrasenha) {
    const response = await fetch(`${API_URL}/usuarios`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ nombre_usuario, contrasenha }),
    });
    return handleResponse(response);
}

export async function loginUsuario(nombre_usuario, contrasenha) {
    const response = await fetch(`${API_URL}/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ nombre_usuario, contrasenha }),
    });
    return handleResponse(response);
}

export async function cambiarNombreUsuario(usuario_id, nuevo_nombre) {
    const response = await fetch(`${API_URL}/usuarios/cambiar_nombre/${usuario_id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ nuevo_nombre }),
    });
    return handleResponse(response);
}

export async function cambiarContrasenhaUsuario(usuario_id, contrasenha_actual, contrasenha_nueva) {
    const response = await fetch(`${API_URL}/usuarios/cambiar_contrasenha/${usuario_id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ contrasenha_actual, contrasenha_nueva }),
    });
    return handleResponse(response);
}

export async function cambiarRolUsuario(usuario_id, nuevo_rol) {
    const response = await fetch(`${API_URL}/usuarios/cambiar_rol/${usuario_id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ nuevo_rol }),
    });
    return handleResponse(response);
}

export async function eliminarUsuario(usuario_id) {
    const response = await fetch(`${API_URL}/usuarios/eliminar/${usuario_id}`, {
        method: 'DELETE',
    });
    return handleResponse(response);
}

// Listas
export async function obtenerListasUsuario(usuario_id) {
    const response = await fetch(`${API_URL}/listas/${usuario_id}`);
    return handleResponse(response);
}

export async function obtenerListaPorId(lista_id) {
    const response = await fetch(`${API_URL}/listas/id/${lista_id}`);
    return handleResponse(response);
}

export async function obtenerListasCompartidasUsuario(usuario_id) {
    const response = await fetch(`${API_URL}/listas/compartidas/${usuario_id}`);
    return handleResponse(response);
}

export async function crearLista(nombre_lista, descripcion, usuario_id) {
    const response = await fetch(`${API_URL}/listas`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ nombre_lista, descripcion, usuario_id }),
    });
    return handleResponse(response);
}

export async function actualizarLista(lista_id, nombre_lista, descripcion) {
    const response = await fetch(`${API_URL}/listas/actualizar/${lista_id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ nombre_lista, descripcion }),
    });
    return handleResponse(response);
}

export async function compartirLista(lista_id, usuario_id_compartir) {
    const response = await fetch(`${API_URL}/listas/compartir`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ lista_id, usuario_id_compartir }),
    });
    return handleResponse(response);
}

export async function eliminarLista(lista_id) {
    const response = await fetch(`${API_URL}/listas/eliminar/${lista_id}`, {
        method: 'DELETE',
    });
    return handleResponse(response);
}