from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON

app = Flask(__name__)
db = SQLAlchemy(app)

class AddProduct():
    id = db.Column('', db.Char, primary_key=True)