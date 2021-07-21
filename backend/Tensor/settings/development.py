from .base import *

DEBUG = True


INTERNAL_IPS = [
    '127.0.0.1',
]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
   }
}

# Paypal
PAYPAL_RECEIVER_EMAIL = "sb-fpbe36699535@business.example.com"
PAYPAL_TEST = True
ABSOLUTE_URL = 'tensor.fr'