# django-rest-demo

A short demonstration of a REST-Api with Django and Django-Rest-Framework.

## Models

### User

- firstname
- lastname
- birthday
- address

### Address

- street
- number
- postcode
- city


## Setup

    $ cd rest-api
    $ pip install -r requirements.txt
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py runserver

The app should now be running on http://127.0.0.1:8000/.