# Boilerplate Python Django sqlLite

## Running:

To run the Django server:
```
python manage.py runserver
```

## Get started:

### 1. Requirements
```
pip install django
pip install django_rest_framework
```
### 2. Create new project (optional)

Create a Django project called todo with the following command:
```
django-admin startproject <project_name>
```
Then, cd into the new <project_name> folder and create a new app for your API:
```
django-admin startapp <project_name_api>
```
**!!Before run your initial migrations, please decide to use which database engine. To get more instruction, please check Database Section!!**

Run your initial migrations of the built-in user model:
```
python manage.py migrate
```
Next, add rest_framework and todo to the INSTALLED_APPS inside the project_name/project_name/settings.py file:
```
# settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    '<project_name_api>'
]
```
Create a serializers.py and urls.py file in <project_name>/<project_name_api> and add new files as configured in the directory structure below:
```
├── <project_name>
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
├── db.sqlite3
├── manage.py
└── <project_name_api>
    ├── admin.py
    ├── serializers.py
    ├── __init__.py
    ├── models.py
    ├── urls.py
    └── views.py
```

Next, create a superuser. We’ll come back to this later:
```
python manage.py createsuperuser
```

### 3. Database:

After creating the model, migrate it to the database:
```
python manage.py makemigrations
python manage.py migrate
```# DjangoSqliteBoilerplate
