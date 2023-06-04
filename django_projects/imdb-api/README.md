# IMDB REST API

## Docker Commands

**Build or rebuild services.**

```commandline
docker-compose build
```

**Create and start containers.**

```commandline
docker-compose up
```

## Linting & Testing

**Linting**

```commandline
docker-compose run --rm app sh -c "flake8"
```

**Run Tests**

```commandline
docker-compose run --rm app sh -c "python manage.py test"
```

## Django Commands

**Start project**

```commandline
docker-compose run --rm app sh -c "django-admin startproject app ."
```