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

pip install -r requirements.txt
python run.py
````

#### README!!

Folder named 'frontend' contains our html files

Folder named 'app' hosts our api

This app will be described as a Single Page Application. Flask will only serve one html - index.html and our javascript and jquery will do the magic in the front end. Implementing an SPA is easier with the use of Javascript Based Frameworks, but we're going to transition gradually. 

Run the app by typing 'python run.py' 

**DATABASE**
We will be using stored procedure calls to interact with our database, hence, it will be a challenge to keep our dbs synced. BUT, a script has been created, to be run using 'python db.py' to setup our db tables and functions. 
