import json
from model import connect_to_db, db
from model import President, Speech     # Collocation
from server import app
from bigramfinder import top_bigrams

data = open('allspeeches.json')

all_speech_info = json.load(data)

data.close()


def load_presidents():
    """Seed database with relevant presidents."""

     # cuz I'll probably redo db multiple times in testing
    President.query.delete()

    for text in all_speech_info:

        name = ''.join(text['president'])

        db_check = President.query.filter(President.name == name).first()

        if db_check is None:

            president = President(name=name)

            db.session.add(president)

    db.session.commit()


def load_speeches():
    """Seeds database with info on each speech"""

    Speech.query.delete()

    for text in all_speech_info:
        link = ''.join(text['url'])
        title = ''.join(text['title'])
        #  date of speech?

        speech = Speech(title=title, link=link)

        db.session.add(speech)

    db.session.commit()


# def load_speech_type():
#     """Seeds db with info on speech types (inaugural, SoU, etc)"""

#     # again, will probs re-do db
#     SpeechTypes.query.delete()

#     for text in all_speech_info:
#         title_data = all_speech_info[text]['title']
#         title_only = ''.join(title_data).split('(')
#         speech_type = title_only[0]

#         s_type = SpeechTypes(speech_type=speech_type)

#         db.session.add(s_type)

#     db.session.commit()


def load_collocations():
    """Seeds database with common bigrams in speeches"""

    stuff = top_bigrams()  # { prezname: { speech1: [(phrases) (moarphrases)] } }

    for prez in stuff:  # returns list for each prez
        for whatevs in stuff[prez]:
            c_speech = db.session.query(Speech.title == whatevs).first()
            print c_speech

    # find speech id corresponding to top_bigrams()
    # bind that to some var
    # for that speech in top_bigrams(), unpack list of tuples
    # add each tuple to db

if __name__ == '__main__':
    connect_to_db(app)

    db.create_all()

    # load_presidents()
    # load_speeches()
    # load_speech_type()
    # load_collocations()

############################
# OLD CODE:
# import string
# def get_speech_text():
#     """Returns a list of all speeches from scrapy json file."""
#     # Make a test here with a different file maybe?

#     full_corpora = []
#     excess = string.whitespace
#     clean_spaces = string.maketrans(excess, ' '*len(excess))

#     for x in range(len(all_speech_info)):
#         text = (''.join(all_speech_info[x]['speech'])).encode('ascii', 'ignore').lower()
#         text = text.translate(clean_spaces)
#         text = text.split()

#         full_corpora.append(text)

#     return full_corpora
