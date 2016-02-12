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
