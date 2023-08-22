# Django Base Setup



## Getting started

Start faster development with this preset of django project.

## Load default data into database
python manage.py loaddata fixtures/settings.json
python manage.py loaddata fixtures/languages.json 
python manage.py loaddata fixtures/permissions.json
python manage.py loaddata fixtures/email_templates.json

## Dump default data from database
python manage.py dumpdata > fixtures/db_dump_v1.0.json
python manage.py dumpdata permissions > fixtures/menu_v1.0.json
python manage.py dumpdata settings > fixtures/settings_v1.0.json
python manage.py dumpdata languages > fixtures/languages_v1.0.json
python manage.py dumpdata email_templates > fixtures/email_templates_v1.0.json
python manage.py dumpdata users > fixtures/users_v1.0.json

## Runserver
python manage.py runserver 0.0.0.0:8000