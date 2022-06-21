abre el codigo un su editor favorito

Paso1: Instale virtualenv
py -m pip install virtualenv

Paso2: cree un entorno virtual
python -m venv env

paso3: activa el entorno virtual
--> cd env/scripts/
--> activate

paso4: vuelve a la carpeta principal
cd../..

paso5: instalar las librerias etc.
pip install -r requirements.txt

pso6: Correr el servidor
python manage.py runserver


Si no quiere tomarce la molestia de instalar el postgreSQL puede editar el codigo en:
core/settings.py
en la linea numero 93 y sustitur por este codigo para que funcione con una base de datos simple en sqlite

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }





