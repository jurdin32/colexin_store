import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'b*$3ks#26-whr*t$%%scwq6uo*)j1ojuapf$6l+e^w($4)ml@x'
DEBUG = True

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'users',
    'carts',
    'orders',
    'charges',
    'products',
    'categories',
    'promo_codes',
    'billing_profiles',
    'shipping_addresses',
    'colexin',
    'store',
    'Pais',
    'Blogs',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'colexin_store.urls'

AUTH_USER_MODEL = 'users.User'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates']
        ,
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

WSGI_APPLICATION = 'colexin_store.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


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


LANGUAGE_CODE = 'es-EC'

TIME_ZONE = 'America/Guayaquil'

USE_I18N = True

USE_L10N = True

USE_TZ = True

from decouple import config

EMAIL_HOST = 'smtp.googlemail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'colexin.ec@gmail.com'
EMAIL_HOST_PASSWORD = '03101989Colexin'
EMAIL_USE_TLS = True

STRIPE_PUBLIC_KEY = 'pk_test_LzoUtMexhaFhO4Jg2yansHBJ00Bvkss2FD'
STRIPE_PRIVATE_KEY = 'sk_test_6NPXd4pr3LY5Vf4jJYieMxiI00EZ0XHr4u'

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    'static',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = '/var/www/colexin_store/media'

