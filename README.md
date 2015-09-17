# django-test

## Prerequisites

Install pyenv:
https://github.com/yyuu/pyenv , https://github.com/yyuu/pyenv-installer

Then:

    pyenv virtualenv 3.4.3 djtest
    pyenv activate djtest
    pip install django==1.8
    pip install celery
    pip install django-celery

## Preparations
    
    python manage.py migrate
    python manage.py makemigrations leaderboard
    python manage.py migrate leaderboard
    python manage.py syncdb
    
## Running the server and the celery worker

Run the server:

    python manage.py runserver

Run celery:
    celery -A leaderboard worker -l info
or:
    python manage.py celery worker -B


