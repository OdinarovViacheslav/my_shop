import os


def reduce_path(file_name, times):
    result = os.path.realpath(file_name)
    for i in range(times):
        result = os.path.dirname(result)
    return result


ROOT_DIR = reduce_path(__file__, 4)
APPS_DIR = reduce_path(__file__, 3)

DJANGO_ENV = os.getenv('DJANGO_ENV', "DEVELOPMENT")
DEBUG = DJANGO_ENV != "PRODUCTION"
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
# ALLOWED_HOSTS = os.environ["DJANGO_ALLOWED_HOSTS"].split(',')
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
ROOT_URLCONF = "config.urls"

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(ROOT_DIR, "static/")
STATICFILES_DIRS = [os.path.join(APPS_DIR, "static/")]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(ROOT_DIR, "media/")
# SECRET_KEY = "django-insecure-jes8j473jqi0t@n)dtgx)eiry$$bbw^4hm@v0)kpdfw32jirun"


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "drf_spectacular",
    "customer",
    "pages"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
