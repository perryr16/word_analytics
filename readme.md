 # About 
 Word Analytics is a Django app that analyzes the content of a web article. Information regarding word frequency, tone, and a sample of the article are available. 

 The app creates tone models based on the IBM Watson API.

 Charts are generated using the chart.js library.

 Users can upload article data using the new artifle form.

 # Entering the Python Environment 
  1. Create the virtual enviornment 
  - Change directory to root of project
  - `$ virtualenv word_analytics_env`
  2. Enter the Environment 
  - in the root directory 
  - `$ source word_analytics_env/bin/activate`
  
# Requirements
- Python version: 3.8 or higher
- virtualenv version: 20.0.31
- Postgres database

# Getting Started
### Installing dependancies
```
$ cd word_analytics_root
$ virtualenv word_analytics_env
$ source word_analytics_env/bin/activate 
$ pg_config
$ which pg_config 
$ pip install psycopg2 
$ pip install django 
```
### Database Config
change settings.py for DATABASE
```DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'word_analytics_db',
        'USER': <Postgres UserName>
        'PASSWORD':'',
        'HOST': 'localhost',
        'PORT':'',
    }
}
```

```
$ createdb project_name_db
$ createdb project_name_db_test
```
### Initial Database
```
$ pythion manage.py makemigrations #
> No changes detected 
$ python manage.py migrate # create default schema
$ python manage.py createsuperuser
$ python manage.py runserver
```