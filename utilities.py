import regex as re
from nltk.corpus import stopwords
from model import db, connect_to_db, President, Speech, Collocation

excess = stopwords.words('english')


def str_parser(sentence):
    """Takes a unicode string of any length, returns string as a list
    split into lowercase words without punctuation.

    >>> str_parser(u'Im just a Poor Boy, I need no sympathy.')
    [u'im', u'poor', u'boy', u'need', u'sympathy']

    >>> str_parser(u'...Easy come, easy go, LITTLE HIGH, little low.')
    [u'easy', u'come', u'easy', u'go', u'little', u'high', u'little', u'low']

    """

    all_lower = sentence.lower()

    clean_text = re.sub(r'\p{P}', '', all_lower)  # removes punctuatation from unicode

    indiv_words = clean_text.split()

    for word in excess:
        while word in indiv_words:
            indiv_words.remove(word)         # removes words like 'and', 'the', 'or'

    return indiv_words


def make_nodes_and_links():
    """Creates dataset for d3 force layout.

    Paths are source/target/type list of dictionaries, nodes are a list of
    id/name/group dictionaries.
    Node groups:
    1: president name
    2: speech title
    3: positive bigram
    4: neutral bigram
    5: negative bigram

    """

    # list of the prez name & speech title nodes to define paths/links
    speech_lst = Speech.query.all()
    phrase_lst = Collocation.query.all()
    prez_lst = President.query.all()

    # all pertinent nodes with group identifier & name that will be passed to d3
    nodes = []

    for item in prez_lst:
        nodes.append({'id': item.name, 'group': 1, 'name': item.name})

    for item in speech_lst:
        nodes.append({'id': item.title, 'group': 2, 'name': item.title})

    node_links = []

    for s in speech_lst:
        node_links.append({'speech': s.title, 'name': s.prez.name})

    # list of bigram/phrase & speech title nodes
    phrase_nodes = []

    for p in phrase_lst:
        # find the speech title for said phrase
        phrase_location = p.connect
        for phrase_info in phrase_location:
            phrase_title = Speech.query.filter(Speech.title == phrase_info.speech.title).first()
        phrase_nodes.append({'collocation': p.phrase, 'speech': phrase_title.title})

    # put all the nodes together in one list for paths/links
    node_links.extend(phrase_nodes)

    # identify how each node is connected, what is primary and what it points to.

    paths = []

    for speech in node_links:
        if 'name' in speech:
            paths.append({'source': speech['name'], 'target': speech['speech'],
                          'type': 'prez-speech'})

        else:
            paths.append({'source': speech['speech'], 'target': speech['collocation'],
                          'type': 'speech-bigram'})

    # add bigrams in speeches to nodes w/ pos, neg or neutral grouping
    # TO FIX:
    for p in phrase_nodes:

        phrase = p['collocation']

        q = Collocation.query.filter(Collocation.phrase == phrase).first()

        if q.sentiment_score == 'positive':
            nodes.append({'id': q.phrase, 'group': 3, 'name': q.phrase})

        elif q.sentiment_score == 'neutral':
            nodes.append({'id': q.phrase, 'group': 4, 'name': q.phrase})

        elif q.sentiment_score == 'negative':
            nodes.append({'id': q.phrase, 'group': 5, 'name': q.phrase})

    return nodes, paths


def graph_data():
    """Makes a data dictionary for vis.js timeline."""

    all_speeches = Speech.query.all()

    items = []

    for stuff in all_speeches:
        # prez = stuff.prez.name
        date = stuff.title[-17:-1]    # cutting [-17:-1] of title gives the date of the speech as a string
        title = stuff.title[:-19]     # title w/ no trailing space.
        sentiment = stuff.sentiment

        items.append({'start': date, 'content': title, 'group': sentiment})

    groups = [{'id': 'pos', 'content': 'positive'},
              {'id': 'neg', 'content': 'negative'}]

    return items, groups


#################################
# for testing this file only, must connect to db.

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    print 'Connected to DB!'
