# Proyecto Evaluación 3 - Tienda Django


## Funcionalidades
* Catálogo de productos con categorías y buscador.
* Filtro para ordenar productos por precio (menor/mayor).
* Formulario para hacer pedidos y subir imágenes de referencia.
* Sistema de seguimiento usando un código único.
* Panel de administración para gestionar insumos, productos y pedidos.

# Cómo instalar y ejecutar

## 1. Clona este repositorio:

Bash
git clone https://github.com/TrickyXIII/BackEnd-tercera-evaluacion

## 2. Entrar a la carpeta:

[Bash]
cd BackEnd-tercera-evaluacion

## 3. Crea y activa tu entorno virtual:

python -m venv venv

### Si usas Git Bash
source venv/Scripts/activate

### Si usas Windows:
venv\Scripts\activate

### Si usas Mac/Linux:
source venv/bin/activate

## 4. Instalar lo necesario:

pip install -r requirements.txt

## 5. Preparar la base de datos:

python manage.py migrate

## 6. Enciende el servidor:

python manage.py runserver


# Datos de acceso:

Página principal: http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin/

Usuario: admin

Clave: admin

# Instrucciones de Deploy (Render)

Este proyecto está configurado para desplegarse fácilmente en Render.

## Pasos para el despliegue:

1.  **Crear servicio:**
    * Entra a [Render.com](https://render.com/) y crea un "New Web Service".
    * Conecta tu repositorio de GitHub.

2.  **Configuración:**
    Usa los siguientes comandos al configurar el servicio:

    * **Runtime:** Python 3
    * **Build Command:**
        ```bash
        pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
        ```
    * **Start Command:**
        ```bash
        gunicorn core.wsgi:application
        ```

3.  **Crear Administrador (Superusuario):**
    Una vez que el sitio esté en línea ("Live"):
    * Ve a la pestaña **"Shell"** en el panel de Render.
    * Ejecuta el siguiente comando y sigue las instrucciones:
        ```bash
        python manage.py createsuperuser
        ```
