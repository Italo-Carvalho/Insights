import os
import sys
import pytest
from django.conf import settings

@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "insights",
        "USER": "rpdb",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": 5432,
    }

sys.path.append(os.path.dirname(__file__))
