## Project e-store

#### Running the app locally (Type the ff in terminal)
````
pip install virtualenv
pip install virtualenvwrapper

sudo nano ~/.bashrc 
# Add the ff line at the end of the file: source '/usr/local/bin/virtualenvwrapper.sh'
source ~/.bashrc

mkvirtualenv estore
workon e-store		# activate virtualenv

# Add the ff lines in you virtualenv activate.py file
# export DATABASE_URL = "postgresql://yourusername:yourpassword@localhost/yournewdb"
# export APP_SETTINGS="config.DevelopmentConfig"

pip install -r requirements.txt
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python manage.py runserver
# Then each time the database models change repeat the migrate and upgrade commands.
````

#### Tools / Modules
````
Flask-SQLAlchemy - ORM
Flask-Migrate - Migrations
Flask-RESTful - Building API backend
````

#### Tutorials
- https://realpython.com/blog/python/handling-user-authentication-with-angular-and-flask/
