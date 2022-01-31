# django_app_gestion
Este proyecto hace parte de una prueba para un sistema de control de acceso a sedes ( puntos de acceso ) para personal
de empresas.

# ejecución:

-clone this repo:
    git@github.com:gabrielbarragan/django_app_gestion.git

# Readme

# Mis sedes app:

Este proyecto hace parte de una prueba para un sistema de control de acceso a sedes ( puntos de acceso ) para personal de una organización y sus sedes.

## Ejecución:

- clona el repositorio:
    
    ### ssh:
    
    `git clone git@github.com:gabrielbarragan/django_app_gestion.git`
    
    ### http:
    
    `git clone https://github.com/gabrielbarragan/django_app_gestion.git`
    
- Crea el entorno virtual para python y sus librerías.
- inicia el entorno virtual.
- Instalar las librerías desde el archivo requirements.txt:
    
    `pip install requirements.txt`
    
- Copia el contenido del archivo **.envexample.**
- Dentro de la carpeta **server/control_sedes** crea un archivo llamado **.env**  y allí pega el contenido del archivo **.envexample.** Cambia los valores encerrados en << >>
    
    ```
    DEBUG=True
    SECRET_KEY=<<Your_Django_secret_key>>
    DATABASE_URL=
    SQLITE_URL=sqlite:///my-local-sqlite.db
    USER_EMAIL=<<Your_email_for_test>>
    USER_EMAIL_PASSWORD= <<Your email password>>
    ```
    
- En la consola, crea primero un superusuario:
    
    `python manage.py createsuperuser`
    

## Funcionamiento de la API:

para el correcto funcionamiento de la API se debe crear una organización, una o más sedes y una o más tablas de horarios.

### endpoints:

**POST:**

requiere token de autorización

/api/v1/token/login/ → Obtener token

/api/v1/users/ → crear un nuevo usuario 

/api/v1/organizations/ → crear una nueva empresa.

/api/v1/organizations/{int: organization_id}/headquarters/ → crear una nueva sede.

/api/v1/timetables/ → crear un nuevo horario

### **/api/v1/users/headquarters/access/ → solicitar acceso a una sede**

**GET:**

requieren token de autorización

/api/v1/users/ → listar usuarios 

/api/v1/users/{int: user_id}/ → listar detalles de un determinado usuario.

/api/v1/organizations/ → listar todas las empresas.

/api/v1/organizations/{int: organization_id}/ → listar detalles de una determinada empresa.

/api/v1/organizations/{int: organization_id}/headquarters/ → listar las sedes de una empresa.

/api/v1/organizations/{int: organization_id}/headquarters/{int: headquarter_id}/ → Detalles de una sede especifica.

/api/v1/timetables/ → Listar todos los horarios

/api/v1/timetables/{int: timetable_id}/ → Listar detalles de un determinado horario
