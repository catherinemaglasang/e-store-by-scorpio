from flask import Flask, Blueprint
from config import config

app = Flask(__name__)
app.config.from_object(config['development'])

from app import views
