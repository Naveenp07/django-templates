# settings/common.py
import environ
from pathlib import Path

# Root directory
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
env = environ.Env()

# DEBUG
DEBUG = env.bool("DJANGO_DEBUG", False)

# Apps
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'widget_tweaks',
]

LOCAL_APPS = [
    'users',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Must come before auth
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Must be after sessions
    'django.contrib.messages.middleware.MessageMiddleware',     # Must be after auth
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'
WSGI_APPLICATION = 'myproject.wsgi.application'

# Database (SQLite default)
DATABASES = {
    'default': env.db("DATABASE_URL", default=f"sqlite:///{ROOT_DIR}/db.sqlite3"),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ROOT_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Static & Media
STATIC_URL = '/static/'
STATIC_ROOT = ROOT_DIR / 'staticfiles'
STATICFILES_DIRS = [ROOT_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = ROOT_DIR / 'media'

# Time & Language
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Auth
AUTH_USER_MODEL = 'users.Person'
LOGIN_URL = '/users/login/'

# Admin
ADMIN_URL = 'admin/'

# Default primary key type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

