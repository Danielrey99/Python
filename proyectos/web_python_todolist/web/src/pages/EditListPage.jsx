import React, { useEffect, useState } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import { obtenerListaPorId, actualizarLista } from '../services/apiService';
import styles from './EditListPage.module.css';
import { Loader2, ArrowLeft, Save, Eye } from 'lucide-react';

function EditListPage() {
    const { id } = useParams();
    const navigate = useNavigate();
    const [nombreLista, setNombreLista] = useState('');
    const [descripcion, setDescripcion] = useState('');
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        async function cargarLista() {
            try {
                const data = await obtenerListaPorId(id);
                setNombreLista(data.nombre_lista);
                setDescripcion(data.descripcion || '');
                setLoading(false);
            } catch (err) {
                setError(err.message);
                setLoading(false);
            }
        }
        cargarLista();
    }, [id]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError(null);
        try {
            await actualizarLista(id, nombreLista, descripcion);
            navigate(`/list/${id}`); // Redirigir a ListDetailPage después de la actualización
        } catch (err) {
            setError(err.message);
            setLoading(false);
        }
    };

    if (loading) {
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

    if (error) {
        return (
            <div className={styles.fullScreenContainer}>
                <div className={styles.messageContainer}>
                    <div className={styles.error}>Error: {error}</div>
                </div>
            </div>
        );
    }

    return (
        <div className={styles.container}>
            <h1 className={styles.title}>Editar Lista</h1>
            <form onSubmit={handleSubmit}>
                <div className={styles.formGroup}>
                    <label htmlFor="nombreLista">Nombre:</label>
                    <input
                        type="text"
                        id="nombreLista"
                        value={nombreLista}
                        onChange={(e) => setNombreLista(e.target.value)}
                        required
                    />
                </div>
                <div className={styles.formGroup}>
                    <label htmlFor="descripcion">Descripción:</label>
                    <textarea
                        id="descripcion"
                        value={descripcion}
                        onChange={(e) => setDescripcion(e.target.value)}
                    />
                </div>
                <button type="submit" className={styles.saveButton}>
                    <Save size={24} className={styles.iconMargin} /> Guardar Cambios
                </button>
            </form>
            <div className={styles.linksContainer}>
                <Link to="/todolist" className={styles.backButton}>
                    <ArrowLeft size={24} className={styles.iconMargin} /> Volver a Mis Listas
                </Link>
                <Link to={`/list/${id}`} className={styles.viewLink}>
                    <Eye size={24} className={styles.iconMargin} /> Ver Detalles
                </Link>
            </div>
        </div>
    );
}

export default EditListPage;