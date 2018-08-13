FROM python:3.6

RUN python -m pip install -U pip

WORKDIR /usr/src/chat

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn gevent
COPY api api
COPY manage.py manage.py

EXPOSE 8000
ENV DJANGO_SETTINGS_MODULE api.settings.production
ENV PYTHONUNBUFFERED 1

RUN python manage.py migrate
CMD ["gunicorn", "api.wsgi:application", "-b 0.0.0.0:8000", "-k gevent"]
