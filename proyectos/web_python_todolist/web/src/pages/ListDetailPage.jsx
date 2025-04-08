import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { obtenerListaPorId } from '../services/apiService';
import styles from './ListDetailPage.module.css';
import { Loader2, Edit, ArrowLeft } from 'lucide-react';

function ListDetailPage() {
    const { id } = useParams();
    const [lista, setLista] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        async function cargarLista() {
            try {
                const data = await obtenerListaPorId(id);
                setLista(data);
            } catch (err) {
                setError(err.message);
            }
        }

        cargarLista();
    }, [id]);

    if (error) {
        return (
            <div className={styles.fullScreenContainer}>
                <div className={styles.messageContainer}>
                    <div className={styles.error}>Error: {error}</div>
                </div>
            </div>
        );
    }

    if (!lista) {
        return (
            <div className={styles.fullScreenContainer}>
                <div className={styles.messageContainer}>
                    <div className={styles.loading}>
                        <Loader2 size={30} className={styles.loaderIcon} />
                        Cargando lista...
                    </div>
                </div>
            </div>
        );
    }

    return (
        <div className={styles.container}>
            <h1 className={styles.title}>{lista.nombre_lista}</h1>
            <p className={styles.description}>{lista.descripcion || 'Sin descripción'}</p>

            <Link to="/todolist" className={styles.backButton}>
                <ArrowLeft size={24} />
            </Link>
            <Link to={`/edit-list/${lista.id}`} className={styles.editLink}>
                <Edit size={24} />
            </Link>
        </div>
    );
}

export default ListDetailPage;
