from flask import Blueprint
from flask_restful import Api
from .resources import DistanceResource

bp = Blueprint("distance_api", __name__,
               template_folder='templates', url_prefix="/")
api = Api(bp)
api.add_resource(DistanceResource, "/<address>")


def init_app(app):
    app.register_blueprint(bp)
