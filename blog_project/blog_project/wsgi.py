"""
WSGI config for blog_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')
profile = os.environ.get('PROJECT_PROFILE','product')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings.%s'%profile)

application = get_wsgi_application()
