
import os
import sys
from datetime import timedelta

DEBUG = True
TEMPLATE_DEBUG = DEBUG

gettext = lambda s: s
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

sys.path.insert(0, os.path.join(PROJECT_DIR, 'apps'))
sys.path.insert(0, os.path.join(PROJECT_DIR, 'cmsplugins'))

ADMINS = (
    ('Sascha Haeusler', 'sascha.haeusler@netzbarkeit.ch'),
)

CMS_REDIRECTS = True

MANAGERS = ADMINS

DEFAULT_CHARSET = 'utf-8'

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'Europe/Zurich'

# Language code for this installation. All choices can be found here:
#
LANGUAGE_CODE = 'de'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# media deliver
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
MEDIA_URL = '/media/'

# static files (application js/img etc)
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'site-static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '&P_%dp3qv&%%&88881jHBBlq_cnf6i*laow21))==)333242,KSKOKLMSj88?#nf@'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # default
)

ANONYMOUS_USER_ID = -1
CMS_PERMISSION = False

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # cms
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    # cms
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
    #'nbk_cms.context_processors.extended_page_options',
)

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
)

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'templates'),
)


INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.humanize',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.comments',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',

    'django_extensions',
    'gunicorn',
    'south',

    # cms
    'cms',
    'mptt',
    'menus',
    'sekizai',
    'tinymce',
    #'psycopg2',

    'cms.plugins.text',
    'cms.plugins.picture',

    'djangular',

    # mine
    'clothing',
]

# LANGUAGES
LANGUAGES = (
    ('de', 'German'),
)


# CMS RELATED STUFF
CMS_TEMPLATES = (
   ('cms/layouts/home.html', gettext('Home Template')),
)

CMS_FRONTEND_LANGUAGES = ('de', )

CMS_LANGUAGES = {
        1: [
            {
                'code': 'de',
                'name': gettext('Deutsch'),
                'public': True,
                'hide_untranslated': True,
                'redirect_on_fallback':False,
            },
        ],
        'default': {
            'fallbacks': ['de'],
            'redirect_on_fallback':True,
            'public': False,
            'hide_untranslated': False,
        }
    }


DJANGO_WYSIWYG_FLAVOR = "tinymce_advanced"    # or "tinymce_advanced"

TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
    #'cleanup_on_startup': True,
    #'custom_undo_redo_levels': 10,
    'style_formats' : [
        {'title' : 'Bold text', 'inline' : 'span', 'classes' : 'blue bold'},
        {'title' : 'Title text', 'inline' : 'span', 'classes' : 'blue bold achievement_title'},
    ],
}
TINYMCE_SPELLCHECKER = False

DEFAULT_FROM_EMAIL = 'sascha.haeusler@netzbarkeit.ch'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


try:
    from local_settings import *
except ImportError:
    pass