import os
from flask import Flask, jsonify, render_template
# from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db
from utilities import make_nodes_and_links, graph_data


app = Flask(__name__)

# app.secret_key = "whatevs"
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'whatevs')


@app.route('/data.json')
def get_force_data():
    """Turn the links list of sources & targets into JSON."""

    nodes, links = make_nodes_and_links()

    return jsonify({'links': links, 'nodes': nodes})


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
