This week I learned about PythonAnywhere and how to install Django on it.

Reference sources:
- https://www.dj4e.com/assn/dj4e_install.md
- https://docs.djangoproject.com/en/3.0/intro/tutorial01/

### Setting up environment

First of all, I created a virtual environment with Python 3 and Django 3 on PythonAnywhere and then configura it. All commands that I used are listed bellow.

```console
mkvirtualenv django3 --python=/usr/bin/python3.6
pip install django
workon django3
```

### Copy of the sample code for Django for Everybody

```console
cd ~
git clone https://github.com/csev/dj4e-samples
cd dj4e-samples
pip install -r requirements.txt
python3 manage.py check
```

### Run migrations

```console
python3 manage.py makemigrations
python3 manage.py migrate
```

### Building my application

```console
cd ~
mkdir django_projects
cd django_projects
django-admin startproject mysite
```

I edited the `~/django_projects/mysite/mysite/settings.py` file and changed the *allowed hosts* line at line 28.

```py
ALLOWED_HOSTS = [ '*' ]
```

### Running my application

In the PythonAnywhere web interface I navigated to the `web` tab and created a new web application. Then I made some changes to the web app configuration: I set the path for **Source code**, **Working directory** and **Virtualenv**.

```
Source code: /home/(my-account)/django_projects/mysite
Working directory: /home/(my-account)/django_projects/mysite
Virtualenv: /home/(my-account)/.virtualenvs/django3
```

Also I edited the **WSGI configuration file** and replaced all code into it.

```py
import os
import sys

path = os.path.expanduser('~/django_projects/mysite')
if path not in sys.path:
    sys.path.insert(0, path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())
```

So I pressed *reload* in the `web` tab and my app was already running at `http://(my-account).pythonanywhere.com/`!

### Adding Polls Application

```console
cd ~/django_projects/mysite
python3 manage.py startapp polls
python3 manage.py check
```

I opened the `~/django_projects/mysite/polls/views.py` file and put Python code in it.

```py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

In the same folder `~/django_projects/mysite/polls` I created a file called `urls.py` and put more code.

```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

Lastly, I opened the `~/django_projects/mysite/mysite/urls.py` file and configured some more stuff.

```py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

### Checking if everything is ok

The `check` does a check for syntax and logic errors in my Django application.

```console
python3 manage.py check
```

Again, I reloaded my application from the `web` tab and my app was already running on `(my-account).pythonanywhere.com/polls`.
