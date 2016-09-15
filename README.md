# DjangoCPH.dk

## How to start developing

- setup a virtualenv with python 3 via virtualenv or virtualenvwrapper `mkvirtualenv -p python3 meetup`
- pip install -r requirements.txt
- cp djangocph_dk/env_sample djangocph_dk/.env
- run the migrations `python manage.py migrate`
- create a superuser `python manage.py createsuperuser`
