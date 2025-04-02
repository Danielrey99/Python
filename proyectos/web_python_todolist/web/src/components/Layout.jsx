// Layout.jsx
import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import styles from './Layout.module.css';
import { Menu, X } from 'lucide-react';

function Layout({ children }) {
    const username = localStorage.getItem('username');
    const [menuOpen, setMenuOpen] = useState(false);

    const handleLogout = () => {
        localStorage.clear();
        window.location.href = '/login';
    };

    return (
        <div className={styles.layoutContainer}>
            {/* Sidebar */}
            <aside className={`${styles.sidebar} ${menuOpen ? styles.open : ''}`}>
                <button className={styles.menuButton} onClick={() => setMenuOpen(!menuOpen)}>
                    {menuOpen ? <X size={24} /> : <Menu size={24} />}
                </button>
                <nav className={styles.nav}>
                    <Link to="/todolist" onClick={() => setMenuOpen(false)}>📋 Listas</Link>
                    <Link to="/create-list" onClick={() => setMenuOpen(false)}>➕ Crear Lista</Link>
                    <Link to="/edit-lista" onClick={() => setMenuOpen(false)}>✏️ Modificar Lista</Link>
                    <Link to="/user" onClick={() => setMenuOpen(false)}>👤 Mi Perfil</Link>
                    {localStorage.getItem('rol') === 'admin' && (
                        <Link to="/admin" onClick={() => setMenuOpen(false)}>⚙️ Usuarios</Link>
                    )}
                </nav>
            </aside>

            {/* Contenido principal */}
            <div className={styles.mainContent}>
                <header className={styles.header}>
                    <div className={styles.userInfo}>
                        <span>{username}</span>
                        <button className={styles.logoutButton} onClick={handleLogout}>Cerrar Sesión</button>
                    </div>
                </header>
                <main className={styles.content}>{children}</main>
            </div>
        </div>
    );
}

export default Layout;