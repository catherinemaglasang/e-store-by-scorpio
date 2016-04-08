import decimal
import flask.json
from flask import Flask, Blueprint, current_app
from config import config
from flask.ext.cors import CORS

api = Blueprint('api', __name__)


class MyJSONEncoder(flask.json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            # Convert decimal instances to strings.
            return str(obj)
        return super(MyJSONEncoder, self).default(obj)


def create_app(_config='development'):
    app = Flask(__name__)

    CORS(app)

    app.config.from_object(config[_config])
    app.json_encoder = MyJSONEncoder

    from app.inventory import views
    from app.cart import views
    from app import views

    app.register_blueprint(api)

    return app
