import { useState } from 'react';
import RouteButton from '../components/RouteButton';
import Logo from '../components/Logo';
import styles from './General.module.css';
import { crearUsuario } from '../services/apiService';
import { validateUsername, validatePassword } from '../utils/validation';

function RegisterPage() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [usernameError, setUsernameError] = useState('');
    const [passwordError, setPasswordError] = useState('');
    const [generalError, setGeneralError] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const usernameErrorMsg = validateUsername(username);
        const passwordErrorMsg = validatePassword(password);

        setUsernameError(usernameErrorMsg);
        setPasswordError(passwordErrorMsg);
        setGeneralError('');

        if (usernameErrorMsg || passwordErrorMsg) {
            return;
        }

        try {
            await crearUsuario(username, password);
            alert('Registro exitoso. Ahora puedes iniciar sesión.');
            window.location.href = '/login';
        } catch (error) {
            console.error('Error al registrar usuario:', error.message);
            alert(error.message);
        }
    };

    return (
        <div className={styles.formContainer}>
            <h1>ToDoList</h1>
            <Logo />
            <h2>Registrarse</h2>
            <div className={styles.formErrorContainer}>
                {generalError && <p className={styles.formError}>{generalError}</p>}
            </div>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    className={styles.formInput}
                    placeholder="Nombre de usuario"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
                <div className={styles.formErrorContainer}>
                    {usernameError && <p className={styles.formError}>{usernameError}</p>}
                </div>
                <input
                    type="password"
                    className={styles.formInput}
                    placeholder="Contraseña"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <div className={styles.formErrorContainer}>
                    {passwordError && <p className={styles.formError}>{passwordError}</p>}
                </div>
                <button type="submit" className={styles.formButton}>Registrarse</button>
            </form>
            <RouteButton to="/login">Iniciar Sesión</RouteButton>
        </div>
    );
}

export default RegisterPage;