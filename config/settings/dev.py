from config.settings.base import *

SECRET_KEY = 'h%)=4k%r15h&1s39hqwd*b!uf=nnn2e3&%$dt3zi5hz5#h718-'
DEBUG = True
ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['PSQL_NAME'],
        'USER': os.environ['PSQL_USERNAME'],
        'PASSWORD': os.environ['PSQL_PASSWORD'],
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

MIDDLEWARE += [

    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INSTALLED_APPS += [

    'django_extensions',
    'django.contrib.staticfiles',
    'debug_toolbar',

    ]


INTERNAL_IPS = [

    '127.0.0.1', 'localhost',
]

