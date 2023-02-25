
<h2 align="center"> Project Installation </h2>
<br>

#### Clone the repository using the following command

```bash
git clone https://github.com/yeazin/log-f-django.git
# After cloning, move into the directory 
# having the project files 
```
#### Create a virtual environment where all the required python packages will be installed

```bash
# Use this on Windows
python -m venv env
# Use this on Linux and Mac
python3 -m venv env
```
#### Activate the virtual environment

```bash

# Windows
env\Scripts\activate.bat

# Linux and Mac
source env/bin/activate

```
#### Install all the project Requirements

```bash

pip install -r require.txt

```
#### Database Setup
We can use default db sqlite or postgreseql <br>
By default DB sqlite. We can use postgresql as <br>
All the config has been given to settings file<br>
We have to just uncomment the code on there

```bash 
"""
Postgres setup 
"""

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

Note : before using Postgres we have to comment down the basic config of default DB sqlite .
Then We can proceed to the Next step
```

#### Apply migrations and create your superuser (follow the prompts)

```bash

# Apply make migrations
python manage.py makemigrations

# apply migrations and create your database
python manage.py migrate

# Create a user with manage.py
python manage.py createsuperuser

```

#### Run the development server

```bash
# run django development server
python manage.py runserver

```
Now we are good to Go . We can check the [127.0.0.1:8000](http://127.0.0.1:8000) <br> for The root API documention.
<br>


<h2 align="center"> Project Structure</h2>
<br>

```bash 


    mainConfig/  #Root Config folder
        |-- __init__.py
        |__ settings/
            |-- base.py # base settings
            |-- development # development settings)
        |-- urls.py (Root URL file)
        |-- wsgi.py
        |-- asgi.py
    
    base/
        |-- __init__.py
        |-- models.py # base models for timestamp

    accounts/ 
        |-- __init.py
        |-- models.py # database file
        |-- views 
        |-- serializer.py # API file
        |-- urls.py # accounts URL file)
        |-- admin.py


    |-- manage.py
    |-- .env  
    |-- .gitignore
    |-- require.txt # package dependency file
    

```

If you have any query Please contact : 
nazrulislamyeasin@gmail.com