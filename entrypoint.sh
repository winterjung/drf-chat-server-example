#!/bin/bash
python manage.py migrate
nohup python manage.py process_tasks > /dev/null &
gunicorn api.wsgi:application -b 0.0.0.0:8000 -k gevent
