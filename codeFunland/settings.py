"""
Django settings for codeFunland project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

from django.core.urlresolvers import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r=*drq0hfqu(ac##rsi)^ct1rq28@8vk^sql)u32=c$9vo4-*k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'start',
    'users',
    'courses',
    'labs',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'codeFunland.urls'

WSGI_APPLICATION = 'codeFunland.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'HOST': "localhost",
        'NAME': "codeUtopia",
        'USER': "code",
        'PASSWORD': "123456",
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# If user isn't logged in , redirect to the below address
LOGIN_URL = reverse_lazy("users:user_login", args=[])


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_PATH = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    STATIC_PATH,
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
TEMPLATE_DIRS = [
    TEMPLATE_PATH,
]


# Loggin config

LOG_FILE_PATH = r"/tmp/log_codeUtopia.log"
LOGGING = {
    "version" : 1,
    "disable_existing_loggers": True,
    "formatters": {
        "verbose": {
            "format": "<%(asctime)s> %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            "datefmt": "%d-%b-%Y %H:%M:%S"
        },
        "simple": {
            "format": "---%(levelname)s %(message)s\n"
        },
    },
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": LOG_FILE_PATH,
            "formatter": "verbose"
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple"
        },
        "error": {
            "level": "ERROR",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_FILE_PATH,
            "formatter": "simple"
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "propagate": True,
            "level": "DEBUG"
        },
        "views_error": {
            "handlers": ["console", "file"],
            "propagate": False,
            "level": "ERROR"
        },
    },
}
