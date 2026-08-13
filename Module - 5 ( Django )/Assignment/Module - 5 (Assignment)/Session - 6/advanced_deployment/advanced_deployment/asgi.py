import os
from django.core.asgi import get_asgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "session6_advanced_deployment.settings")
application = get_asgi_application()
