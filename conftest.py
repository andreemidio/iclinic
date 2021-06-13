from django.conf import settings
from drf_extra_fields.runtests.settings import MIDDLEWARE_CLASSES
from prettyconf import Configuration

from config.settings import INSTALLED_APPS

config = Configuration()


def pytest_configure(config):
    from django.conf import settings

    settings.configure(
        DEBUG=True,
        DATABASE_ENGINE="sqlite3",
        DATABASES={
            "default": {
                "NAME": ":memory:",
                "ENGINE": "django.db.backends.sqlite3",
                "TEST_NAME": ":memory:",
            },
        },
        DATABASE_NAME=":memory:",
        TEST_DATABASE_NAME=":memory:",
        INSTALLED_APPS=INSTALLED_APPS,
        MIDDLEWARE_CLASSES=MIDDLEWARE_CLASSES,

    )