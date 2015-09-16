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

    python manage.py runserver
    celery -A bubitest worker -l info

