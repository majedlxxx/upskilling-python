# Django example
## Creating the project
```
django-admin startproject project_name
```
* a directory holding the project's name will be created. within that folder you will find:
    * manage.py
    * project's folder which contains:
        - settings.py
        - urls.py
        - other files to be used when deploying the application
## Creating our first app
```
python3 manage.py startapp app_name
```
* Add the created app to the installed_apps list found in settings.py file 
* the application folder contains:
    - models.py
    - views.py
    - admin.py
    - tests.py
    - migrations
    - Other configuration files

## Creating our first model
- navigate to app_name/models.py, then create a class that represent a table in the database [Documents](https://docs.djangoproject.com/en/3.2/topics/db/models/)

## Configuring database
- By default Django uses SQLite as a database. And stores our data/tables in a file called db.sqlite3
- The default configurations can be altered by modifying the variable DATABASES found in settings.py [Documents](https://docs.djangoproject.com/en/3.2/ref/databases/)


## Creating migrations and apply them
```
python3 manage.py makemigrations
```
* Migrations are a bunch of scripts that can modify the database by adding new tables or altering them.
* After running the above command migration scripts will be added to app_name/migrations/
* About migrations:
    - for each app the migrations are numbered 0001 0002 and so on.
    - to apply the migrations you can use(applying the changes that these scrip imply):
    ```
    python3 manage.py migrate
    ```
    * after running the migrate command by default django will apply all new migrations to the database. however we can specify which migrations we can apply by using the command:
        - to specify application(s):
        ```
        python3 manage.py migrate app1 app2
        ```
        - to specify a certain migration within an application / can be used rollbacks
        ```
        python3 manage.py migrate app #number
        ```
    * After migrating to the database the tables will be names "appname_className"
    * To check it in your sqlite3 database:
        * python3 manage.py shell
        * .tables
    * To check the migrations you can view the migrations table:
        * .mode columns
        * .headers on
        * SELECT * from django_migrations;

## Creating our first View
* in app_name/views create a view function that can return one of the following:
    - Json response
    - http response
    - render

* If I am creating an API the I will most likely need to use JSON responses only.
* But if I am developing a full website I will need to render a template and to do so:
    - create templates folder "app_name/templates"
    - within that folder create an HTML page.
    - let the view render that html page


## Linking the urls to your view:
- create a urls.py file in your app_name folder
- let the project's urls.py file point to the application's urls.py file using the method include
- let the application's urls.py point to your newly created view.

## Running the server and testing it out:
```
python3 manage.py runserver
```

* Navigate to http://127.0.0.1:8000/


## Admin page
* Create an admin user:
```    
python3 manage.py createsuperuser
```
* navigate to app_name/admin.py and register your model

## Creating a User model:
- Django has a built-in user model called "AbstractBaseUser" and another called "AbstractUser".
- Instead of implementing a User model from scratch we can usually extend(inherit) the built-in model.[Documents](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/)
- To specify your custom user model to be the default authentication model you just add the variable "AUTH_USER_MODEL" to settings.py
- [Example](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html)