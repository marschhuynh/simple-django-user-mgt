# Instruction

## Install dependecies

```shell
pip install -r requirements.txt
```

## Prepare database

- First

```shell
python manage.py migrate usermgt
```

- Second

```shell
python manage.py migrate
```

## Run server

```shell
python manage.py runserver
```
