"""
Django settings for hcd project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2n-u9ed__0r2awe)^zhj#z9dyfvbe+iw2%7^b(acl0g*&s%sk#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

LOGIN_REDIRECT_URL = 'chores:index'
LOGOUT_REDIRECT_URL = 'user_management:login'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
AUTHENTICATION_BACKENDS = [
    # ...
    'axes.backends.AxesStandaloneBackend',
    'django.contrib.auth.backends.ModelBackend',
    # ...
]

# settings.py

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


# Email Backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# SMTP Configuration for Gmail
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587  # Port number for TLS
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False  # Set to False for TLS
EMAIL_HOST_USER = 'securecoding9@gmail.com'  # Your Gmail email address
EMAIL_HOST_PASSWORD = 'xxzs lkwp euox wsxk'  # Your Gmail password or an application-specific password

# Default From Email
DEFAULT_FROM_EMAIL = 'securecoding9@gmail.com'

# Email Subject Prefix
EMAIL_SUBJECT_PREFIX = '[HCD]'

# Email Timezone
EMAIL_TIME_ZONE = 'UTC'  # Change to your desired timezone

# Email Connection Timeout
EMAIL_TIMEOUT = 5  # Timeout in seconds (adjust as necessary)



# Application definition

INSTALLED_APPS = [
    'chores',  # The name should match your app name.
    'user_management',  # The name should match your app name.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'axes',

]
# settings.py

# Axes configuration
AXES_LOGIN_FAILURE_LIMIT = 10 # Number of allowed login attempts before lockout
AXES_COOLOFF_TIME = 1
AXES_LOCKOUT_TEMPLATE = 'user_management/login_lockout.html'  # Create this template


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware',
]


ROOT_URLCONF = 'hcd.urls'
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_AGE = 1800
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SESSION_SAVE_EVERY_REQUEST = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'hcd.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
