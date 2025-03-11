CREATE DATABASE todo_list_db;

CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre_usuario VARCHAR(50) UNIQUE NOT NULL,
    contrasenha VARCHAR(100) NOT NULL,
    rol VARCHAR(20) NOT NULL DEFAULT 'usuario',
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE usuarios ADD CONSTRAINT chk_rol CHECK (rol IN ('usuario', 'admin'));

CREATE TABLE listas (
    id SERIAL PRIMARY KEY,
    nombre_lista VARCHAR(100) NOT NULL,
    descripcion TEXT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE usuario_lista (
    usuario_id INT REFERENCES usuarios(id),
    lista_id INT REFERENCES listas(id),
    PRIMARY KEY (usuario_id, lista_id)
);