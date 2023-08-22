# Set-Up

* **[Install Python 3](https://realpython.com/installing-python/)** - 

* **[Install a Text Editor](https://realpython.com/courses/python-development-visual-studio-code-setup-guide/)** - VS Code

* **[Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)** 

* **[Install Docker](https://hub.docker.com/)**

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

* Install Django
```shell
python -m pip install django~=4.0.0
```

* Upgrade pip
```shell
python -m pip install --upgrade pip
```

* Create a new Django project called django-project
```shell
django-admin startproject django_project .
```

* Initialize the database
```shell
python manage.py migrate
```

* Start the local web server
```shell
python manage.py runserver
```

* Django is running: Open the URL http://127.0.0.1:8000/ in your browser to view Django's welcome page

![Sample output Set-Up](https://github.com/nihathalici/Deploying-a-Simple-Django-App-to-Render-A-Step-by-Step-Guide/blob/main/S-01-Set-Up/screenshots/setup-sample-screenshot.png)


