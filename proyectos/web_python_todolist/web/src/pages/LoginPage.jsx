import { useState } from 'react';
import Input from '../components/Input';
import Button from '../components/Button';
import LinkButton from '../components/LinkButton';
import Logo from '../components/Logo';
import styles from './LoginPage.module.css';
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
            window.location.href = '/todolist';
        } catch (error) {
            console.error('Error en login:', error.message);
            alert(error.message);
        }
        console.log('Login:', { username, password });
    };

    return (
        <div className={styles.loginContainer}>
            <h1>ToDoList</h1>
            <Logo />
            <h2>Iniciar Sesión</h2>
            <form onSubmit={handleSubmit}>
                <Input
                    type="text"
                    placeholder="Nombre de usuario"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
                <Input
                    type="password"
                    placeholder="Contraseña"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <Button type="submit">Iniciar Sesión</Button>
            </form>
            <LinkButton to="/register">Registrarse</LinkButton>
        </div>
    );
}

export default LoginPage;