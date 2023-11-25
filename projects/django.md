# Django

## References

- [Django Introduction](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)
- [Django Model Indexes](https://docs.djangoproject.com/en/4.2/ref/models/indexes/)
- [Django Rest Framework](https://www.django-rest-framework.org)
- [Django Rest Framework - Serializers](https://testdriven.io/blog/drf-serializers/)
- [Effectively Using DRF 1](https://profil-software.com/blog/development/10-things-you-need-know-effectively-use-django-rest-framework/)
- [Effectively Using DRF 2](https://www.velotio.com/engineering-blog/using-drf-for-faster-apis)
- [Django Rest Framework - Best Practices](https://rpep.dev/posts/best-practices-django-views/)
- [Custom Exception Handling](https://medium.com/turkcell/request-validation-and-custom-exception-handling-in-django-rest-framework-649fddecb415)
- [Custom User Model](https://dev.to/earthcomfy/getting-started-custom-user-model-5hc)


Django comes with the `django-admin` utility that creates a project's skeleton.

- `project`: a collection of settings for Django instance, applicable to the whole website;
- `application`: a submodule of a project that implements certain functionalities.

An app is a web application that does something - e.g., a blog system, a database of public
records or a small poll app. A project is a collection of configuration and apps for a
particular website. A project can contain multiple apps. An app can be in multiple projects.

## Commands

**Start project**

```shell
mkdir todo-api
cd todo-api
django-admin startproject config . # start project in current directory
```

**Start application**

```shell
cd api
django-admin startapp app
```

**Make migrations**

```shell
python manage.py makemigrations app_name
```

**Run migrations**

```shell
python manage.py migrate app_name
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
    'app',
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

## Create Superuser

```shell
python3 manage.py createsuperuser
```