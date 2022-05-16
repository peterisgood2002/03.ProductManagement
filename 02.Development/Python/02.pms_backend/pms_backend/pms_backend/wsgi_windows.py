"""
WSGI config for pms_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
from pathlib import Path

sys.path.append("C:/Apache24/app/02.pms_backend/pms_backend/")
#sys.path.append("C:/Apache24/app/02.pms_backend/pms_backend/pms_backend/pms_be/")

path_home = str(Path(__file__).parents[1])
print("PATH = " + path_home)
print( sys.path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'pms_backend.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pms_backend.settings')

application = get_wsgi_application()
