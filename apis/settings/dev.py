from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^mm-24*i-6iecm7c@z9l+7%^ns^4g^z!8=dgffg4ulggr-4=1%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += ['corsheaders', 'apis_bibsonomy', 'apis_highlighter']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}

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
