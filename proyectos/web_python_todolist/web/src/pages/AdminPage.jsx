import React, { useState, useEffect } from 'react';
import { obtenerUsuarios, cambiarRolUsuario } from '../services/apiService';
import styles from './AdminPage.module.css';
import { User, ShieldUser, Loader2 } from 'lucide-react';

function AdminPage() {
    const [usuarios, setUsuarios] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        async function cargarUsuarios() {
            try {
                const data = await obtenerUsuarios();
                setUsuarios(data);
            } catch (err) {
                setError(err.message);
            }
        }
        cargarUsuarios();
    }, []);

    const handleRolChange = async (usuarioId, rolActual) => {
        const nuevoRol = rolActual === 'usuario' ? 'admin' : 'usuario';
        try {
            await cambiarRolUsuario(usuarioId, nuevoRol);
            setUsuarios(usuarios.map(usuario =>
                usuario.id === usuarioId ? { ...usuario, rol: nuevoRol } : usuario
            ));
        } catch (err) {
            setError(err.message);
        }
    };

    if (error) {
        return (
            <div className={styles.adminErrorContainer}>
                <div className={styles.adminMessageContainer}>
                    <div className={styles.adminError}>Error: {error}</div>
                </div>
            </div>
        );
    }

    if (!usuarios) {
        return (
            <div className={styles.adminErrorContainer}>
                <div className={styles.adminMessageContainer}>
                    <div className={styles.adminLoading}>
                        <Loader2 size={30} className={styles.adminLoaderIcon} />
                        Cargando usuarios...
                    </div>
                </div>
            </div>
        );
    }

    return (
        <div className={styles.adminContainer}>
            <h1>Administración de Usuarios</h1>
            <table className={styles.adminTable}>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Nombre de Usuario</th>
                        <th>Rol</th>
                        <th>Fecha de Registro</th>
                        <th>Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    {usuarios.map(usuario => (
                        <tr key={usuario.id}>
                            <td>{usuario.id}</td>
                            <td>{usuario.nombre_usuario}</td>
                            <td>{usuario.rol}</td>
                            <td>{new Date(usuario.fecha_registro).toLocaleDateString()}</td>
                            <td>
                                {usuario.id != Number(localStorage.getItem('userId')) && (
                                    <button
                                        onClick={() => handleRolChange(usuario.id, usuario.rol)}
                                        className={styles.cambiarRolButton}
                                    >
                                        {usuario.rol === 'usuario' ? <User size={20} /> : <ShieldUser size={20} />}
                                    </button>
                                )}
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default AdminPage;