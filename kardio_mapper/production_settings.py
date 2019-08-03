from kardio_mapper.settings import *
import dj_database_url

# CUSTOM
DATABASE_URL = os.environ.get("DATABASE_URL")

DATABASES = {
    'default': dj_database_url.config(
        default=DATABASE_URL
    )
}

SECURE_SSL_REDIRECT = True
