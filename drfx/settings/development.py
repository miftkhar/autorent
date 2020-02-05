from .base import *
DEBUG = True
ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost']

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]


DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': "",
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}


# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'incremental': True,
#     'root': {
#         'level': 'DEBUG',
#     },
# }

LOGGING = {
    'version': 1,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
        }
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'sg2plcpnl0122.prod.sin2.secureserver.net'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'info@autorent.pk'
EMAIL_HOST_PASSWORD = 'XXXu5454'
DEFAULT_FROM_EMAIL = 'info@autorent.pk'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

# EMAIL_HOST = 'smtp.mailgun.org'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'postmaster@sandboxdbeda9cad0a946e8889a94bc17e72a42.mailgun.org'
# EMAIL_HOST_PASSWORD = 'b60ec0e7ea5597769803ab1492383829-2b4c5a6c-254441c0'
# #DEFAULT_FROM_EMAIL = 'donotreply@kamiltrojnar.pl'
# EMAIL_USE_TLS = True
