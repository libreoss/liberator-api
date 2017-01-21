FROM python:3.4
ENV PYTHONUNBUFFERED 1
# ssh-keygen is needed because some packages from requirements.txt are not available on pypy and are git cloned instead
RUN ssh-keygen -q -t rsa -N '' -f id_rsa
RUN apt-get update && apt-get install netcat enchant hunspell hunspell-sh -y
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
ADD requirements-dev.txt /code/
RUN pip install -r requirements.txt && pip install -r requirements-dev.txt && pip install uwsgi 
ADD . /code/
RUN groupadd -r liberator && useradd -r -g liberator liberator
RUN mkdir -m 777 -p /var/db/liberator/dictionaries/
USER liberator
