from flask import Flask, jsonify, make_response, abort, request
from flask.ext.sqlalchemy import SQLAlchemy
import os 
import config

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)
db = SQLAlchemy(app)

from app import views, models