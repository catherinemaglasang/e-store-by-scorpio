from app import db
from datetime import datetime
from flask import url_for

class User(db.Model):
    """An admin user capable of viewing reports.

    :param str email: email address of user
    :param str password: encrypted password for the user

    """
    email = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)

    def __repr__(self):
        return '%s' % (self.email)