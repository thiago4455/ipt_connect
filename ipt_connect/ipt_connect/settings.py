"""
Django settings for ipt_connect project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'XXX'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SERVER_EMAIL = 'XXX'

ADMINS = (('XXX', 'XXX@XXX'),)

ALLOWED_HOSTS = [u"*"]

# Place all the names of the tournaments here
# Default tournament (i.e. the one displayed on the main page) should be the first

INSTALLED_TOURNAMENTS = (
    'BPT',
)

# Application definition

INSTALLED_APPS = (
    'grappelli',
    'solo.apps.SoloAppConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
) + INSTALLED_TOURNAMENTS

MIGRATION_MODULES = dict(
    [(app, app + '.migrations.' + app) for app in INSTALLED_TOURNAMENTS]
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #    'django.middleware.security.SecurityMiddleware',
    #'ipt_connect.URLLocaleMiddleWare.URLLocaleMiddleware',
)

ROOT_URLCONF = 'ipt_connect.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
        'DIRS': [os.path.join(BASE_DIR, 'templates').replace('\\', '/')],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            # List of callables that know how to import templates from various sources.
            'loaders': (
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                # 'django.template.loaders.eggs.Loader',
            ),
        },
    },
]

WSGI_APPLICATION = 'ipt_connect.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'pt-br'

LOCALE_PATHS = (os.path.join('locale'),)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join('', 'static')
MEDIA_ROOT = os.path.join(os.getcwd(), 'media/')
MEDIA_URL = '/media/'

CACHES = {
    'default': {
        # 	'BACKEND': 'django.core.cache.backends.dummy.DummyCache', # Switch the cache off
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

SOLO_CACHE = 'default'
SOLO_CACHE_TIMEOUT = 5 * 60

DEFAULT_AUTO_FIELD='django.db.models.AutoField' 

try:
    from ipt_connect.local_settings import *
except ImportError:
    pass
