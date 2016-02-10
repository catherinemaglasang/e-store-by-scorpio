# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.dialects.postgresql import JSON

# app = Flask(__name__)
# db = SQLAlchemy(app)

# class Category(db.Model):
#     name = db.Column(db.String)

# class Product(db.Model):
#     id = db.Column(db.String(), primary_key=True)
#     description = db.Column(db.String())
#     category_id = db.Column('Category')
