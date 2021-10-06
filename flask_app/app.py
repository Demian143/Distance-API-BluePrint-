from flask import Flask
from .blueprints import distance_api

app = Flask(__name__)


distance_api.init_app(app)
