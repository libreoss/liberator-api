#!/bin/bash

while ! echo exit | nc db 5432
do
  sleep 1;
done

python3 manage.py syncdb --noinput
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
