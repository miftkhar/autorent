import os
from decouple import config
# import datetime
# pip install -e git+git://github.com/oscarmlage/django-cruds-adminlte/@0.0.17+git.082ac1b#egg=django-cruds-adminlte

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# BASE_DIR = C:\Users\Iftkhar\projects\django-apps\mycarapp
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


STATIC_ROOT = os.path.join(BASE_DIR, 'static')

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
    # 'imagekit',

    'api',
    'users',
    'vechiles',
    'django_filters',
    'treebeard',
    'rest_framework',
    # 'baton',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',


    'corsheaders',
    'rest_framework.authtoken',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_auth',
    'rest_auth.registration',
    'django.contrib.staticfiles',
    # 'baton.autodiscover',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'csp.middleware.CSPMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


]


# CSP_DEFAULT_SRC = ("'self'", "'unsafe-inline'", 'http://api.autorent.pk:9000',)
# CSP_STYLE_SRC = ("'self'", "'unsafe-inline'", 'http://api.autorent.pk:9000',)
# CSP_SCRIPT_SRC = ("'self'", "'unsafe-inline'", 'http://api.autorent.pk:9000',)
# CSP_IMG_SRC = ("'self'",)
# CSP_FONT_SRC = ("'self'",)
# CSP_CONNECT_SRC = ("'self'",)
# CSP_WORKER_SRC = ("'self'",)


ROOT_URLCONF = 'drfx.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)


ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_AUTHENTICATION_METHOD = 'email'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_EMAIL_FIELD = 'email'
ACCOUNT_LOGOUT_ON_GET = True

AUTH_USER_MODEL = 'users.CustomUser'

REST_AUTH_SERIALIZERS = {
    "USER_DETAILS_SERIALIZER": "users.serializers.CustomUserDetailsSerializer",
}
REST_AUTH_REGISTER_SERIALIZERS = {
    "REGISTER_SERIALIZER": "users.serializers.CustomRegisterSerializer",
}


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    # 'DEFAULT_RENDERER_CLASSES': (
    #     'rest_framework.renderers.JSONRenderer',
    # ),
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    # ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',

    'PAGE_SIZE': 20,

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

REST_SESSION_LOGIN = False
