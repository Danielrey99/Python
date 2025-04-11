import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { cambiarNombreUsuario, cambiarContrasenhaUsuario, eliminarUsuario } from '../services/apiService';
import styles from './UserPage.module.css';
import { Save, Trash2, KeyRound } from 'lucide-react';
import { validateUsername, validatePassword } from '../utils/validation';

function UserPage() {
    const navigate = useNavigate();
    const [nuevoNombre, setNuevoNombre] = useState('');
    const [contrasenhaActual, setContrasenhaActual] = useState('');
    const [contrasenhaNueva, setContrasenhaNueva] = useState('');
    const [nuevoNombreError, setNuevoNombreError] = useState('');
    const [contrasenhaActualError, setContrasenhaActualError] = useState('');
    const [contrasenhaNuevaError, setContrasenhaNuevaError] = useState('');
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleCambiarNombre = async (e) => {
        e.preventDefault();
        const nuevoNombreErrorMsg = validateUsername(nuevoNombre);
        setNuevoNombreError(nuevoNombreErrorMsg);

        if (nuevoNombreErrorMsg) {
            return;
        }

        setLoading(true);
        setError(null);
        try {
            await cambiarNombreUsuario(nuevoNombre);
            setLoading(false);
            alert('Nombre de usuario cambiado con éxito.');
        } catch (err) {
            setError(err.message);
            setLoading(false);
        }
    };

    const handleCambiarContrasenha = async (e) => {
        e.preventDefault();
        const contrasenhaActualErrorMsg = validatePassword(contrasenhaActual);
        const contrasenhaNuevaErrorMsg = validatePassword(contrasenhaNueva);

        setContrasenhaActualError(contrasenhaActualErrorMsg);
        setContrasenhaNuevaError(contrasenhaNuevaErrorMsg);

        if (contrasenhaActualErrorMsg || contrasenhaNuevaErrorMsg) {
            return;
        }

        setLoading(true);
        setError(null);
        try {
            await cambiarContrasenhaUsuario(contrasenhaActual, contrasenhaNueva);
            setLoading(false);
            alert('Contraseña cambiada con éxito.');
        } catch (err) {
            setError(err.message);
            setLoading(false);
        }
    };

    const handleEliminarUsuario = async () => {
        if (window.confirm('¿Estás seguro de que quieres eliminar tu cuenta?')) {
            setLoading(true);
            setError(null);
            try {
                await eliminarUsuario();
                localStorage.removeItem('token');
                navigate('/login');
                window.location.reload();
            } catch (err) {
                setError(err.message);
                setLoading(false);
            }
        }
    };

    if (loading) {
        return (
            <div className={styles.userFullScreenContainer}>
                <div className={styles.userMessageContainer}>
                    <div className={styles.userLoading}>Cargando...</div>
                </div>
            </div>
        );
    }

    if (error) {
        return (
            <div className={styles.userFullScreenContainer}>
                <div className={styles.userMessageContainer}>
                    <div className={styles.userError}>Error: {error}</div>
                </div>
            </div>
        );
    }

    return (
        <div className={styles.userContainer}>
            <h1 className={styles.userTitle}>Configuración de Usuario</h1>

            <button onClick={handleEliminarUsuario} className={styles.userDeleteButton}>
                <Trash2 size={24} className={styles.userIconMargin} /> Eliminar Cuenta
            </button>

            <div className={styles.userChangeNameContainer}>
                <form onSubmit={handleCambiarNombre}>
                    <div className={styles.userFormGroup}>
                        <label htmlFor="nuevoNombre" className={styles.userLabel}>Nuevo Nombre de Usuario:</label>
                        <input
                            type="text"
                            id="nuevoNombre"
                            value={nuevoNombre}
                            onChange={(e) => setNuevoNombre(e.target.value)}
                            required
                            className={styles.userInput}
                        />
                        <div className={styles.userValidationErrorContainer}>
                            {nuevoNombreError && <p className={styles.userValidationErrorMessage}>{nuevoNombreError}</p>}
                        </div>
                    </div>
                    <div className={styles.userButtonContainer}>
                        <button type="submit" className={styles.userSaveButton}>
                            <Save size={24} className={styles.userIconMargin} /> Cambiar Nombre
                        </button>
                    </div>
                </form>
            </div>

            <div className={styles.userChangePasswordContainer}>
                <form onSubmit={handleCambiarContrasenha}>
                    <div className={styles.userFormGroup}>
                        <label htmlFor="contrasenhaActual" className={styles.userLabel}>Contraseña Actual:</label>
                        <input
                            type="password"
                            id="contrasenhaActual"
                            value={contrasenhaActual}
                            onChange={(e) => setContrasenhaActual(e.target.value)}
                            required
                            className={styles.userInput}
                        />
                        <div className={styles.userValidationErrorContainer}>
                            {contrasenhaActualError && <p className={styles.userValidationErrorMessage}>{contrasenhaActualError}</p>}
                        </div>
                    </div>
                    <div className={styles.userFormGroup}>
                        <label htmlFor="contrasenhaNueva" className={styles.userLabel}>Nueva Contraseña:</label>
                        <input
                            type="password"
                            id="contrasenhaNueva"
                            value={contrasenhaNueva}
                            onChange={(e) => setContrasenhaNueva(e.target.value)}
                            required
                            className={styles.userInput}
                        />
                        <div className={styles.userValidationErrorContainer}>
                            {contrasenhaNuevaError && <p className={styles.userValidationErrorMessage}>{contrasenhaNuevaError}</p>}
                        </div>
                    </div>
                    <div className={styles.userButtonContainer}>
                        <button type="submit" className={styles.userSaveButton}>
                            <KeyRound size={24} className={styles.userIconMargin} /> Cambiar Contraseña
                        </button>
                    </div>
                </form>
            </div>
        </div>
    );
}

export default UserPage;