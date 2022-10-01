from .base import *

DEBUG = False

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASE_ROUTERS = ['Tensor.dbrouters.router']

ALLOWED_HOSTS = ['tensor.fr', 'www.tensor.fr']

USE_X_FORWARDED_HOST = True

DATABASES = {
    'default': {
        'NAME': 'tensor',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'tensor',
        'PASSWORD': os.getenv("DB_TENSOR_PASS"),
        'HOST': '172.17.0.1',
        'PORT': '3306',
    },
    'rank_awp': {
        'NAME': 'rank_awp',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'awp',
        'PASSWORD': os.getenv("DB_AWP_PASS"),
        'HOST': '172.17.0.1',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4',
                    'auth_plugin': 'mysql_native_password'
                    }
    },
    'surftimer': {
        'NAME': 'surftimer',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'surf',
        'PASSWORD': os.getenv("DB_SURF_PASS"),
        'HOST': '172.17.0.1',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4',
                    'auth_plugin': 'mysql_native_password'
                    }
    },
    'sourcebans': {
        'NAME': 'sourcebans',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'sourcebans',
        'PASSWORD': os.getenv("DB_SOURCEBANS_PASS"),
        'HOST': '172.17.0.1',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4',
                    'auth_plugin': 'mysql_native_password'
                    }
    },
    'rank_retake': {
        'NAME': 'rank_retakes',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'retakes',
        'PASSWORD': os.getenv("DB_RETAKES_PASS"),
        'HOST': '172.17.0.1',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4',
                    'auth_plugin': 'mysql_native_password'
                    }
    },
    'tvip': {
        'NAME': 'VIP',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'awp',
        'PASSWORD': os.getenv("DB_AWP_PASS"),
        'HOST': '172.17.0.1',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4',
                    'auth_plugin': 'mysql_native_password'
                    }
    },
}

# Paypal
PAYPAL_RECEIVER_EMAIL = os.getenv("PAYPAL_EMAIL")
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
