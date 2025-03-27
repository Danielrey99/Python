import React from 'react';
import { Link } from 'react-router-dom';
import styles from './RouteButton.module.css';

function RouteButton({ to, children }) {
    return (
        <Link to={to} className={styles.routeButton}>
            {children}
        </Link>
    );
}

export default RouteButton;