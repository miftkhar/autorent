from .base import *
ALLOWED_HOSTS = ['127.0.0.1', 'localhost',
                 'api.autorent.pk', '165.22.254.232']

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

SECRET_KEY = '31&9*n_egoick%w+dv*1azf879u^^!uy4e9waib$qoje*y6c_@'

STATIC_ROOT = "/home/rentacar/autorent/static/"
STATIC_URL = '/static/'

#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_ROOT = "/home/rentacar/autorent/media/"
MEDIA_URL = 'api.autorent.pk/media/'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static/"),
#     '/home/rentacar/autorent/static/',
#     '/home/rentacar/autorent/',
# ]


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'sg2plcpnl0122.prod.sin2.secureserver.net'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'info@autorent.pk'
EMAIL_HOST_PASSWORD = 'XXXu5454'
DEFAULT_FROM_EMAIL = 'info@autorent.pk'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
