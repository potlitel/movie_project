"""
Django settings for movie_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c9t0=q=j!aop6mn=+kq@a+5m^z3t%h5x4st*!qb)ac@l5m$%v7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.utils',
    'crispy_forms',
	#'MovieLib',
    #'Todo',
    'FileSample',
    #'parsley',
    #'myauth',
    'django_bootstrap_breadcrumbs',
    #'any_imagefield',
    'datetimewidget',
    'pagination',
    #'smart_selects',
    #'sortedm2m',
    'better_filter_widget',
    #'django_js_reverse',
    'wkhtmltopdf',
    #'django_summernote',
    'django_password_strength',
    'related_choice_field',
    'avatar',
    #'extra_views'
    # 'registration',
    )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'movie_project.urls'

WSGI_APPLICATION = 'movie_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqliteMovieLib'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True

WKHTMLTOPDF_CMD = 'C:/Archivos de programa/wkhtmltopdf/bin/wkhtmltopdf.exe'  

WKHTMLTOPDF_CMD_OPTIONS = {
        'quiet': True,
    }

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

"""
STATICFILES_FINDERS = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "static")
)
"""

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticFilesLocation')
#STATIC_URL = os.path.join(BASE_DIR, '/static/')
STATICFILES_DIRS = (
            os.path.join(BASE_DIR, "static"), 
    )


MEDIA_ROOT = os.path.join(BASE_DIR, "userfiles")
MEDIA_URL = 'userfiles/'

AVATAR_STORAGE_DIR = 'userfiles/avatars'

PHANTOMJS_BIN = ( 
            os.path.join(BASE_DIR, "static/Phantomjs/bin/phantomjs"), 
    )

# MEDIA_ROOT = "/media/"
# MEDIA_URL = 'http://localhost/media/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

# AUTH_USER_MODEL = 'myauth.User'

TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
                               "django.core.context_processors.debug",
                               "django.core.context_processors.i18n",
                               "django.core.context_processors.media",
                               "django.core.context_processors.request",
                               "django.contrib.messages.context_processors.messages")

USE_L10N = True
USE_TZ = True
USE_I18N = True

USE_DJANGO_JQUERY = True

# URL of the login page.
LOGIN_URL = 'loguin'
LOGOUT_URL = 'logout'
# The URL where requests are redirected after login when the contrib.auth.login
# view gets no next parameter.
LOGIN_REDIRECT_URL = 'inicio'

AUTH_PROFILE_MODULE = 'FileSample.Profile'

FILE_CHARSET = "utf-8"