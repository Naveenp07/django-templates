"""
WSGI config for repo_name project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Replace {{project_name}} with your actual project folder name
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings.production")

application = get_wsgi_application()
