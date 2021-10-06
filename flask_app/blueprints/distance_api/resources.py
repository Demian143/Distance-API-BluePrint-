from flask import abort
from flask_restful import Resource
from .scrapper import Search


class DistanceResource(Resource):
    def get(self, address):
        # Call the main class Search to make calc distance
        # have access to the inner search_soup() call
        search = Search()
        distance = search.calc_distance(address) or abort(204)
        return f'{distance}' or abort(204)
