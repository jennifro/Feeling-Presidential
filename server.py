from flask import Flask
# from flask_debugtoolbar import DebugToolbarExtension
from model import President, Speech, Collocation, SpeechCollocation, db, connect_to_db

app = Flask(__name__)


def make_nodes():

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

    # i think i need a single big list

    nodes = prez_speeches
    nodes.extend(phrases)

    #### works up to here ######

    # index_nodes = {}

    # for idx, fml in enumerate(nodes):
    #     index_nodes[fml['title']] = (idx, fml['name'])
    #     index_nodes[fml['collocation']] = (idx, fml['speech'])  # speech throws key error

    # return index_nodes

    prez_speech_index_nodes = {}

    for idx, stuff in enumerate(prez_speeches):
        prez_speech_index_nodes[stuff['title']] = (idx, stuff['name'])

    phrase_index_nodes = {}

    for idx, thing in enumerate(phrases):
        phrase_index_nodes[thing['collocation']] = (idx, thing['speech'])

    paths = []

    for idc in prez_speeches:
        # connect on something
        # speech title to speech title in phrase?


# @app.route('/data.json')
# """jsonify output of helper function"""


# @app.route('/')
# def index():
#     html = "<html><body><h1>Homepage here!</h1></body></html>"
#     return html

if __name__ == "__main__":
    app.debug = True

    # DebugToolbarExtension(app)

    # app.run(host="0.0.0.0")

    connect_to_db(app)
