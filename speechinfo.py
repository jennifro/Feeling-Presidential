import json
import string
from model import connect_to_db, db
from model import Speech
from model import SpeechTypes
from server import app

data = open('allspeeches.json')

all_speech_info = json.load(data)


def get_speech_text():
    """Returns a list of all speeches from scrapy json file."""
    # Make a test here with a different file maybe?

    full_corpora = []
    excess = string.whitespace
    clean_spaces = string.maketrans(excess, ' '*len(excess))

    for x in range(len(all_speech_info)):
        text = (''.join(all_speech_info[x]['speech'])).encode('ascii', 'ignore').lower()
        text = text.translate(clean_spaces)
        text = text.split()

        full_corpora.append(text)

    return full_corpora


def load_speeches():
    """Seeds database with info on each speech"""

    for text in all_speech_info:
        link = all_speech_info[text]['url']
        prez = all_speech_info[text]['president']
        title = all_speech_info[text]['title']

        speech = Speech(title=title, speaker=prez, link=link)

        db.session.add(speech)

    db.session.commit()


def load_speech_type():

    for text in all_speech_info:
        title_data = all_speech_info[text]['title']
        title_only = ''.join(title_data).split('(')
        speech_type = title_only[0]

        s_type = SpeechTypes(speech_type=speech_type)

        db.session.add(s_type)

    db.session.commit()

if __name__ == '__main__':
    connect_to_db(app)

    db.create_all()

    load_speeches()
    load_speech_type()
