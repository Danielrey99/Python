// Register
export function validateUsername(username) {
    if (!username) {
        return 'El nombre de usuario es obligatorio.';
    }
    if (username.length < 3) {
        return 'El nombre de usuario debe tener al menos 3 caracteres.';
    }
    if (username.length > 50) {
        return 'El nombre de usuario no puede tener más de 50 caracteres.';
    }
    return '';
}

export function validatePassword(password) {
    if (!password) {
        return 'La contraseña es obligatoria.';
    }
    if (password.length < 8) {
        return 'La contraseña debe tener al menos 8 caracteres.';
    }
    if (password.length > 72) {
        return 'La contraseña no puede tener más de 72 caracteres.';
    }
    if (!/[0-9]/.test(password)) {
        return 'La contraseña debe contener al menos un número.';
    }
    if (!/[A-Z]/.test(password)) {
        return 'La contraseña debe contener al menos una letra mayúscula.';
    }
    return '';
}

// Login
export function validateLoginFields(username, password) {
    const errors = {
        username: '',
        password: '',
    };

    if (!username) {
        errors.username = 'El nombre de usuario es obligatorio.';
    }

    if (!password) {
        errors.password = 'La contraseña es obligatoria.';
    }

    return errors;
}