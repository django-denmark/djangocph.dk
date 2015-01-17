import os
from whitenoise.django import DjangoWhiteNoise
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangocph_dk.settings")
application = DjangoWhiteNoise(application)
