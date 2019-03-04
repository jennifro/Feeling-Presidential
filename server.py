import os
from flask import Flask, json, jsonify, render_template
# from flask_debugtoolbar import DebugToolbarExtension
from model import db, connect_to_db
from utilities import make_nodes_and_links, graph_data


app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'whatevs')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/forceData')
def get_force_data():
    """Turn the links list of sources & targets into JSON."""

    nodes, links = make_nodes_and_links()
    forceData = {'links': links, 'nodes': nodes}

    response = app.response_class(
        response=json.dumps(forceData),
        status=200,
        mimetype='application/json'
    )

    return response


@app.route('/')
def index():
    """Main page with d3 force layout."""
    return render_template('index.html')


@app.route('/timeline.json')
def get_timeline_data():
    """Create JSON data object for chart.js."""
    items, groups = graph_data()

    return jsonify({'items': items, 'groups': groups})


@app.route('/timeline')
def second_page():

    return render_template('timeline.html')


@app.route('/error')
def error():
    raise Exception('Error!')



if __name__ == "__main__":

    connect_to_db(app, os.environ.get('DATABASE_URL'))

    DEBUG = "NO_DEBUG" not in os.environ
    PORT = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
