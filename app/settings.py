"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path
import paypalrestsdk
import razorpay

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6)luf6o*#hhonf%y4nf_^-lp_g_$@pxe#e)vw7c@^*kk@fp80#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ecom',
    'ckeditor',
    'ckeditor_uploader',
    'colorfield',
    # 'cart',
    'django_simple_coupons',
    'colorful',
    'paypalrestsdk',
    'mathfilters',
     'paypal.standard.ipn',
    
]
# set paypal test mode
PAYPAL_TEST = True
DSC_COUPON_CODE_LENGTH = 16
# CART_SESSION_ID = 'cart'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'ecom.middleware.simplemiddleware'
    
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'cart.context_processor.cart_total_amount',
                'django.template.context_processors.request',
               "app.context_processors.categories_processor", 
                
            ],
        },
    },
]


WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
STATIC_ROOT = '/static/'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

from ckeditor.configs import DEFAULT_CONFIG

CKEDITOR_UPLOAD_PATH = "Media/uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_THUMBNAIL_SIZE = (300, 300)
CKEDITOR_IMAGE_QUALITY = 40
CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_ALLOW_NONIMAGE_FILES = True
CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False
CKEDITOR_JQUERY_URL = 'http://libs.baidu.com/jquery/2.0.3/jquery.min.js'


CUSTOM_TOOLBAR = [
    {
        "name": "document",
        "items": [
            "Styles", "Format", "Bold", "Italic", "Underline", "Strike", "-",
            "TextColor", "BGColor",  "-",
            "JustifyLeft", "JustifyCenter", "JustifyRight", "JustifyBlock",
        ],
    },
    {
        "name": "widgets",
        "items": [
            "Undo", "Redo", "-",
            "NumberedList", "BulletedList", "-",
            "Outdent", "Indent", "-",
            "Link", "Unlink", "-",
            "Image", "CodeSnippet", "Table", "HorizontalRule", "Smiley", "SpecialChar", "-",
            "Blockquote", "-",
            "ShowBlocks", "Maximize",
        ],
    },
]

LOGIN_REDIRECT_URL = 'Home'
LOGOUT_REDIRECT_URL = 'Home'


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'priyabrata.a@digitally.global'
EMAIL_HOST_PASSWORD = 'Digitally@98300$$!'



paypalrestsdk.configure({
  "mode": "sandbox", # Set to "live" for production
  "client_id": "ARK3NclAwBH55-YHC-BrwIyUJVok-cAv5p_oGmEZd5woWVE6-k5TUReO9-dPAFk0xNa061A_rEucz4iX",
  "client_secret": "EAuRZPCKwON6DhzwfUrM1lBJLRPAHgoDZzkFOZFamR_DiW29gcfNRKov5i7C_jkfnzGfjhn5JaZk7MTB",
})

PAYPAL_RECEIVER_EMAIL="bizdevesh@gmail.com"
SITE_URL = "https://b5c8-49-37-33-255.ngrok-free.app/"

client = razorpay.Client(auth=("rzp_test_Zst0lERAYg5HKw","yT4pY8zanoSIFeAqdHkdNcvI"))
client.set_app_details({"title" : "Gifshion", "version" : "0.0.1"})