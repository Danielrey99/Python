# Mi Aprendizaje de Python 🐍

Este repositorio contiene mi progreso en Python, con ejercicios, proyectos y notas de aprendizaje.

## 📂 Contenido

- `fundamentos/` - **Conceptos básicos de Python**:
    - `01_variables/` - **Declaración, tipos y operaciones con variables**
        - `variables.py` - Declaración, tipos y operaciones con variables.
        - `constantes.py` - Definición y uso de constantes.
        - `listas.py` - Trabajo con listas y sus métodos.
        - `diccionarios.py` - Trabajo con diccionarios y sus métodos.
    - `02_bucles/` - **Estructuras de control de bucles**
        - `if.py` - Uso de la estructura condicional `if`.
        - `for.py` - Uso del bucle `for`.
        - `while.py` - Uso del bucle `while`.
        - `anidados.py` - Ejemplos de bucles anidados.
        - `match_case.py` - Ejemplos de bucles match case.
    - `03_funciones/` - **Funciones en Python**
        - `funciones.py` - Definición y uso de funciones.
    - `04_manejo_errores/` - **Manejo de errores en Python**
        - `try_except.py` - Ejemplos de manejo de errores con `try-except`.
    - `05_clases/` - **Programación Orientada a Objetos (POO) en Python**
        - `clases.py` - Definición y uso de clases y objetos.

- `ejercicios/` - **Ejercicios prácticos para reforzar los conceptos aprendidos**
    - `calculadora.py` - Implementación de una calculadora.

- `proyectos/` - **Proyectos prácticos desarrollados con Python**
    - `web_python_todolist/` - Aplicación web de lista de tareas desarrollada con Python y React.

- `.gitignore` - Archivo para ignorar archivos y carpetas en Git.
- `README.md` - Documentación del proyecto.

## 📂 web_python_todolist
- `web_python_todolist/` - Contiene el código fuente de la aplicación web, así como la API que la soporta:
    - `api/` - **Lógica de la API REST**
        - `__init__.py`
        - `index.html` - Vista de la api con documentación básica.
        - `main.py` - Punto de entrada para la API.
        - `services.py` - Gestiona la interacción entre modelos y la base de datos.
        - `routes.py` - Definición de las rutas de la API.
        - `models/` - **Modelos de la base de datos para la API**
            - `__init__.py`
            - `lista.py` - Modelo para gestionar listas en la API.
            - `usuario.py` - Modelo para gestionar usuarios en la API.
        - `database/` - **Configuración y conexión a la base de datos**
            - `__init__.py`
            - `db.py` - Conexión y configuración de la base de datos.

    - `web/` - **Interfaz de usuario creada con React y Vite**
        - `node_modules/` - Dependencias de Node.js.
        - `public/` - Archivos públicos (HTML, imágenes, etc.).
        - `src/` - **Código fuente de la aplicación React**
            - `assets/` - Recursos estáticos (imágenes, SVG, etc.).
            - `components/Auth/` - **Componentes de autenticación**
                - `Login.jsx` - Componente para el inicio de sesión.
                - `Register.jsx` - Componente para el registro de usuarios.
            - `pages/` - **Páginas de la aplicación**
                - `LoginPage.jsx` - Página de inicio de sesión.
                - `RegisterPage.jsx` - Página de registro de usuarios.
            - `routes/` - **Configuración de rutas**
                - `AppRoutes.jsx` - Configuración de rutas de la aplicación.
            - `services/` - **Servicios de la aplicación**
                - `apiService.jsx` - Servicio para interactuar con la API.
            - `globalStyles.css` - Estilos globales de la aplicación.
            - `main.jsx` - Punto de entrada de la aplicación.
        - `.gitignore` - Archivo para ignorar archivos y carpetas en Git.
        - `index.html` - Página HTML principal.
        - `package.json` - Configuración del proyecto Node.js.
        - `package-lock.json` - Versiones exactas de las dependencias.
        - `vite.config.js` - Configuración de Vite.
        - `README.md` - Documentación de la aplicación React.

    - `sql_files/` - **Scripts SQL para la base de datos**
        - `V1__create_tables.sql` - Script SQL para crear las tablas de la base de datos.

    - `tests/` - **Pruebas unitarias y de integración para la API y la web**
        - `test_db.py` - Pruebas unitarias para la conexión a la base de datos.
        - `test_services.py` - Pruebas unitarias para los servicios de la API.

    - `.env` - Archivo para almacenar variables de entorno sensibles.
    - `populate_db.py` - Archivo para intoducir datos básicos en la base de datos.
    - `requirements.txt` - Lista de dependencias del proyecto.

