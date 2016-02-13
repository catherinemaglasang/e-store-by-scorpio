from flask import render_template, flash, redirect, request
from flask import jsonify
from app import app
from app import db
from .models import *


@app.route('/')
def index():
	return render_template('index.html', title='Home') 

class AddCostumer(View):
    def post(self, request):
        # Get data
        costumer_id = request.POST['costumer_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        city = request.POST['city']
        state = request.POST['state']
        postal_code = request.POST['postal_code']
        country = request.POST['country']
        phone = request.POST['phone']
        email = request.POST['email']
        user_id = request.POST['user_id]
        billing_address = request.POST['billing_address']
        shipping_address = request.POST['shipping_address']
        
        
        
