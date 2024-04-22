from .base import *
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^mm-24*i-6iecm7c@z9l+7%^ns^4g^z!8=dgffg4ulggr-4=1%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[contactor] %(levelname)s %(asctime)s %(message)s'
        },
    },
    'handlers': {
        # Send all messages to console
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        # This is the "catch all" logger
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}

DEV_VERSION = False

INSTALLED_APPS += ['corsheaders', 'apis_bibsonomy', 'apis_highlighter']
DATABASES = {}

#DATABASES["default"] = dj_database_url.parse(os.environ['DATABASE_LOCAL'], conn_max_age=600)
DATABASES["default"] = dj_database_url.config(conn_max_age=600)


CSRF_TRUSTED_ORIGINS = ['sola.acdh-dev.oeaw.ac.at']

APIS_RELATIONS_FILTER_EXCLUDE += ['annotation', 'annotation_set_relation']

REDMINE_ID = "13104"

PROJECT_NAME="coladay"

ALLOWED_HOSTS = ['.sola.sisyphos.arz.oeaw.ac.at', '.sola.acdh-dev.oeaw.ac.at', '.coladay-backend-main.acdh-dev.oeaw.ac.at']

EMAIL_HOST = 'smtp.oeaw.ac.at'

SERVER_EMAIL = 'acdh-tech@oeaw.ac.at'

ADMINS = [('Matthias Schlögl', 'matthias.schloegl@oeaw.ac.at')]

APIS_BIBSONOMY = [{
    'type': 'bibsonomy',
    'url': 'https://www.bibsonomy.org/',
    'user': os.environ.get('APIS_BIBSONOMY_USER'),
    'API key': os.environ.get('APIS_BIBSONOMY_PASSWORD'),
    'group': 'coladay'
},]

APIS_COMPONENTS = ['apis_highlighter']

APIS_HIGHLIGHTER_MODELS = [
    (97, 'Sunday Representations'),
    (41, 'Passage Publication')

]

APIS_SKOSMOS = {
    'url': os.environ.get('APIS_SKOSMOS', 'https://vocabs.acdh-dev.oeaw.ac.at'),
    'vocabs-name': os.environ.get('APIS_SKOSMOS_THESAURUS', 'coladayhesaurus'),
    'description': 'Thesaurus of the Coladay project. Used to type entities and relations.'
}

APIS_BASE_URI = "https://sola.acdh-dev.oeaw.ac.at"


import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://5708cb45635e4bd88a02a7eaaa39f337@sentry.io/1885780",
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)


