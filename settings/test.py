from .dev import *  # noqa

DEFAULT_FILE_STORAGE = 'inmemorystorage.InMemoryStorage'

# Speeds up tests.
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]
