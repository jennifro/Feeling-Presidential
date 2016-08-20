from flask import Flask, jsonify
# from flask_debugtoolbar import DebugToolbarExtension
from model import President, Speech, Collocation, SpeechCollocation, db, connect_to_db

app = Flask(__name__)


def make_links():

    # list of {speech title: president}
    speech_lst = Speech.query.all()

    prez_speeches = []

    for s in speech_lst:
        prez_speeches.append({'title': s.title, 'name': s.prez.name})

    # print prez_speeches

    # list of {phrase: respective speech}
    phrases = []

    phrase_lst = Collocation.query.all()

    for p in phrase_lst:
        # find the speech title for said phrase
        phrase_location = p.connect
        for phrase_info in phrase_location:
            phrase_title = Speech.query.filter(Speech.title == phrase_info.speech.title).first()
        phrases.append({'collocation': p.phrase, 'speech': phrase_title.title})

    links = []

    # {'name': u'Barack Obama', 'title': u'2010 State of the Union Address (January 27, 2010)'}
    for speech in prez_speeches:
        links.append({'source': speech['name'], 'target': speech['title']})

    for bigram in phrases:
        links.append({'source': bigram['speech'], 'target': bigram['collocation']})

    return links


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
