# Deploying a Simple Django App to Render.com: A Step-by-Step Guide

# Set-Up

* **[Install Python 3](https://realpython.com/installing-python/)** - 

* **[Install a Text Editor](https://realpython.com/courses/python-development-visual-studio-code-setup-guide/)** - VS Code

* **[Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)** 


* Make a new directory

```shell
mkdir render-prj
```

* Create a virtual environment within this new directory 

```shell
python3 -m venv .venv
```

* Activate a new virtual environment called .venv
```shell
source .venv/bin/activate
```

* Install Django, psycopg2-binary gunicorn dj-database-url
```shell
pip install django psycopg2-binary gunicorn dj-database-url 
```

* Create a new Django project called django-project
```shell
django-admin startproject django_project .
```

* Create a new app called example
```shell
django-admin startapp example
```

* Edit django_project/settings.py
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "example.apps.ExampleConfig",
]
```
* Build the templates directory within example folder

* Create index.html within templates folder

* Edit example/views.py

```python
from django.shortcuts import render

def mainView(request):
    return render(request, "index.html")
```

* Edit django_project/urls.py
```python
from django.contrib import admin
from django.urls import path
from example.views import mainView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", mainView),
]
```

* Navigate to http://127.0.0.1:8000/ in your web browser
![Sample output-1](https://github.com/nihathalici/Deploying-a-Simple-Django-App-to-Render-A-Step-by-Step-Guide/blob/main/screenshots/sample-screenshot-django-locally-running.png)


* Edit django_project/settings.py imports
```python
from pathlib import Path
import os # new
import dj_database_url # new 
```

* Edit django_project/settings.py SECRET_KEY
```python
SECRET_KEY = os.environ.get("SECRET_KEY", "563479vxw56867")
```

* Edit django_project/settings.py DEBUG settings
```python
DEBUG = 'RENDER' not in os.environ
```

* Edit django_project/settings.py DATABASE settings
```python
DATABASES = {
    'default': dj_database_url.config(
        conn_max_age=600,
        conn_health_checks=True,
    ),
}
```

* Edit django_project/settings.py ALLOWED_HOSTS settings
```python
ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
```

* Install django-cors-headers
```shell
pip install django-cors-headers
```

* Edit django_project/settings.py INSTALLED_APPS settings
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "example.apps.ExampleConfig"
    "corsheaders", # new
]
```

* Edit django_project/settings.py MIDDLEWARE settings
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",  # new
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

* Edit django_project/settings.py / Add CORS_ALLOW_ALL_ORIGINS
```python
WSGI_APPLICATION = 'django_project.wsgi.application'
CORS_ALLOW_ALL_ORIGINS = True  # new
```

* Create the setup.sh file in the project-level directory

* Create the deps.txt fiel
```shell
pip freeze > deps.txt
```

* Edit setup.sh file
```shell
pip install -r deps.txt
python manage.py migrate
```

* Make setup.sh executable
```shell
chmod +x setup.sh
```

* Deploying to GitHub
```shell
git init
git add .
git commit -m "first commit"
git remote add origin git@github.com:<your repo>
git remote -v
```

