"""
WSGI config for System project.

It exposes the WSGI callable as emergency_management module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "System.settings")

application = get_wsgi_application()
