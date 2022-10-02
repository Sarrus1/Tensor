FROM python:3.10.0-slim-buster

RUN apt-get update && apt-get -y install default-libmysqlclient-dev gcc cron && touch /var/log/cron.log
RUN python -m pip install -U  pip
COPY ./backend/requirements.txt requirements.txt
RUN pip install -r requirements.txt

# create the server user
RUN adduser server

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

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
RUN mkdir $SERVER_HOME/staticfiles
RUN mkdir $SERVER_HOME/mediafiles
RUN chown -R server:server $SERVER_HOME
USER server

CMD ["/bin/bash", "start_server.sh"]