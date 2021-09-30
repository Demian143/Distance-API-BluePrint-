from flask import Flask
from . import blueprint

app = Flask(__name__)

blueprint.init_app(app)
