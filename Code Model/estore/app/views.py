from flask import render_template, flash, redirect, request
from flask import jsonify
from app import app
from app import db
from .models import *


@app.route('/')
def index():
	return render_template('index.html', title='Home') 