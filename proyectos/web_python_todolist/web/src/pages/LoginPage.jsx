import { useState } from 'react';
import RouteButton from '../components/RouteButton';
import Logo from '../components/Logo';
import styles from './General.module.css';
import { loginUsuario } from '../services/apiService';
import { validateLoginFields } from '../utils/validation';

function LoginPage() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [usernameError, setUsernameError] = useState('');
    const [passwordError, setPasswordError] = useState('');
    const [generalError, setGeneralError] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const errors = validateLoginFields(username, password);
        setUsernameError(errors.username);
        setPasswordError(errors.password);
        setGeneralError('');

        if (errors.username || errors.password) {
            return;
        }

        try {
            const data = await loginUsuario(username, password);
            localStorage.setItem('token', data.token);
            localStorage.setItem('username', data.usuario.nombre_usuario);
            localStorage.setItem('rol', data.usuario.rol);
            window.location.href = '/todolist';
        } catch (error) {
            console.error('Error en login:', error.message);
            alert(error.message);
        }
    };

    return (
        <div className={styles.formContainer}>
            <h1>ToDoList</h1>
            <Logo />
            <h2>Iniciar Sesión</h2>
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
                <button type="submit" className={styles.formButton}>Iniciar Sesión</button>
            </form>
            <RouteButton to="/register">Registrarse</RouteButton>
        </div>
    );
}

export default LoginPage;