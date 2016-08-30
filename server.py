from flask import Flask, jsonify, render_template
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db
from utilities import make_links


app = Flask(__name__)

app.secret_key = "whatevs"


@app.route('/data.json')
def get_force_data():
    """Turn the links list of sources & targets into JSON."""

    paths = make_links()

    return jsonify({'paths': paths})


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.debug = True

    DebugToolbarExtension(app)

    connect_to_db(app)

    app.run(host="0.0.0.0")
