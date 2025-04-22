import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { obtenerListasCompartidasUsuario } from '../services/apiService';
import styles from './ToDoListPage.module.css';
import { Eye, Loader2, Edit } from 'lucide-react';

function SharedListsPage() {
    const [sharedLists, setSharedLists] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        async function cargarListasCompartidas() {
            try {
                const data = await obtenerListasCompartidasUsuario();
                setSharedLists(data);
            } catch (err) {
                setError(err.message);
            }
        }

        cargarListasCompartidas();
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

    if (!sharedLists) {
        return (
            <div className={styles.todoErrorContainer}>
                <div className={styles.todoMessageContainer}>
                    <div className={styles.todoLoading}>
                        <Loader2 size={30} className={styles.todoLoaderIcon} />
                        Cargando listas compartidas...
                    </div>
                </div>
            </div>
        );
    }

    return (
        <div className={styles.todoContainer}>
            <h1 className={styles.todoTitle}>Listas Compartidas Conmigo</h1>
            {sharedLists.length > 0 ? (
                <table className={styles.todoTable}>
                    <thead>
                        <tr>
                            <th>Nombre</th>
                            <th>Fecha de Creación</th>
                            <th>Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        {sharedLists.map(lista => (
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
                <p className={styles.todoNoLists}>No se han compartido listas contigo.</p>
            )}
        </div>
    );
}

export default SharedListsPage;