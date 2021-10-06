from flask import Blueprint
from flask_restful import Api
from .resources import DistanceResource

bp = Blueprint("distance_api", __name__, url_prefix="/api/v1")
api = Api(bp)
api.add_resource(DistanceResource, "/distance/<address>")


def init_app(app):
    app.register_blueprint(bp)
