from flask import Flask, redirect, url_for, render_template, request
from selen import search_geocode, calc_distance

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index_search():
    if request.method == "POST":
        consult = request.form['search']
        search_verbose = search_geocode(consult)
        search_ll = calc_distance(search_verbose)
        return '<h2>Result for:</h2> <p>{}</p> <br> <h2>Your distance from MKAD:</h2><p>{}</p>'.format(search_verbose, search_ll)
    else:
        return render_template('form.html')
