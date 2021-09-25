from flask import Blueprint, render_template, request
from scrapper import calc_distance

search_blueprint = Blueprint(
    'search_blueprint', __name__, template_folder='templates')


@search_blueprint.route('/', methods=['POST', 'GET'])
def _search_blueprint():
    if request.method == "POST":
        form = request.form['search']
        result = calc_distance(form)
        context = {'form': form, 'result': result}

        return render_template('result.html', context=context)

    else:
        return render_template('form.html')
