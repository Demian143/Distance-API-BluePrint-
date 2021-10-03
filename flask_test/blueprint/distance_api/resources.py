from flask import abort
from flask_restful import Resource
from .scrapper import calc_distance


class DistanceResource(Resource):
    def get(self, address):
        obj = calc_distance(address)
        return {address: obj['Point']} or abort(204)
