import os 
import flask
import sys
from flask import Flask, jsonify
from app.models import DBconn

app = Flask(__name__)
<<<<<<< HEAD:Code Model/app/__init__.py

=======
>>>>>>> a74407d51d360d03b2835b3ac16b974d32bf91fc:Code Model/estore/app/__init__.py

def spcall(qry, param, commit=False):
    try:
        dbo = DBconn()
        cursor = dbo.getcursor()
        cursor.callproc(qry, param)
        res = cursor.fetchall()
        if commit:
            dbo.dbcommit()
        return res
    except:
        res = [("Error: " + str(sys.exc_info()[0]) + " " + str(sys.exc_info()[1]),)]
    return res

from app import views
