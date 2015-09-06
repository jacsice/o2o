#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
Django settings for wei project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket

SITE_ID = 1

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xq)ve7w-mt+1nh99=k@xa@=+fbum3j9bsw=mfutx+vzdrr^t_g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = DEBUG

ATOMIC_REQUESTS = True

LOGIN_URL = '/accounts/login/'

ALLOWED_HOSTS = ['*']

ADMINS = (
    ('zhangbo', '413761980@qq.com'),
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'shoes',
    'wechat',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    #'common.middleware.UserRestrictMiddleware',
    #'common.middleware.ApiLogMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    #'config.context_processors.functions',
    #'config.context_processors.undone_messages',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django.contrib.auth.backends.RemoteUserBackend',
)

ROOT_URLCONF = 'want.urls'

WSGI_APPLICATION = 'want.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Chongqing'

USE_I18N = True

USE_L10N = True

# USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
STATIC_ROOT = os.path.join(os.path.join(BASE_DIR, ".."), 'static')


STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, os.path.join(os.pardir, "media"))

MEDIA_URL = "/media/"

# email
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# DEFAULT_FROM_EMAIL = 'cfpamf@cfpamf.org.cn'
# EMAIL_HOST = 'smtpcom.263xmail.com'
# EMAIL_PORT = 25
# EMAIL_HOST_USER = 'if@cfpamf.org.cn'
# EMAIL_HOST_PASSWORD = 'zhnxif@2014@SYS'

#SERVER_EMAIL = 'noreply@xiangxin.org.cn'
#EMAIL_HOST = 'smtp.exmail.qq.com'
#EMAIL_PORT = 25
#EMAIL_HOST_USER = 'noreply@xiangxin.org.cn'
#EMAIL_HOST_PASSWORD = 'zhnxif@2014'
# EMAIL_USE_TLS = True
#DEFAULT_FROM_EMAIL = 'noreply@xiangxin.org.cn'

EMAIL_SUBJECT_PREFIX = '[django][%s]' % socket.gethostname()

SITE_ID = 1

LANGUAGES = [
    ('zh-cn', 'Chinese'),
]

# logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(funcName)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        # 'special': {
        #     '()': 'project.logging.SpecialFilter',
        #     'foo': 'bar',
        # }
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false']
        },
        'debug': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/want_debug.log'),
            'formatter': 'verbose',
        },
        'info': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/want_info.log'),
            'formatter': 'verbose',
        },
        'err': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/want_err.log'),
            'formatter': 'verbose',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'debug': {
            'handlers': ['debug'],
            'level': 'DEBUG',
        },
        'info': {
            'handlers': ['info'],
            'level': 'INFO',
        },
        'err': {
            'handlers': ['err'],
            'level': 'ERROR',
        },
    }
}


SESSION_COOKIE_AGE = 60 * 60 * 2
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# django-celery
#CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'
#BROKER_URL = 'redis://localhost:6379/0'
CELERY_DISABLE_RATE_LIMITS = True

try:
    from local_settings import *
except ImportError:
    pass
