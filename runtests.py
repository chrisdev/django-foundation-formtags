#!/usr/bin/env python

import os
import sys
import django

from django.conf import settings


if not settings.configured:
    settings_dict = dict(
        INSTALLED_APPS=(
            'foundation_formtags',
            'foundation_formtags.tests',
        ),
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": ":memory:",
                "USER": "",
                "PASSWORD": "",
                "HOST": "",
                "PORT": "",
            }
        },
        MIDDLEWARE_CLASSES = (),
        TEMPLATES = [{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.contrib.auth.context_processors.auth',
                    'django.template.context_processors.debug',
                    'django.template.context_processors.i18n',
                    'django.template.context_processors.media',
                    'django.template.context_processors.static',
                    'django.template.context_processors.tz',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
        ]
    )

    settings.configure(**settings_dict)
    if django.VERSION >= (1, 7):
        django.setup()


def runtests(*test_args):
    if not test_args:
        test_args = ['foundation_formtags']

    parent = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, parent)

    if django.VERSION < (1, 8):
        from django.test.simple import DjangoTestSuiteRunner
        failures = DjangoTestSuiteRunner(
            verbosity=1, interactive=True, failfast=False).run_tests(['tests'])
        sys.exit(failures)

    else:
        from django.test.runner import DiscoverRunner
        failures = DiscoverRunner(
            verbosity=1, interactive=True, failfast=False).run_tests(test_args)
        sys.exit(failures)


if __name__ == '__main__':
    runtests()
