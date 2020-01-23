from .base import *
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'api.autorent.pk', '58.65.176.42']

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

DEBUG = False

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'autosale',
        'USER': 'autorent',
        'PASSWORD': 'rent@Car',
        'HOST': '127.0.0.1',
        # 'PORT': "",
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'postmaster@sandboxdbeda9cad0a946e8889a94bc17e72a42.mailgun.org'
EMAIL_HOST_PASSWORD = 'b60ec0e7ea5597769803ab1492383829-2b4c5a6c-254441c0'
EMAIL_USE_TLS = True

SECRET_KEY = '31&9*n_egoick%w+dv*1azf879u^^!uy4e9waib$qoje*y6c_@'

#STATIC_ROOT = "/home/rentacar/autorent/static/"
STATIC_URL = '/static/'

#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_ROOT = "/home/rentacar/autorent/"
MEDIA_URL = 'http://api.autorent.pk:9000/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static/"),
    '/home/rentacar/autorent/static/',
    '/home/rentacar/autorent/',
]
