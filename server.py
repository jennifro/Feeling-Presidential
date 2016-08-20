from flask import Flask, jsonify
# from flask_debugtoolbar import DebugToolbarExtension
from model import President, Speech, Collocation, SpeechCollocation, db, connect_to_db

app = Flask(__name__)


def make_links():

    # list of the prez name & speech title nodes
    speech_lst = Speech.query.all()

    nodes = []

    for s in speech_lst:
        nodes.append({'title': s.title, 'name': s.prez.name})

    # list of bigram/phrase & speech title nodes
    phrase_nodes = []

    phrase_lst = Collocation.query.all()

    for p in phrase_lst:
        # find the speech title for said phrase
        phrase_location = p.connect
        for phrase_info in phrase_location:
            phrase_title = Speech.query.filter(Speech.title == phrase_info.speech.title).first()
        phrase_nodes.append({'collocation': p.phrase, 'speech': phrase_title.title})

    # put all the nodes together in one list
    nodes.extend(phrase_nodes)

    # identify how each node is connected, what is primary and what it points to.

    links = []

    for speech in nodes:
        if 'name' in speech:
            links.append({'source': speech['name'], 'target': speech['title']})

        else:
            links.append({'source': speech['speech'], 'target': speech['collocation']})

    return links, 'NODES AQUI', nodes


@app.route('/data.json')
def get_force_data():
    """Turn the links list of sources & targets into JSON."""

    return jsonify(make_links())


# @app.route('/')
# def index():
#     html = "<html><body><h1>Homepage here!</h1></body></html>"
#     return html

if __name__ == "__main__":
    app.debug = True

    # DebugToolbarExtension(app)

    # app.run(host="0.0.0.0")

    connect_to_db(app)
