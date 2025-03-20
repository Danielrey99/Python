import logo from '../assets/logo.jpeg';
import styles from './Logo.module.css';

function Logo() {
    return <img src={logo} alt="Logo ToDoList" className={styles.logo} />;
}

export default Logo;