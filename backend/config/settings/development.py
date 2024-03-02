from datetime import timedelta

from .base import *

SECRET_KEY = 'django-insecure-5lu5o1*h$q74+$&q9kb&tshm+a#3m8#jpw9a7bvpe_g&lt5=p$'

DEBUG = True

ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        
    ],
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}