const API_URL = 'http://localhost:8000';

// Función genérica para manejar solicitudes fetch
async function handleResponse(response) {
    if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.message || 'Error en la solicitud');
    }
    return response.json();
}

function getToken() {
    return localStorage.getItem('token');
}

// Usuarios
export async function obtenerUsuarios() {
    const response = await fetch(`${API_URL}/usuarios`, {
        headers: {
            'Authorization': `Bearer ${getToken()}`
        }
    });
    return handleResponse(response);
}

export async function crearUsuario(nombre_usuario, contrasenha) {
    const response = await fetch(`${API_URL}/register`, {
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

export async function cambiarNombreUsuario(nuevo_nombre) {
    const response = await fetch(`${API_URL}/usuarios/cambiar_nombre`, {
        method: 'PUT',
        headers: { 
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${getToken()}`
        },
        body: JSON.stringify({ nuevo_nombre }),
    });
    return handleResponse(response);
}

export async function cambiarContrasenhaUsuario(contrasenha_actual, contrasenha_nueva) {
    const response = await fetch(`${API_URL}/usuarios/cambiar_contrasenha`, {
        method: 'PUT',
        headers: { 
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${getToken()}`
        },
        body: JSON.stringify({ contrasenha_actual, contrasenha_nueva }),
    });
    return handleResponse(response);
}

export async function cambiarRolUsuario(usuario_id, nuevo_rol) {
    const response = await fetch(`${API_URL}/usuarios/cambiar_rol`, {
        method: 'PUT',
        headers: { 
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${getToken()}`
        },
        body: JSON.stringify({ usuario_id, nuevo_rol }),
    });
    return handleResponse(response);
}

export async function eliminarUsuario() {
    const response = await fetch(`${API_URL}/usuarios/eliminar`, {
        method: 'DELETE',
        headers: {
            'Authorization': `Bearer ${getToken()}`
        }
    });
    return handleResponse(response);
}

// Listas
export async function obtenerListasUsuario() {
    const response = await fetch(`${API_URL}/listas`, {
        headers: {
            'Authorization': `Bearer ${getToken()}`
        }
    });
    return handleResponse(response);
}

export async function obtenerListaPorId(lista_id) {
    const response = await fetch(`${API_URL}/listas/id/${lista_id}`, {
        headers: {
            'Authorization': `Bearer ${getToken()}`
        }
    });
    return handleResponse(response);
}

export async function obtenerListasCompartidasUsuario() {
    const response = await fetch(`${API_URL}/listas/compartidas`, {
        headers: {
            'Authorization': `Bearer ${getToken()}`
        }
    });
    return handleResponse(response);
}

export async function crearLista(nombre_lista, descripcion) {
    const response = await fetch(`${API_URL}/listas`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${getToken()}`
        },
        body: JSON.stringify({ nombre_lista, descripcion }),
    });
    return handleResponse(response);
}

export async function actualizarLista(lista_id, nombre_lista, descripcion) {
    const response = await fetch(`${API_URL}/listas/actualizar`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${getToken()}`
        },
        body: JSON.stringify({ lista_id, nombre_lista, descripcion }),
    });
    return handleResponse(response);
}

export async function compartirLista(lista_id, usuario_id_compartir) {
    const response = await fetch(`${API_URL}/listas/compartir`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${getToken()}`
        },
        body: JSON.stringify({ lista_id, usuario_id_compartir }),
    });
    return handleResponse(response);
}

export async function eliminarLista(lista_id) {
    const response = await fetch(`${API_URL}/listas/eliminar/${lista_id}`, {
        method: 'DELETE',
        headers: {
            'Authorization': `Bearer ${getToken()}`
        }
    });
    return handleResponse(response);
}