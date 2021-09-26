from flask import Blueprint, render_template, request
from scrapper import calc_distance

search_blueprint = Blueprint(
    'search_blueprint', __name__, template_folder='templates')


@search_blueprint.route('/<int:longlat>', methods=['POST', 'GET'])
def _search_blueprint(longlat):
    if request.method == "POST":
        result = calc_distance(longlat)
        context = {'result': result}

        return render_template('result.html', context=context)

    else:
        return render_template('form.html')
# i need to pass into a http request
