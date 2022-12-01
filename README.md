# TP_INTEGRADOR
Aqui realizaremos el trabajo- RED DE BUS


Primer paso entrar a tu entorno virtual y instalar los requirements con pip install -r requirements.txt


Luego tienes que abrir otra terminal y entrar en su  cliente mysql y crear una base de datos llamada SERVICIO_BUS


Luego tienes que modificar el archivo settings.py y modificar el USER y PASSWORD

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



y por ultimo desde la terminal y adentro del proyecto ejecutar python3 manage.py runserver






