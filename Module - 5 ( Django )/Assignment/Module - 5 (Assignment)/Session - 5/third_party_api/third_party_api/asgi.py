import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "session5_third_party_api.settings")
application = get_asgi_application()
