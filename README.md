# news-management

A Django project to manage articles and users in a newspaper.

## Requirements

- Python 3.11
- Django 4.1.11
- Django REST Framework 3.14.0
- MySQL 8.0.34
- drf-spectacular 0.26.5 (for API documentation)

and a couple of Python packages listed in `requirements.txt` file.

## Installation on development environment

First, run SQL script in `sql/db_creation.sql` file to create database and database user for Django to access MySQL server.

Create virtual environment `venv` for project (using virtualenv) and install required packages in `requirements.txt`:

```commandline
py -m pip install virtualenv
py -m virtualenv venv

# Activate virtual environment
# On Ubuntu
source venv/bin/activate
# On Windows
.\venv\Scripts\activate

# Install packages
py -m pip install -r requirement.txt
```

Generate tables and initial data to database:

```commandline
cd newsmanagement
.\manage.py migrate
```

Start development web server, use this command:

```commandline
cd newsmanagement
.\manage.py runserver
```

Now you can test APIs using curl, httpie, Postman, etc.

## Testing

To test some function and APIs in the project, use the command below:

```commandline
cd newsmanagement
.\manage.py test newsmanagement.tests
```


## API Documentation

To create schema file for API documentation (OpenAPI 3.0, Swagger UI), run the command below:

```commandline
cd newsmanagement
.\manage.py spectacular --color --file schema.yml

# Then, start web server
.\manage.py runserver
```

You can browse API documentation on web browser via http://127.0.0.1:8000/docs/

![API documentation](/images/1.png)
*API documentation generated using drf-spectacular*

## Docker
### Prerequisites
- Docker 24.0.6
- Docker Compose 1.27.4

### Installation

First, build docker image:

```commandline
sudo docker-compose build
```

Run app through docker compose on port 8000:
```commandline
sudo docker-compose up
```

![docker compose](/images/2.png)
*Run app successfully using docker-compose*