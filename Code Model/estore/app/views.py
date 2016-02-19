import json
from flask import render_template, flash, redirect, request, session
from flask import jsonify
from app import app, db
from app.models import User


@app.route('/')
def index():
	return render_template('index.html', title='Home')
