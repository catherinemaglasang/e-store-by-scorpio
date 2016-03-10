from flask import Flask

app = Flask(__name__, static_folder="../frontend/static", template_folder="../frontend")

from app import views
