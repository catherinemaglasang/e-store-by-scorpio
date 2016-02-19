from flask import Flask, jsonify, make_response, abort, request
from flask.ext.bcrypt import Bcrypt
from flask.ext.sqlalchemy import SQLAlchemy
import os 


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

from app import views, models