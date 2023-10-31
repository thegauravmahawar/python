# Django

Django comes with the `django-admin` utility that creates a project's skeleton. 

- `project`: a collection of settings for Django instance, applicable to the whole website;
- `application`: a submodule of a project that implements certain functionalities.

## Commands

**Start project**

```shell
mkdir app
cd app
django-admin startproject api . # start project in current directory
```

**Start application**

```shell
cd api
django-admin startapp user
```

## manage.py

This file is a command-line utility for administrative purposes. One can interchangeably use 
`django-admin <command>` or `python manage.py <command>`.

Some of the common commands executed with manage.py:

- `runserver`
- `makemigrations`
- `migrate`

## settings.py

This file contains various project-level parameters such as language and time-zone setup or 
definition of database.

In the beginning, default values will be enough, though you will need to add your application 
name to the `INSTALLED_APPS` variable.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user',
    'todo',
]
```

## models.py

`Model` component is in charge of the data in your project. It includes all the database 
operations with the project's business objects. A **business object** reflects a structured 
piece of data from your application that you want to store persistently or temporarily.

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
```

## views.py and urls.py

In `urls.py`, we define the routing for our service. **Routing** is a process of matching 
request links with appropriate **view handlers**. A view handler is a function or a class 
that responds to requests.

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.sites.urls),
]
```

Now we define how to respond to requests that we receive in `urls.py` by linking them with views.

```python
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.example_view, name='VIEW_NAME')
]
```

The `urls.py` file in an application defines routes specific to that application.

View handlers are defined in the corresponding `views.py` file. View functions play a mediator 
role between the model and the templates layer. 

```python
from django.http import HttpResponse

def example_view(request):
    return HttpResponse('Hello, World!')
```

