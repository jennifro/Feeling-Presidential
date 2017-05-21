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


if __name__ == "__main__":
    import unittest

    unittest.main()
