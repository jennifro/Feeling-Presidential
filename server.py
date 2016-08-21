from flask import Flask, jsonify, render_template
from flask_debugtoolbar import DebugToolbarExtension
from model import Speech, Collocation, connect_to_db, db
# from flask.ext.login import LoginManager, UserMixin, login_required, login_user, logout_user


app = Flask(__name__)

app.secret_key = "whatevs"
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = "login"


def make_links():

    # list of the prez name & speech title nodes
    speech_lst = Speech.query.all()

    nodes = []

    for s in speech_lst:
        nodes.append({'speech': s.title, 'name': s.prez.name})

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

    paths = []

    for speech in nodes:
        if 'name' in speech:
            paths.append({'source': speech['name'], 'target': speech['speech'], 'type': 'prez-speech'})

        else:
            paths.append({'source': speech['speech'], 'target': speech['collocation'], 'type': 'speech-bigram'})

    return paths


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
