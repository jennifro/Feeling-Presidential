from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import speechinfo

app = Flask(__name__)

db = SQLAlchemy()

DB_URI = 'postgresql:///speeches'


class President(db.Model):
    """docstring for President"""

    __tablename__ = 'presidents'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    start_yr = db.Column(db.Integer, nullable=False)
    end_yr = db.Column(db.Integer, nullable=False)

    speech = db.relationship('Speech')

    def __repr__(self):
        return '<ID={}, Name={}>'.format(self.id, self.name)


class Speech(db.Model):
    """docstring for Speeches"""

    __tablename__ = 'speeches'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), db.ForeignKey('speech_types.speech_type'))
    speaker = db.Column(db.String(50), db.ForeignKey('presidents.name'))
    link = db.Column(db.String(100), nullable=True)

    prez = db.relationship('President')

    speechtype = db.relationship('SpeechTypes')

    connect = db.relationship('Connection')

    def __repr__(self):
        return '<ID={}, Title: {}, President: {}>'.format(self.id, self.title, self.speaker)


class SpeechTypes(db.Model):
    """docstring for SpeechType"""

    __tablename__ = 'speech_types'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    speech_type = db.Column(db.String(100), nullable=False)

    speeches = db.relationship('Speech')


class Collocation(db.Model):
    """docstring for Collocations"""

    __tablename__ = 'collocations'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phrase = db.Column(db.String(75), nullable=False)

    connect = db.relationship('Connection')


class Connection(db.Model):
    """docstring for Connection"""

    __tablename__ = 'connections'

    connect_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    speech_id = db.Column(db.Integer, db.ForeignKey('speeches.id'))
    phrase_id = db.Column(db.Integer, db.ForeignKey('collocations.id'))

    speech = db.relationship('Speech')
    phrase = db.relationship('Collocation')
