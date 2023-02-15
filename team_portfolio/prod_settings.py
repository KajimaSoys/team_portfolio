import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = False
ALLOWED_HOSTS = ['www.kajimacode.com', 'kajimacode.con', '127.0.0.1']

SECRET_KEY = os.environ.get('SECRET_KEY')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'team_portfolio',
        'USER': 'postgres',
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


STATIC_ROOT = os.path.join(BASE_DIR, "static")

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True