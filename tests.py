from server import app
from unittest import TestCase
from model import connect_to_db, db, test_data, President, Speech, Collocation, SpeechCollocation
import server
import json


class FlaskTestRoutes(TestCase):
    """docstring for FlaskTestRoutes"""

    def setUp(self):
        self.client = app.test_client()

        app.config['TESTING'] = True

    def test_index(self):
        result = self.client.get('/')
        self.assertIn('phrases', result.data)

    def test_timeline(self):
        result = self.client.get('/timeline')
        self.assertIn('Overall', result.data)


class FlaskTestDB(TestCase):
    """docstring for FlaskTestsDB"""

    def setUp(self):
        self.client = app.test_client()

        app.config['TESTING'] = True

        connect_to_db(app, 'postgresql:///testdb')

        db.create_all()
        test_data()

    def tearDown(self):
        db.session.close()
        db.drop_all()

    def test_d3_data(self):
        result = self.client.get('/data.json')
        self.assertEqual(result.status_code, 200)
        self.assertIn("""'source': 'State of the Union (January 7, 2020)'""", result.data)



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

    
if __name__ == "__main__":
    import unittest

    unittest.main()
