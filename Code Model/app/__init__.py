from flask import Flask, Blueprint, current_app
from config import config
from flask.ext.cors import CORS

api = Blueprint('api', __name__)


def create_app(_config='development'):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config[_config])

    from app.inventory import controller

    app.register_blueprint(api)

    return app
