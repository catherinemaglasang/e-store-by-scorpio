from flask import Flask, Blueprint, current_app
from config import config

api = Blueprint('api', __name__)

def create_app(_config='development'):
    app = Flask(__name__)
    app.config.from_object(config[_config])

    from app import views
    from app.product import controller
    from app.product.controller import api

    app.register_blueprint(api)

    return app
