import { useState } from 'react';
import RouteButton from '../components/RouteButton';
import Logo from '../components/Logo';
import styles from './General.module.css';
import { loginUsuario } from '../services/apiService';

function LoginPage() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const data = await loginUsuario(username, password);
            console.log('Login exitoso:', data);
            localStorage.setItem('token', data.token);
            console.log('Token guardado en localStorage:', data.token);
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
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    className={styles.formInput}
                    placeholder="Nombre de usuario"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
                <input
                    type="password"
                    className={styles.formInput}
                    placeholder="Contraseña"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <button type="submit" className={styles.formButton}>Iniciar Sesión</button>
            </form>
            <RouteButton to="/register">Registrarse</RouteButton>
        </div>
    );
}

export default LoginPage;