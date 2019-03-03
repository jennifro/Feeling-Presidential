import os

class AppConfig(object):
    """Configuration for a Flask app and capability to host on Heroku
    """

    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', 'whatevs')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgres:///speeches'
    SQLALCHEMY_TRACK_MODIFICATIONS = False



