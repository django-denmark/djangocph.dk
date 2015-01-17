import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangocph_dk.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)
