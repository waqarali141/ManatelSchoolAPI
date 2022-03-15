# ManatelSchoolAPI

## Overview
### Execution environment
#### Web Application
- python 3.8
- [Django 4.0.3](https://docs.djangoproject.com/en/4.0/)
#### Database
- [(PostgreSQL)](https://cloud.google.com/sql/docs/postgres/)

## Getting Start
### Start app in local environment
- Prepare
> Make sure you've git, python (3.8) and pipenv installed on your machine
- Download
```
git clone https://github.com/waqarali141/ManatelSchoolAPI.git
cd ManatelSchoolAPI
```

- Install packages
```
pip install pipenv
pipenv install
```
> set enviroment vairables
```bash
export DJANGO_SETTINGS_MODULE='config.settings.settings'
export SECRET_KEY='...'
... # see the the full list in settings
You can enviroment files in the project and can export using python dotenv library
```
OR
To add environment variables in PyCharm you can use the plugin [EnvFile](https://github.com/Ashald/EnvFile)


- PostgreSQL Database
You can use your local database:
```
CREATE DATABASE school_db;
```

or use docker container
```
docker-compose up -d
```

- Migrate Database to apply changes from your current branch
```
python manage.py migrate
```

- Run runserver
```
python manage.py runserver
```
Starting development server at http://127.0.0.1:8000/

-Install git-hooks
```
pre-commit install
```
 update migrate file
```
python manage.py makemigrations
python manage.py migrate
```

### Development breakdown:

 - Setting up project env (Bolierplate): ~ 2 hours (In cludes, Postgres Docker, Settings, Env)
 - Setting up PipFile: ~ 1 including check and scrpits
 - Building the API's: ~ 1.5 hours including routes, corner cases.
 - Writing TestCode: ~ 1 hour

