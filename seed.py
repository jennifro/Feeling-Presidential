import json
from model import connect_to_db, db
from model import President, Speech, Collocation, SpeechCollocation
from server import app
from bigramfinder import top_bigrams, bigram_sentiment
from analyzer import analyze_speeches

data = open('allspeeches.json')

all_speech_info = json.load(data)

data.close()


def load_presidents():
    """Seed database with relevant presidents."""

    # clears the database before seeding anew
    SpeechCollocation.query.delete()
    Collocation.query.delete()
    Speech.query.delete()
    President.query.delete()

    # checks if the president's name is already in the President table. If not, then adds.
    for text in all_speech_info:

        name = ''.join(text['president'])

        db_check = President.query.filter(President.name == name).first()

        if db_check is None:

            president = President(name=name)

            db.session.add(president)

    db.session.commit()


def load_speeches():
    """Seeds database with info on each speech"""

    sentiment_analysis = analyze_speeches()

    for text in all_speech_info:
        link = ''.join(text['url'])
        title = ''.join(text['title'])
        prez = ''.join(text['president'])

        sentiment = sentiment_analysis[title]
        speaker = President.query.filter_by(name=prez).one()
        speech = Speech(title=title, link=link, speaker=speaker.prez_id,
                        sentiment=sentiment)

        db.session.add(speech)

    db.session.commit()


def load_collocations():
    """Seeds database with common bigrams in a table and
    seeds an association table with bigrams and related speeches.
    """

    all_bigrams = top_bigrams()  # { prezname: { speech1: [(phrases) (moarphrases)] } }
    # print all_bigrams
    sentiments = bigram_sentiment()    # {(phrase): 'pos', 'neutral', 'neg'}

    for prez in all_bigrams:  # returns list for each prez
        for p_speech in all_bigrams[prez]:
            current_speech = Speech.query.filter_by(title=p_speech).first()

            for bigram in all_bigrams[prez][p_speech]:
                # print bigram, type(bigram)
                sentiment = sentiments[bigram]

                phrase = Collocation(phrase=' '.join(bigram), sentiment_score=sentiment)

                db.session.add(phrase)

            db.session.commit()

            for bigram in all_bigrams[prez][p_speech]:
                # print bigram, type(bigram)
                new_bigram = Collocation.query.filter_by(phrase=' '.join(bigram)).first()

                current_bigrams = SpeechCollocation(speech_id=current_speech.speech_id,
                                                    phrase_id=new_bigram.phrase_id)

                print current_bigrams

                db.session.add(current_bigrams)

            db.session.commit()

############################
if __name__ == '__main__':
    connect_to_db(app)

    db.create_all()

    load_presidents()
    load_speeches()
    load_collocations()
