from .base import *
import os

# SECURITY WARNING: keep the secret key used in production secret!
DEFAULT_SECRET_KEY = "a+nkut46lzzg_=ul)zrs29$u_6^*)2by2mjmwn)tqlgw)_at&l"
SECRET_KEY = os.environ.get("SECRET_KEY", DEFAULT_SECRET_KEY)
if os.environ.get("SENTRY_DSN"):
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn=os.environ.get("SENTRY_DSN"),
        integrations=[
            DjangoIntegration(),
        ],
        environment="production",
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0,
        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True,
    )
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

DATABASES = {
   'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': os.environ.get('APIS_DB_NAME'),
         'USER': os.environ.get('APIS_DB_USER'),
         'PASSWORD': os.environ.get('APIS_DB_PASSWORD'),
         'HOST': os.environ.get('APIS_DB_HOST', '127.0.0.1'),
         'PORT': os.environ.get('APIS_DB_PORT', '3306'),
     }
 }


CSRF_TRUSTED_ORIGINS = ['sola.acdh-dev.oeaw.ac.at']

APIS_RELATIONS_FILTER_EXCLUDE += ['annotation', 'annotation_set_relation']

REDMINE_ID = "13104"

PROJECT_NAME="coladay"

ALLOWED_HOSTS = ['.sola.sisyphos.arz.oeaw.ac.at', '.sola.acdh-dev.oeaw.ac.at']

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


