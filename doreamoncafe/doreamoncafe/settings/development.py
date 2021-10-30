from .base import *


# Application definition
INSTALLED_APPS = INBUILT_APPS + THIRD_PARTY_APPS + CUSTOM_APPS

# Middleware Definition
MIDDLEWARE = CREATED_REQUEST_MIDDLEWARES + CREATED_MIDDLEWARES + \
    DEFAULT_MIDDLEWARES + CREATED_RESPONSE_MIDDLEWARES

DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_USER_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),

        # https://django-mysql.readthedocs.io/en/latest/checks.html#django-mysql-w003-utf8mb4
        'OPTIONS': {
            # Tell MySQLdb to connect with 'utf8mb4' character set
            'charset': 'utf8mb4',
        },
        # Tell Django to build the test database with the 'utf8mb4' character set
        'TEST': {
            'CHARSET': 'utf8mb4',
            'COLLATION': 'utf8mb4_unicode_ci',
        }
    }
}