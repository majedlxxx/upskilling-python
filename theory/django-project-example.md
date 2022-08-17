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
- navigate to app_name/models.py, then create a class that represent a table in the database

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
