from .base import *

DEBUG = False

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASE_ROUTERS = ['Tensor.dbrouters.router']

ALLOWED_HOSTS = ['tensor.fr', 'www.tensor.fr']

USE_X_FORWARDED_HOST = True

DATABASES = {
    'default': {
        'NAME': 'Tensor',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'tensor',
        'PASSWORD': password_DB_tensor,
        'HOST': '172.17.0.1',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4',
                    'auth_plugin': 'mysql_native_password'
                    }
    },
    'rank_awp': {
        'NAME': 'rank_awp',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'csgoawp',
        'PASSWORD': password_DB_awp,
        'HOST': '172.17.0.1',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4',
                    'auth_plugin': 'mysql_native_password'
                    }
    },
    'surftimer': {
        'NAME': 'surftimer',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'csgosurf',
        'PASSWORD': password_DB_awp,
        'HOST': '192.168.1.105',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4',
                    'auth_plugin': 'mysql_native_password'
                    }
    },
    'sourcebans': {
        'NAME': 'sourceban',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'sourceban',
        'PASSWORD': password_DB_sb,
        'HOST': '172.17.0.1',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4',
                    'auth_plugin': 'mysql_native_password'
                    }
    },
    'rank_retake': {
        'NAME': 'retake_rank',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'retake',
        'PASSWORD': password_DB_retakes,
        'HOST': '172.17.0.1',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4',
                    'auth_plugin': 'mysql_native_password'
                    }
    },
    'tvip': {
        'NAME': 'VIP',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'csgoawp',
        'PASSWORD': password_DB_awp,
        'HOST': '172.17.0.1',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4',
                    'auth_plugin': 'mysql_native_password'
                    }
    },
}

# Paypal
PAYPAL_RECEIVER_EMAIL = paypalEmail
PAYPAL_TEST = False
ABSOLUTE_URL = 'tensor.fr'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '[DJANGO] %(levelname)s %(asctime)s %(module)s '
            '%(name)s.%(funcName)s:%(lineno)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    'loggers': {
        '*': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}
