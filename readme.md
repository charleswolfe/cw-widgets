
**Installation**

cd to this directory

Install `pip` and `venv`


Then activate a virtual environment

`python3 -m venv widgets`

`source widgets/bin/activate`

Now install the packages into this virtual environment
`python -m pip install -r requirements.txt`

Copy .env.example to .env

cd to app/

`python manage.py runserver 8080`

Base Url will be http://127.0.0.1:8080/ for all requests


API spec is available in **openapi.yaml**. To regenerate OpenAPI spec, visit http://127.0.0.1:8080/schema 


To run bandit check (from app/) `bandit -r ../`

To run flake8 (from app/) `flake8 app`

To run tests (from app/) `./manage.py test`
