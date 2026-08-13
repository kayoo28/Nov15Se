import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "session5_third_party_api.settings")
application = get_wsgi_application()
