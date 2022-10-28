# TP_INTEGRADOR
Aqui realizaremos el trabajo- RED DE BUS




Para poder ejecutar el programa debes instalar las requirements con pip install -r requirements.txt



Luego tienes que runear el archivo DATABASES.txt en mysql para crear la base de datos



Luego tienes que modificar el archivo settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'SERVICIO_BUS',
        'USER': 'tu nombre de mysql',
        'PASSWORD': 'contraseña',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}   







luego ejecuta el archivo index.py y ingresa a https://localhost:5000/login
