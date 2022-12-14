"""
Django settings for MaterialsSystem project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'syy+*^lf6bx6gsebu2-2sh43k^sxk(*&h5^8v=7fh4%(l9y5l)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "simpleui",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'ckeditor',
    'apps.local_library.apps.LocalLibraryConfig',
    'apps.center_library.apps.CenterLibraryConfig',
    'apps.home.apps.HomeConfig',
    'apps.material_application.apps.MaterialApplicationConfig',
    'corsheaders',
    # "easy_pdf"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'home.middleware.MyMiddle',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MaterialsSystem.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'MaterialsSystem.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

if DEBUG:
    BASE_URL = "http://127.0.0.1:8000/"
    pdfkit_path = "/usr/local/bin/wkhtmltopdf"
    PASSWORD = "root123456"
# else:
#     BASE_URL = "https://fywzgl.oilhb.com/"
#     pdfkit_path = r"C:\Softwares\wkhtmltopdf\bin\wkhtmltopdf.exe"
#     PASSWORD = "hh@200196"

BASE_URL = "http://127.0.0.1:8000/"
pdfkit_path = "/usr/local/bin/wkhtmltopdf"
PASSWORD = "root123456"

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',  # ????????????mysql?????????
        'NAME': 'materials_system_bak',  # ???????????????????????????
        'HOST': '127.0.0.1',  # ????????????ip??????
        'USER': 'root',  # ?????????????????????
        'PASSWORD': PASSWORD,  # ???????????????
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        "OPTIONS": {
            "min_length": 12
        }
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
    {
        'NAME': 'home.backends.MyNumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, "static")

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

# ?????????????????????????????????
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

SIMPLEUI_HOME_INFO = False
SIMPLEUI_ANALYSIS = False
SIMPLEUI_HOME_ACTION = False # ?????????????????????
SIMPLEUI_HOME_QUICK = True  # ????????????????????????
base_path = "upload/"

status_choices_dict = {
    "1": "?????????????????????",
    "2": "???????????????",
    "3": "?????????????????????",
    "4": "????????????",
    "5": "?????????",
}
status_choices = []
for _k, _v in status_choices_dict.items():
    status_choices.append((_k, _v))

CORS_ORIGIN_ALLOW_ALL = True
# ??????????????????
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = ()

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    "x-ajax",
    "Access-Control-Allow-Headers",
    "CORS",
    "*"
)

LOGGING = {
    'version': 1,
    'disable_existing_logger': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s \"%(pathname)s???%(module)s:%(funcName)s:%(lineno)d\" [%(levelname)s]-%(message)s]'
        },
    },
    # ?????????
    'handlers': {
        # ???????????????
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        # ????????????
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'logs/default.log',
            'formatter': 'verbose',
            # ????????????????????????
            'when': 'M',
            # ????????????
            'interval': 2,
            # ??????15?????????
            'backupCount': 15,
            'encoding': 'utf-8'
        },
    },
    # ?????????
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagete': True,
        },
    }
}
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/home/index/'
