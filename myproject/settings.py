"""
Django settings for myproject project.
WORKING VERSION – Nov 05, 2025
"""

from pathlib import Path
from datetime import timedelta

# ──────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-en4(01tt+s#r)_9nk68vj6_#rs2f(h8#^_u0488+ped%2arow_'
DEBUG = False
ALLOWED_HOSTS = []

# ──────────────────────────────────────────────────────────────
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',           # ← ONLY ONE TIME
    'rest_framework_simplejwt',
    'corsheaders',
    'habits',
    'myapp',
]

# ──────────────────────────────────────────────────────────────
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),   # ← 30 days now!
    'REFRESH_TOKEN_LIFETIME': timedelta(days=90),
}

# ──────────────────────────────────────────────────────────────
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Allow your phone/expo to talk to Django
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8081",
    "http://localhost:19006",
    "http://10.0.2.2:8000",      # Android emulator
    "http://127.0.0.1:8000",
]

# Or simpler (only for development!)
CORS_ALLOW_ALL_ORIGINS = True   # ← remove this when you deploy later

ALLOWED_HOSTS = ['10.209.102.130', 'localhost', '127.0.0.1', '0.0.0.0']

ROOT_URLCONF = 'myproject.urls'

# ──────────────────────────────────────────────────────────────
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],   # ← FIXED: NOW A REAL LIST
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

WSGI_APPLICATION = 'myproject.wsgi.application'

# ──────────────────────────────────────────────────────────────
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ──────────────────────────────────────────────────────────────
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']   # ← CSS/JS folder
STATIC_ROOT = BASE_DIR / 'staticfiles'     # for collectstatic later
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'