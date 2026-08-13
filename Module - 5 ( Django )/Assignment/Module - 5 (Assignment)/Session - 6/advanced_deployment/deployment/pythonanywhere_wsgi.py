import os
import sys

PROJECT_PATH = "/home/YOUR_USERNAME/session6_advanced_deployment"
if PROJECT_PATH not in sys.path:
    sys.path.insert(0, PROJECT_PATH)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "session6_advanced_deployment.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
