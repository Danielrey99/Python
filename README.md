# Mi Aprendizaje de Python 🐍

Este repositorio contiene mi progreso en Python, con ejercicios, proyectos y notas de aprendizaje.

## 📂 Contenido

- `fundamentos/` - Conceptos básicos de Python:
    - `01_variables/` - Declaración, tipos y operaciones con variables:
        - `constantes.py` - Definición y uso de constantes.
        - `listas.py` - Trabajo con listas y sus métodos.
        - `variables.py` - Declaración, tipos y operaciones con variables.

## 📖 ¿Por qué este repositorio?

Este repositorio me ayuda a documentar mi avance en Python y compartir lo que aprendo.

## 🚀 Cómo usarlo

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/miusuario/mirepo-python.git

## Entornos virtuales (.venv)

1. Creación del entorno virtual
   ```bash
   python -m venv .venv  # Crea un entorno virtual llamado .venv

   .\.venv\Scripts\activate  # Activa el entorno virtual windows
   source .venv/bin/activate  # Activa el entorno virtual linux/macOS
   deactivate  # Desactiva el entorno virtual

   pip install <nombre_del_paquete>  # Instala un paquete específico
   pip install pandas  # Ejemplo: instala pandas
   pip install --upgrade pandas #Actualizar pandas
   pip install -r requirements.txt # Instala paquetes desde un archivo requirements.txt

   pip list  # Lista los paquetes instalados en el entorno virtual
   pip freeze > requirements.txt # Crea un archivo requirements.txt con los paquetes instalados

   python.exe -m pip install --upgrade pip  # Actualiza pip