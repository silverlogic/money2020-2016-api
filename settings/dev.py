from .base import *  # noqa

DEBUG = True
SECRET_KEY = '1234'

# Email
DEFAULT_FROM_EMAIL = 'tsl@example.com'
DJMAIL_REAL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Debug Toolbar
INSTALLED_APPS += ['debug_toolbar']
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'apps.base.debug_toolbar.show_toolbar'
}
