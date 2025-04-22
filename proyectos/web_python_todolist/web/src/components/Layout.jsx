import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import styles from './Layout.module.css';
import { Menu, X, LogOut } from 'lucide-react';

function Layout({ children }) {
    const username = localStorage.getItem('username');
    const [menuOpen, setMenuOpen] = useState(false);

    const handleLogout = () => {
        localStorage.clear();
        window.location.href = '/login';
    };

    return (
        <div className={styles.layoutContainer}>
            <aside className={`${styles.sidebar} ${menuOpen ? styles.open : ''}`}>
                <nav className={styles.nav}>
                    <Link to="/todolist" onClick={() => setMenuOpen(false)}>📋 Listas</Link>
                    <Link to="/shared-lists" onClick={() => setMenuOpen(false)}>👥 Listas Compartidas</Link>
                    <Link to="/create-list" onClick={() => setMenuOpen(false)}>➕ Crear Lista</Link>
                    <Link to="/user" onClick={() => setMenuOpen(false)}>👤 Mi Perfil</Link>
                    {localStorage.getItem('rol') === 'admin' && (
                        <Link to="/admin" onClick={() => setMenuOpen(false)}>⚙️ Usuarios</Link>
                    )}
                </nav>
            </aside>

            <div className={`${styles.mainContent} ${menuOpen ? styles.shifted : ''}`}>
                <header className={styles.header}>
                    <button className={styles.menuButton} onClick={() => setMenuOpen(!menuOpen)}>
                        {menuOpen ? <X size={30} /> : <Menu size={30} />}
                    </button>

                    <div className={styles.userInfo}>
                        <span className={styles.username}>{username}</span>
                        <button className={styles.logoutButton} onClick={handleLogout}>
                            <LogOut size={24} />
                        </button>
                    </div>
                </header>
                <main className={styles.content}>{children}</main>
            </div>
        </div>
    );
}

export default Layout;
