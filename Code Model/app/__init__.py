from flask import Flask

app = Flask(__name__, template_folder="../frontend", static_folder="../frontend/static")

from app import views
