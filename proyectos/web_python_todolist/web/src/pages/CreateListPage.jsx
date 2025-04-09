import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { crearLista } from '../services/apiService';
import styles from './CreateListPage.module.css';
import { ArrowLeft, Save } from 'lucide-react';

function CreateListPage() {
    const navigate = useNavigate();
    const [nombreLista, setNombreLista] = useState('');
    const [descripcion, setDescripcion] = useState('');
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError(null);
        try {
            const nuevaLista = await crearLista(nombreLista, descripcion);
            navigate(`/list/${nuevaLista.id}`);
        } catch (err) {
            setError(err.message);
            setLoading(false);
        }
    };

    if (loading) {
        return (
            <div className={styles.createFullScreenContainer}>
                <div className={styles.createMessageContainer}>
                    <div className={styles.createLoading}>
                        Cargando...
                    </div>
                </div>
            </div>
        );
    }

    if (error) {
        return (
            <div className={styles.createFullScreenContainer}>
                <div className={styles.createMessageContainer}>
                    <div className={styles.createError}>Error: {error}</div>
                </div>
            </div>
        );
    }

    return (
        <div className={styles.createContainer}>
            <h1 className={styles.createTitle}>Crear Nueva Lista</h1>
            <form onSubmit={handleSubmit}>
                <div className={styles.createFormGroup}>
                    <label htmlFor="nombreLista" className={styles.createLabel}>Nombre:</label>
                    <input
                        type="text"
                        id="nombreLista"
                        value={nombreLista}
                        onChange={(e) => setNombreLista(e.target.value)}
                        required
                        className={styles.createInput}
                    />
                </div>
                <div className={styles.createFormGroup}>
                    <label htmlFor="descripcion" className={styles.createLabel}>Descripción:</label>
                    <textarea
                        id="descripcion"
                        value={descripcion}
                        onChange={(e) => setDescripcion(e.target.value)}
                        className={styles.createTextarea}
                        rows="10"
                    />
                </div>
                <button type="submit" className={styles.createSaveButton}>
                    <Save size={24} className={styles.createIconMargin} /> Crear Lista
                </button>
            </form>
            <div className={styles.createLinksContainer}>
                <Link to="/todolist" className={styles.createBackButton}>
                    <ArrowLeft size={24} className={styles.createIconMargin} /> Volver a Mis Listas
                </Link>
            </div>
        </div>
    );
}

export default CreateListPage;