## 🚀 Cómo usarlo (web_python_todolist)

1. Clonar el repositorio
    ```
    git clone [https://github.com/miusuario/mirepo-python.git](https://github.com/miusuario/mirepo-python.git)
    ```

2. Navegar al directorio del proyecto
    ```
    cd proyectos
    cd web_python_todolist
    ```

3. Crear y activar un entorno virtual
    ```
    python -m venv .venv
    .venv\Scripts\activate
    ```

4. Instalar las dependencias del proyecto
    ```
    pip install -r requirements.txt
    ```

5. Configurar la base de datos
    * Asegúrate de tener PostgreSQL instalado y configurado.
    * Crea una base de datos en PostgreSQL para el proyecto usando los archivos en sql_files.
    * Crea un archivo .env para guardar las variables de entorno con las credenciales de tu base de datos.
    Ejemplo:
    ```
    DB_HOST=localhost
    DB_PORT=5432
    DB_NAME=todolist
    DB_USER=tu_usuario
    DB_PASSWORD=tu_contraseña
    ```
    * Ejecutar populate_db para intoducir datos básicos en la base de datos.

6. Iniciar la API
    * Ejecuta el servidor de la API
        ```
        python -m api.main
        ```
    * La API estará disponible en http://localhost:8000.
    * Control + C parar la ejecucion de la api

7. Iniciar la aplicación React:
    * Navega al directorio `web`:
        ```
        cd web
        ```
    * Instala las dependencias de Node.js:
        ```
        npm install
        ```
    * Ejecuta el servidor de desarrollo de React:
        ```
        npm run dev
        ```
    * La aplicación estará disponible en `http://localhost:5173` (o el puerto que Vite asigne).
    * Presiona `Ctrl + C` para detener la ejecución de la aplicación React.

### Entornos virtuales (.venv)

1. Creación del entorno virtual
    ```
    python -m venv .venv  # Crea un entorno virtual llamado .venv

    .venv\Scripts\activate  # Activa el entorno virtual windows
    source .venv/bin/activate  # Activa el entorno virtual linux/macOS
    deactivate  # Desactiva el entorno virtual

    pip install <nombre_del_paquete>  # Instala un paquete específico
    pip uninstall <nombre_del_paquete> # Desinstala un paquete específico
    pip install --upgrade <nombre_del_paquete> #Actualizar un paquete específico

    pip list  # Lista los paquetes instalados en el entorno virtual
    pip freeze > requirements.txt # Crea un archivo requirements.txt con los paquetes instalados
    pip install -r requirements.txt # Instala paquetes desde un archivo requirements.txt
    pip uninstall -y -r requirements.txt # Elimina los paquetes que hay en el archivo

    python.exe -m pip install --upgrade pip  # Actualiza pip
    ```

### React + Vite + Javascript

1. Creación del proyecto React usando Vite:
    * Navega al directorio donde quieres crear tu proyecto React.
    * Ejecuta el siguiente comando para crear un proyecto React con Vite:
    ```
    npm create vite@latest
    ```
        * `npm create vite@latest`: Inicia el proceso de creación interactiva de un proyecto Vite.
        * Sigue las instrucciones en la terminal para:
            * Darle un nombre a tu proyecto (por ejemplo, `web`).
            * Seleccionar `React` como framework.
            * Seleccionar `JavaScript + SWC` como variante.
    * Navega a la carpeta del proyecto:
        ```
        cd web
        ```
    * Instala las dependencias del proyecto:
        ```
        npm install
        ```
        * Este comando instala todas las librerías necesarias especificadas en `package.json`.

2.  Iniciar el servidor de desarrollo:
    * Ejecuta el siguiente comando para iniciar el servidor de desarrollo de Vite:
        ```
        npm run dev
        ```
    * La aplicación estará disponible en `http://localhost:5173` (o el puerto que Vite asigne).
    * Presiona `Ctrl + C` en la terminal para detener el servidor.

3.  Instalar dependencias adicionales:
    * Para instalar una librería o paquete adicional, usa el siguiente comando:
        ```
        npm install <nombre_del_paquete>
        ```
        * Reemplaza `<nombre_del_paquete>` con el nombre de la librería que quieres instalar (ej: `npm install react-router-dom`).


### Test unitarios

1. Ejecutar tests
    ```
    python -m unittest <nombre_del_archivo_test> # Ejecutar un test específico
    python -m unittest discover # Busca los archivos que comiencen con test_ en el directorio actual y ejecutará las pruebas que contengan
    ```
