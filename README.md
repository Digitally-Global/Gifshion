# Gifshion

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Digitally-Global/Gifshion.git
$ cd Gifshion
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

To make any update to the models file

```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

To Create an admin User

```sh
$ python manage.py createsuperuser
```

To Collect Static Files

```sh
$ python manage.py collectstatic
```

For More Details visit Official Django Docs https://docs.djangoproject.com/en/4.2/
