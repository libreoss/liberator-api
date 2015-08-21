Dockerfile and docker-compose.yml are based on the information found at https://docs.docker.com/compose/django/


To create and run the Docker instance, simply execute:

    docker-compose up


While everything is running, execute the following to create the required database structures:

    docker-compose run web python manage.py syncdb


Create a user:

    docker-compose run web python manage.py createsuperuser


You can now log in at http://localhost:8000


That's it, happy hacking!
