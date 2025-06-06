import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { obtenerListasUsuario } from '../services/apiService';
import styles from './ToDoListPage.module.css';
import { Eye, Loader2, Edit } from 'lucide-react';

function ToDoListPage() {
    const [listas, setListas] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        async function cargarListas() {
            try {
                const data = await obtenerListasUsuario();
                setListas(data);
            } catch (err) {
                setError(err.message);
            }
        }

        cargarListas();
    }, []);

    if (error) {
        return (
            <div className={styles.todoErrorContainer}>
                <div className={styles.todoMessageContainer}>
                    <div className={styles.todoError}>Error: {error}</div>
                </div>
            </div>
        );
    }

    if (!listas) {
        return (
            <div className={styles.todoErrorContainer}>
                <div className={styles.todoMessageContainer}>
                    <div className={styles.todoLoading}>
                        <Loader2 size={30} className={styles.todoLoaderIcon} />
                        Cargando listas...
                    </div>
                </div>
            </div>
        );
    }

    return (
        <div className={styles.todoContainer}>
            <h1 className={styles.todoTitle}>Mis Listas</h1>
            {listas.length > 0 ? (
                <table className={styles.todoTable}>
                    <thead>
                        <tr>
                            <th>Nombre</th>
                            <th>Fecha de Creación</th>
                            <th>Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        {listas.map(lista => (
                            <tr key={lista.id}>
                                <td>{lista.nombre_lista}</td>
                                <td>{new Date(lista.fecha_creacion).toLocaleDateString()}</td>
                                <td>
                                    <Link to={`/list/${lista.id}`} className={styles.todoViewLink}>
                                        <Eye size={24} />
                                    </Link>
                                    <Link to={`/edit-list/${lista.id}`} className={styles.todoEditLink}>
                                        <Edit size={24} />
                                    </Link>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            ) : (
                <p className={styles.todoNoLists}>No tienes listas creadas.</p>
            )}
        </div>
    );
}

export default ToDoListPage;