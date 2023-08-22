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

