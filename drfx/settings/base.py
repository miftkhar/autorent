import os
from decouple import config
# import datetime
# pip install -e git+git://github.com/oscarmlage/django-cruds-adminlte/@0.0.17+git.082ac1b#egg=django-cruds-adminlte

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "static"),
# )

STATIC_ROOT = 'static/'
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Application definition

INSTALLED_APPS = [

    # 'adminlteui',
    # 'cruds',

    # 'crispy_forms',
    # 'django_select2',
    # 'easy_thumbnails',
    # 'image_cropping',
    # 'django_ajax',
    # 'cruds_adminlte',


    'dal',
    'dal_select2',
    'imagekit',
    'baton',
    'api',
    'users',
    'vechiles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django_filters',
    'treebeard',

    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_auth',
    'rest_auth.registration',
    'django.contrib.staticfiles',
    'baton.autodiscover',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',

]


CSP_DEFAULT_SRC = ("'self'", 'http://165.22.254.232:9000/')
CSP_STYLE_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'",)
CSP_IMG_SRC = ("'self'",)
CSP_FONT_SRC = ("'self'",)


ROOT_URLCONF = 'drfx.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'drfx.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'incremental': True,
    'root': {
        'level': 'DEBUG',
    },
}
# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

AUTH_USER_MODEL = 'users.CustomUser'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'

SITE_ID = 1


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS':
        ['django_filters.rest_framework.DjangoFilterBackend']
}

# BATON = {
#     'SITE_HEADER': 'Rent A Car',
#     'SITE_TITLE': 'Rent A Car System',
#     'INDEX_TITLE': 'Site administration',
#     'SUPPORT_HREF': '',
#     'COPYRIGHT': 'copyright © 2017 ',  # noqa
#     'POWERED_BY': '',
#     'CONFIRM_UNSAVED_CHANGES': True,
#     'SHOW_MULTIPART_UPLOADING': True,
#     'ENABLE_IMAGES_PREVIEW': True,
#     'MENU': (
#         {'type': 'title', 'label': 'main', 'apps': ('auth', )},
#         {
#             'type': 'app',
#             'name': 'vechiles',
#             'label': 'Car',
#             'icon': 'fa fa-car',
#             # 'models': (
#             #     {
#             #         'name': 'user',
#             #         'label': 'Users'
#             #     },
#             #     {
#             #         'name': 'vechiles',
#             #         'label': 'Vehicles'
#             #     },
#             # )
#         },
#         {'type': 'title', 'label': 'Contents', 'apps': ('flatpages', )},
#         {'type': 'model', 'label': 'Pages', 'name': 'flatpage', 'app': 'flatpages'},
#         {'type': 'free', 'label': 'Users', 'url': '/admin/users/customuser/',
#             # 'perms': ('flatpages.add_flatpage', 'auth.change_user')
#         },
#         # {'type': 'free', 'label': 'My parent voice', 'children': [
#         #     {'type': 'model', 'label': 'A Model', 'name': 'mymodelname',
#         #         'app': 'myapp', 'icon': 'fa fa-gavel'},
#         #     {'type': 'free', 'label': 'Another custom link',
#         #         'url': 'http://www.google.it'},
#         # ]},
#     ),
#     # 'ANALYTICS': {
#     #     'CREDENTIALS': os.path.join(BASE_DIR, 'credentials.json'),
#     #     'VIEW_ID': '12345678',
#     # }
# }

CRISPY_TEMPLATE_PACK = 'bootstrap3'
# Django_debug_toolbar settings
INTERNAL_IPS = ('127.0.0.1',)
# THUMBNAIL_PROCESSORS = (
#     'image_cropping.thumbnail_processors.crop_corners',
# ) + thumbnail_settings.THUMBNAIL_PROCESSORS

TIME_FORMAT = 'h:i A'
DATETIME_FORMAT = 'd/m/Y H:i:s'
DATE_FORMAT = "d/m/Y"

TIME_INPUT_FORMATS = ['%I:%M %p']


IMAGE_CROPPING_JQUERY_URL = None

CORS_ORIGIN_ALLOW_ALL = True
#CORS_ALLOW_CREDENTIALS = False

# CORS_ORIGIN_WHITELIST = [
#     'http://165.22.254.232:9000',
# ]
# CORS_ORIGIN_REGEX_WHITELIST = [
#     'http://165.22.254.232:9000',
# ]

CORS_REPLACE_HTTPS_REFERER = True


CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken',
    'accept-encoding'
)

CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS'
)
