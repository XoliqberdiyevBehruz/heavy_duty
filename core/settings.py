from pathlib import Path
import environ
# Build paths inside the project like this: BASE_DIR / 'subdir'.
env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent
env.read_env(BASE_DIR / '.env')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.str('DEBUG')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'drf_yasg',
    'rest_framework',
    'corsheaders',

    'apps.accounts',
    'apps.shared',
    'apps.common',
    'apps.products',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('POSTGRES_DB'),
        'USER': env.str('POSTGRES_USER'),
        'PASSWORD': env.str("POSTGRES_PASSWORD"),
        'HOST': env.str('POSTGRES_HOST'),
        'PORT': env.str("POSTGRES_PORT"),
        'CONN_MAX_AGE': 0
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'uz'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'resources/static/'
STATIC_ROOT = BASE_DIR / 'resources/static'

MEDIA_URL = 'resourcer/media/'
MEDIA_ROOT = BASE_DIR / 'resources/media'


# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'accounts.User'

LANGUAGES = (
    ('uz', 'Uzbek'),
    ('ru', 'Russian'),
    ('en', 'English')
)
MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'

CACHES = {
    "default": {
        "BACKEND": 'django_redis.cache.RedisCache',
        "LOCATION": 'redis://127.0.0.1:6379/1',
        "TIMEOUT": 5,
    },
}

CACHE_MIDDLEWARE_SECONDS = 5


CACHEOPS_REDIS = 'redis://127.0.0.1:6379/1'
CACHEOPS_DEFAULTS = {
    "timeout": 5,
}
CACHEOPS = {
    "common.*": {
        "ops": "all",
        "timeout": 60 * 5, 
    },
}
CACHEOPS_DEGRADE_ON_FAILURE = True
CACHEOPS_ENABLED = env.bool("CACHE_ENABLED", False)


CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://heavyduty.uz",
    "https://heavydutyuz.ru",
]
CORS_ALLOW_ALL_ORIGINS = True

JAZZMIN_SETTINGS = {
    "site_title": "Admin Panel",
    "site_header": "Heavy Duty Admin",
    "site_brand": "Heavy Duty",
    # "site_logo": "image.png",  # static papkada joylashgan logoni yo‘li
    "welcome_sign": "Welcome to Heavy Duty Admin",
    "copyright": "Heavy Duty Inc",
    "search_model": ["products.Product", "products.ProductCategory"],

    "topmenu_links": [
        {"name": "Bosh sahifa", "url": "admin:index"},
    ],

    "icons": {
        "products": "fas fa-box",
        "products.Product": "fas fa-cube",
        "products.ProductCategory": "fas fa-tags",
        "products.UsageArea": "fas fa-compass",

        "common.AboutUs": "fa-solid fa-address-card",
        "common.Settings": "fas fa-cogs",
        "common.Sertificate": 'fas fa-certificate',
        "common.Statistics": 'fa-solid fa-chart-line',
        'common.Banner': 'fas fa-image',
        'common.ContactUs': 'fas fa-phone',
        "common.CompanyContactInfo": 'fas fa-building',
        "common.ProductInfo": "fas fa-file-alt",
    },

    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["products", "common"],

    "show_sidebar": True,
    "navigation_expanded": True,

    "language_chooser": False,
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
