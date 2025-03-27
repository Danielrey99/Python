import { useState } from 'react';
import RouteButton from '../components/RouteButton';
import Logo from '../components/Logo';
import styles from './General.module.css';
//import { crearUsuario } from '../services/apiService';

function RegisterPage() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
    };

    return (
        <div className={styles.formContainer}>
            <h1>ToDoList</h1>
            <Logo />
            <h2>Registrarse</h2>
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
                <button type="submit" className={styles.formButton}>Registrarse</button>
            </form>
            <RouteButton to="/login">Iniciar Sesión</RouteButton>
        </div>
    );
}

export default RegisterPage;