#!/bin/sh

python manage.py migrate --noinput
python manage.py collectstatic 
uwsgi --chdir=/code -s 0.0.0.0:$1 --module=project.wsgi:application

