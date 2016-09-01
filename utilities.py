import regex as re
from nltk.corpus import stopwords
from model import connect_to_db, Speech, Collocation

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


def make_links():
    """Creates source/target/type dictionary for d3 force layout."""

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


def graph_data():
    """Makes a data dictionary for vis.js timeline."""

    all_speeches = Speech.query.all()

    items = []

    for stuff in all_speeches:
        # prez = stuff.prez.name
        date = stuff.title[-17:-1]    # cutting [-17:-1] of title gives the date of the speech as a string
        title = stuff.title[:-19]     # title w/ no trailing space.
        sentiment = stuff.sentiment

        items.append({'start': date, 'content': title, 'title': sentiment})

    return items


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    print 'Connected to DB!'
