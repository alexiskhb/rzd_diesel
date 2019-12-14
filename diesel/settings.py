import logging
import os

DEBUG = True
BASE_DIR = os.path.dirname(__file__)

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbloko',
        'USER': 'readslave',
        'PASSWORD': 'rzd_2020',
        'HOST': 'lokosampledb.cozlbgcgmptq.us-east-2.rds.amazonaws.com',
        'PORT': '3306',
    }
}


INSTALLED_APPS = [
    "diesel",
    "django.contrib.auth",
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "django.contrib.messages",
]

SECRET_KEY = 'supersikrettf1oybj9alm100im6whyg$_fz2e4xjqt=i-s4dg'
LOGIN_REDIRECT_URL = "/"


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")


ROOT_URLCONF = "diesel.urls"
LANGUAGES = (("en", "English"), ("ru", "Russian"))

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            STATIC_ROOT,
            os.path.join(STATIC_ROOT, 'templates'),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

STRIPE_SECRET_KEY = "none"
STRIPE_PUBLISHABLE_KEY = "none"

if os.environ.get("LOG"):
    logger = logging.getLogger("user_payments")
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)

WSGI_APPLICATION = 'diesel.wsgi.application'
