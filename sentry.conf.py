import dj_database_url

import os

CONF_ROOT = os.path.dirname(__file__)

DATABASES = {
    'default': dj_database_url.config(default="postgres://localhost"),
}

SENTRY_KEY = 'CHANGEME'

# Set this to false to require authentication
SENTRY_PUBLIC = False

SENTRY_URL_PREFIX = 'http://CHANGEME'

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = os.environ.get('PORT', 80)
SENTRY_WEB_OPTIONS = {
    'workers': 3,  # the number of gunicorn workers
    # 'worker_class': 'gevent',
}

# Mail server configuration

# For more information check Django's documentation:
#  https://docs.djangoproject.com/en/1.3/topics/email/?from=olddocs#e-mail-backends

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = ''
EMAIL_PORT = 25
EMAIL_USE_TLS = False
