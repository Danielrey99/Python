import { useState } from 'react';
import Input from '../components/Input';
import Button from '../components/Button';
import LinkButton from '../components/LinkButton';
import Logo from '../components/Logo';
import styles from './RegisterPage.module.css';

function RegisterPage() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        // Aquí irán las peticiones a la API para el registro
        console.log('Registro:', { email, password });
    };

    return (
        <div className={styles.registerContainer}>
            <h1>ToDoList</h1>
            <Logo />
            <h2>Registrarse</h2>
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
                <Button type="submit">Registrarse</Button>
            </form>
            <LinkButton to="/login">Iniciar Sesión</LinkButton>
        </div>
    );
}

export default RegisterPage;