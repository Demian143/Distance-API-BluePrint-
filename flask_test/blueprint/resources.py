from flask import abort, render_template
from flask_restful import Resource
from .scrapper import calc_distance


class DistanceResource(Resource):
    def get(self, address):
        obj = calc_distance(address)
        return render_template(obj['Address']) or abort(204)
