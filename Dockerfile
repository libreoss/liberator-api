FROM python:3.4
ENV PYTHONUNBUFFERED 1
# ssh-keygen is needed because some packages from requirements.txt are not available on pypy and are git cloned instead
RUN ssh-keygen -q -t rsa -N '' -f id_rsa
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
