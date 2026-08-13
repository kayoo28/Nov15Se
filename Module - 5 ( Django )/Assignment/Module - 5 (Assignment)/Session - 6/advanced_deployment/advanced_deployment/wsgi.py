import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "session6_advanced_deployment.settings")
application = get_wsgi_application()
