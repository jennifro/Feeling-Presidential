# routes for the app

from flask import jsonify, render_template
from utilities import make_nodes_and_links, graph_data
from app import app


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
