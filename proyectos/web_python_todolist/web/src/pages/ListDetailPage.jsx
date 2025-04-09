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
            <div className={styles.detailFullScreenContainer}>
                <div className={styles.detailMessageContainer}>
                    <div className={styles.detailError}>Error: {error}</div>
                </div>
            </div>
        );
    }

    if (!lista) {
        return (
            <div className={styles.detailFullScreenContainer}>
                <div className={styles.detailMessageContainer}>
                    <div className={styles.detailLoading}>
                        <Loader2 size={30} className={styles.detailLoaderIcon} />
                        Cargando lista...
                    </div>
                </div>
            </div>
        );
    }

    return (
        <div className={styles.detailContainer}>
            <h1 className={styles.detailTitle}>{lista.nombre_lista}</h1>
            <p className={styles.detailDescription}>
                {lista.descripcion ? lista.descripcion.split('\n').map((line, index) => (
                    <React.Fragment key={index}>
                        {line}
                        {index < lista.descripcion.split('\n').length - 1 && <br />}
                    </React.Fragment>
                )) : 'Sin descripción'}
            </p>

            <Link to="/todolist" className={styles.detailBackButton}>
                <ArrowLeft size={24} />
            </Link>
            <Link to={`/edit-list/${lista.id}`} className={styles.detailEditLink}>
                <Edit size={24} />
            </Link>
        </div>
    );
}

export default ListDetailPage;