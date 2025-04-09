import React, { useEffect, useState } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import { obtenerListaPorId, eliminarLista } from '../services/apiService';
import styles from './ListDetailPage.module.css';
import { Loader2, Edit, ArrowLeft, Trash2 } from 'lucide-react';

function ListDetailPage() {
    const { id } = useParams();
    const navigate = useNavigate();
    const [lista, setLista] = useState(null);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        async function cargarLista() {
            try {
                const data = await obtenerListaPorId(id);
                setLista(data);
                setLoading(false);
            } catch (err) {
                setError(err.message);
                setLoading(false);
            }
        }

        cargarLista();
    }, [id]);

    const handleDelete = async () => {
        if (window.confirm("¿Estás seguro de que quieres eliminar esta lista?")) {
            setLoading(true);
            try {
                await eliminarLista(id);
                navigate('/todolist');
            } catch (err) {
                setError(err.message);
                setLoading(false);
            }
        }
    };

    if (loading) {
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

    if (error) {
        return (
            <div className={styles.detailFullScreenContainer}>
                <div className={styles.detailMessageContainer}>
                    <div className={styles.detailError}>Error: {error}</div>
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

            <div className={styles.detailActionsContainer}>
                <Link to="/todolist" className={styles.detailBackButton}>
                    <ArrowLeft size={24} />
                </Link>
                <button onClick={handleDelete} className={styles.detailDeleteButton}>
                    <Trash2 size={24} />
                </button>
                <Link to={`/edit-list/${lista.id}`} className={styles.detailEditLink}>
                    <Edit size={24} />
                </Link>
            </div>
        </div>
    );
}

export default ListDetailPage;