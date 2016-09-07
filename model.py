from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()

# DB_URI = 'postgresql:///speeches'

## TODO: FIGURE OUT AUTOINCREMENT RESET


class President(db.Model):
    """docstring for President"""

    __tablename__ = 'presidents'

    prez_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    speech = db.relationship('Speech')

    def __repr__(self):
        return '<ID={}, Name={}>'.format(self.prez_id, self.name)

    # POST MVP:
    # start_yr = db.Column(db.Integer, nullable=False)
    # end_yr = db.Column(db.Integer, nullable=False)


class Speech(db.Model):
    """docstring for Speech"""

    __tablename__ = 'speeches'

    speech_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))       # db.ForeignKey('speech_types.speech_type')
    speaker = db.Column(db.Integer, db.ForeignKey('presidents.prez_id'))
    link = db.Column(db.String(100), nullable=True)
    sentiment = db.Column(db.String(25))

    prez = db.relationship('President')

    speech_phrases = db.relationship('SpeechCollocation')

    def __repr__(self):
        return '<ID={}, Title: {}, President: {}, Sentiment: {}>'.format(self.speech_id,
                                                                         self.title, self.speaker, self.sentiment)


class Collocation(db.Model):
    """docstring for Collocations"""

    __tablename__ = 'collocations'

    phrase_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phrase = db.Column(db.String(75), nullable=False)
    sentiment_score = db.Column(db.String(25))

    connect = db.relationship('SpeechCollocation')

    def __repr__(self):
        return '<ID={}, Phrase={}>'.format(self.phrase_id, self.phrase)


class SpeechCollocation(db.Model):
    """docstring for SpeechCollocation"""

    __tablename__ = 'SpeechCollocations'

    connect_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    speech_id = db.Column(db.Integer, db.ForeignKey('speeches.speech_id'))
    phrase_id = db.Column(db.Integer, db.ForeignKey('collocations.phrase_id'))

    speech = db.relationship('Speech')
    phrase = db.relationship('Collocation')

    def __repr__(self):
        return '<ID={}, Speech ID={}, Phrase ID={}>'.format(self.connect_id, self.speech_id, self.phrase_id)


def connect_to_db(app, db_uri='postgresql:///speeches'):
    """Connect database to Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def test_data():
    """Create sample data for testing."""

    President.query.delete()
    Speech.query.delete()
    Collocation.query.delete()
    SpeechCollocation.query.delete()

    p1 = President(name='Kanye West')
    p2 = President(name='Beyonce Knowles')
    p3 = President(name='Janelle Monae')

    s1 = Speech(title='State of the Union (January 7, 2020)', sentiment='pos',
                speaker=p1.prez_id)
    s2 = Speech(title='State of the Union (January 25, 2024)', sentiment='neg',
                speaker=p2.prez_id)
    s3 = Speech(title='State of the Union (January 10, 2028)', sentiment='pos',
                speaker=p3.prez_id)

    c1 = Collocation(phrase='climb spaceship', sentiment_score='negative')
    c2 = Collocation(phrase='formation coordination', sentiment_score='neutral')
    c3 = Collocation(phrase='electric lady', sentiment_score='positive')

    sc1 = SpeechCollocation(phrase_id=c1.phrase_id, speech_id=s1.speech_id)
    sc2 = SpeechCollocation(phrase_id=c2.phrase_id, speech_id=s2.speech_id)
    sc3 = SpeechCollocation(phrase_id=c3.phrase_id, speech_id=s3.speech_id)

    db.session.add_all([p1, p2, p3, s1, s2, s3, c1, c2, c3, sc1, sc2, sc3])
    db.session.commit()

#################

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    print 'Connected to DB!'
