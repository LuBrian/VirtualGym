"""
Django settings for VirtualGym project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


ADMINS = (
    # ('Your Name', 'your_email@example.com'),
    ('cujo2k', 'thectaeh@gmail.com'),
)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vibj5$x&!ogu@1ksm*=w0819u4f-&732=ua6wh!88zver)5dmv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'comments',
    'users',
    'exercise',
    'VirtualGym',
    'forum',
    'social.apps.django_app.default',
    'social_django',
]

###################### AUTH ##########################

AUTH_USER_MODEL = 'users.MyUsers'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    )


#######################################################

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware', 
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'VirtualGym.urls'

TEMPLATES = [
    {
        # BASE_DIR,
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [os.path.join(BASE_DIR,"templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',


                'social_django.context_processors.backends',  # <--
                'social_django.context_processors.login_redirect', # <--
            ],
        },
    },
]

SOCIAL_AUTH_URL_NAMESPACE = 'social'


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1082380445663-a6pee1tpgug2o78can7d3n1j32129499.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'ad6TPM9N7jlkpplDYEXkXiNH'

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_KEY = '181251585758026'
SOCIAL_AUTH_FACEBOOK_SECRET = '78e7874e5f884ba062885611d9edaa45'

SOCIAL_AUTH_TWITTER_KEY = 'jGXhvPd1hcE5NRhuAxsu5tBEP'
SOCIAL_AUTH_TWITTER_SECRET = '0Jp7bQMBRvgNxP8MHlwTafL03LqxFIuHb7AyF22AJ0knlNNcbd'

SOCIAL_AUTH_USER_MODEL = 'users.MyUsers'




LOGIN_REDIRECT_URL = '/index/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/index/'
# SOCIAL_AUTH_LOGIN_URL = '/signIn/'
# LOGIN_URL = 'signIn'
# LOGOUT_URL = '/index/'
# LOGIN_REDIRECT_URL = '/index/'


SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'social_core.pipeline.social_auth.associate_by_email',
)



STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    # '/var/www/static/',
]

WSGI_APPLICATION = 'VirtualGym.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'virtualgym',
#         'USER': 'user',
#         'PASSWORD': 'password',
#         'HOST': 'localhost',
#     }
# }



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'vg.db'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL="/media/"
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media_cdn')
