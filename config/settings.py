# pylint: disable-all
"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
# pylint: disable-all
from pathlib import Path
from django.conf import settings
import os
import posixpath
import dj_database_url
import environ

# Environment variables

from six import python_2_unicode_compatible
import django.utils.encoding
django.utils.encoding.python_2_unicode_compatible = python_2_unicode_compatible
import collections.abc
import sys
from collections.abc import MutableSet




env = environ.Env()
environ.Env.read_env()


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#BASE_DIR = Path(__file_).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "o!ld8nrt4vc*h1zoey*wj48x*q0#ss12h=+zh)kk^6b3aygg=!"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# change the default user models to our custom model
AUTH_USER_MODEL = "accounts.User"

# Application definition

DJANGO_APPS = [
    "jet.dashboard",
    "jet",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
   #s "advanced_filters"
  #  "postgressql.connector.django",

]

# Third party apps
THIRD_PARTY_APPS = [
    "crispy_forms",
    "rest_framework",
   
]

# Custom apps
PROJECT_APPS = [
    "app.apps.AppConfig",
    "accounts.apps.AccountsConfig",
    "course.apps.CourseConfig",
    "result.apps.ResultConfig",
    "search.apps.SearchConfig",
    "quiz.apps.QuizConfig",
    "payments.apps.PaymentsConfig",
    "crispy_bootstrap4",
     'preventconcurrentlogins',
     
]

# Combine all apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE = [
    "whitenoise.Middleware.whitenoiseMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
     'preventconcurrentlogins.middleware.PreventConcurrentLoginsMiddleware',
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # 'django.template.context_processors.i18n',
                # 'django.template.context_processors.media',
                # 'django.template.context_processors.static',
                # 'django.template.context_processors.tz',
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

ASGI_APPLICATION = "config.asgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# -----------------------------
# NOTE: Some model fields may not work on sqlite db,
# so consider using postgresql instead



DATABASES = {
    
    'default':dj_database_url.parse(env('DATABASE_URL'))
      
      #  'default':{
       
     # 'ENGINE' :'django.db.backends.postgresql',
     #   'NAME' :'king',
     #   'USER':'postgres',
     #  'PASSWORD' : 'Dembe@12',
     #  'HOST' :'localhost',
     #  'PORT' :'5432',

  # }
      
     

    }
    
    






# https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-DEFAULT_AUTO_FIELD
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"
MEDIA_URL = "/media/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),

    
]




MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
#STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ["staticfiles"]))

# -----------------------------------
# E-mail configuration

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = (
    "smtp.gmail.com"  # Here lojs xogb twex tjst i'm using gmail as the email host, but you can change it
)
EMAIL_PORT = 465
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "kktshipala@gmail.com"
EMAIL_HOST_PASSWORD = "lojsxogbtwextjst"

# crispy config
CRISPY_TEMPLATE_PACK = "bootstrap4"

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# DRF setup
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
}

# Strip payment config
#STRIPE_SECRET_KEY = env("STRIPE_SECRET_KEY")
#STRIPE_PUBLISHABLE_KEY = env("STRIPE_PUBLISHABLE_KEY")


#AWS_ACCESS_KEY_ID ="AKIAU6GD3B4R6IKQGUDR"
##AWS_SECRET_ACCESS_KEY ="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"
#AWS_STORAGE_BUCKET_NAME ="backendbucketlms"
#AWS_S3_SIGNATURE_NAME ="s3v4"
#AWS_S3_REGION_NAME ="us-east-1"
#AWS_S3_FILE_OVERWRITE ="False"
#AWS_DEFAULT_AC ="None"
#AWS_S3_VERITY ="True"
#DEFAULT_FILE_STORAGE ="storeges.backends.s3botos.S3Boto3Storage"
