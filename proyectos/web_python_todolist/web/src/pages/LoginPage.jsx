import { useState } from 'react';
import Input from '../components/Input';
import Button from '../components/Button';
import LinkButton from '../components/LinkButton';
import Logo from '../components/Logo';
import styles from './LoginPage.module.css';

function LoginPage() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        // Aquí irán las peticiones a la API para el login
        console.log('Login:', { email, password });
    };

    return (
        <div className={styles.loginContainer}>
            <h1>ToDoList</h1>
            <Logo />
            <h2>Iniciar Sesión</h2>
            <form onSubmit={handleSubmit}>
                <Input
                    type="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
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