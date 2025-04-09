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
            navigate(`/list/${id}`);
        } catch (err) {
            setError(err.message);
            setLoading(false);
        }
    };

    if (loading) {
        return (
            <div className={styles.editFullScreenContainer}>
                <div className={styles.editMessageContainer}>
                    <div className={styles.editLoading}>
                        <Loader2 size={30} className={styles.editLoaderIcon} />
                        Cargando lista...
                    </div>
                </div>
            </div>
        );
    }

    if (error) {
        return (
            <div className={styles.editFullScreenContainer}>
                <div className={styles.editMessageContainer}>
                    <div className={styles.editError}>Error: {error}</div>
                </div>
            </div>
        );
    }

    return (
        <div className={styles.editContainer}>
            <h1 className={styles.editTitle}>Editar Lista</h1>
            <form onSubmit={handleSubmit}>
                <div className={styles.editFormGroup}>
                    <label htmlFor="nombreLista" className={styles.editLabel}>Nombre:</label>
                    <input
                        type="text"
                        id="nombreLista"
                        value={nombreLista}
                        onChange={(e) => setNombreLista(e.target.value)}
                        required
                        className={styles.editInput}
                    />
                </div>
                <div className={styles.editFormGroup}>
                    <label htmlFor="descripcion" className={styles.editLabel}>Descripción:</label>
                    <textarea
                        id="descripcion"
                        value={descripcion}
                        onChange={(e) => setDescripcion(e.target.value)}
                        className={styles.editTextarea}
                        rows="12"
                    />
                </div>
                <button type="submit" className={styles.editSaveButton}>
                    <Save size={24} className={styles.editIconMargin} /> Guardar Cambios
                </button>
            </form>
            <div className={styles.editLinksContainer}>
                <Link to="/todolist" className={styles.editBackButton}>
                    <ArrowLeft size={24} className={styles.editIconMargin} /> Volver a Mis Listas
                </Link>
                <Link to={`/list/${id}`} className={styles.editViewLink}>
                    <Eye size={24} className={styles.editIconMargin} /> Ver Detalles
                </Link>
            </div>
        </div>
    );
}

export default EditListPage;