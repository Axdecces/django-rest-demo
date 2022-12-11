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

The app should now be running on http://127.0.0.1:8000/api/.

The two usable endpoints are http://127.0.0.1:8000/api/users/ and http://127.0.0.1:8000/api/addresses/.

When creating a user a nested address can be created. It is not possible to update the nested address with the users endpoint. Updates have to be done with the address endpoint.

The HTTP-verbs are 'GET' for retrieving data, 'POST' for creating entities, 'PUT' for updating entities, 'PATCH' for partially updating entities and 'DELETE' for deleting entities.