import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { obtenerListasUsuario } from '../services/apiService';
import styles from './ToDoListPage.module.css';
import { Eye } from 'lucide-react';

function ToDoListPage() {
    const [listas, setListas] = useState([]);
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
        return <div className={styles.error}>Error: {error}</div>;
    }

    return (
        <div className={styles.container}>
            <h1 className={styles.title}>Mis Listas</h1>
            {listas.length > 0 ? (
                <table className={styles.table}>
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
                                    <Link to={`/list/${lista.id}`} className={styles.viewLink}>
                                        <Eye size={24} />
                                    </Link>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            ) : (
                <p className={styles.noLists}>No tienes listas creadas.</p>
            )}
        </div>
    );
}

export default ToDoListPage;