import React from 'react';
import { Link } from 'react-router-dom';
import styles from './LinkButton.module.css';

function LinkButton({ to, children }) {
    return (
        <Link to={to} className={styles.linkButton}>
            {children}
        </Link>
    );
}

export default LinkButton;