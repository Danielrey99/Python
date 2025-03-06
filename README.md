# Mi Aprendizaje de Python 🐍

Este repositorio contiene mi progreso en Python, con ejercicios, proyectos y notas de aprendizaje.

## 📂 Contenido

- `fundamentos/` - Conceptos básicos de Python:
    - `01_variables/` - Declaración, tipos y operaciones con variables:
        - `variables.py` - Declaración, tipos y operaciones con variables.
        - `constantes.py` - Definición y uso de constantes.
        - `listas.py` - Trabajo con listas y sus métodos.
        - `diccionarios.py` - Trabajo con diccionarios y sus métodos.
    - `02_bucles/` - Estructuras de control de bucles:
        - `if.py` - Uso de la estructura condicional `if`.
        - `for.py` - Uso del bucle `for`.
        - `while.py` - Uso del bucle `while`.
        - `anidados.py` - Ejemplos de bucles anidados.
        - `match_case.py` - Ejemplos de bucles match case.
    - `03_funciones/` - Funciones en Python
        - `funciones.py` - Definición y uso de funciones.
    - `04_manejo_errores/` - Manejo de errores en Python:
        - `try_except.py` - Ejemplos de manejo de errores con `try-except`.
    - `05_clases/` - Programación Orientada a Objetos (POO) en Python:
        - `clases.py` - Definición y uso de clases y objetos.

- `ejercicios/` - Ejercicios prácticos para reforzar los conceptos aprendidos:
    - `calculadora.py` - Implementación de una calculadora.

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
   pip uninstall <nombre_del_paquete> # Desinstala un paquete específico
   pip install --upgrade <nombre_del_paquete> #Actualizar un paquete específico
   pip install -r requirements.txt # Instala paquetes desde un archivo requirements.txt

   pip list  # Lista los paquetes instalados en el entorno virtual
   pip freeze > requirements.txt # Crea un archivo requirements.txt con los paquetes instalados

   python.exe -m pip install --upgrade pip  # Actualiza pip