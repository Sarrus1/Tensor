FROM python:3.10.0-slim-buster

RUN apt-get update && apt-get -y install default-libmysqlclient-dev gcc cron && touch /var/log/cron.log
RUN python -m pip install -U  pip
COPY ./backend/requirements.txt requirements.txt
RUN pip install -r requirements.txt

# create the server user
RUN adduser server

# create the appropriate directories
ENV HOME=/home/server
ENV SERVER_HOME=/home/server/tensor
RUN export PATH=/home/server/.local/bin:$PATH
WORKDIR $HOME

ENV DJANGO_SETTINGS_MODULE=Tensor.settings.production

# copy project
WORKDIR $SERVER_HOME
RUN rm -rf ./*
COPY ./backend .
RUN chown -R server:server $SERVER_HOME
USER server
RUN python3 manage.py collectstatic --noinput
RUN python3 manage.py migrate