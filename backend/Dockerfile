FROM python:3.10.4-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app/backend

RUN apt-get update && apt-get install -y \
    build-essential libssl-dev xvfb curl wget \
    libffi-dev libpq-dev python-dev gcc unzip nano \
    daemonize dbus-user-session fontconfig gettext \
    binutils libproj-dev git gdal-bin python3-gdal libgdal-dev

COPY requirements.txt requirements.txt

RUN pip install -U pip && pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT [ "sh", "entrypoint.sh" ]