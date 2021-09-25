from flask import Flask
from search_blueprint import search_blueprint

app = Flask(__name__)
app.register_blueprint(search_blueprint, url_prefix='/blueprint')


@app.route('/')
def index():
    return '<h1>Test</h1>'


if __name__ == "__main__":
    app.run(debug=True)
