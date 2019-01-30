"""
Tests for meetups operations
"""

import unittest
from app import create_app
import json



class MeetupTest(unittest.TestCase):
    """class representing the meetups test case"""

    def setUp(self):
        '''initialize the app and define test variable'''
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.app_context = self.app

        self.meetup = {
            "meetupId": "1",
            "topic": "Javascript",
            "createdon": "Thu, 10 Jan 2019 18:17:59 GMT",
            "host": "Eugine",
            "location": "Mombasa ",
            "happeningon": "5th Jan",
            "summary": "ES6 syntax",
            "tags": "react redux ",
            
        }
    def test_create_meetup(self):
        '''test the endpoint of creating new meetup'''

        res = self.client.post("/api/v1/meetups/", data=json.dumps(self.meetup),
                               content_type="application/json")
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_data["message"], "meetup created successfully")

            
        