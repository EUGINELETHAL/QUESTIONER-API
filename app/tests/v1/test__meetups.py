"""
Tests for meetups operations
"""

import unittest
import json
from app import create_app


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
            "created_on": "Thu, 10 Jan 2019 18:17:59 GMT",
            "host": "Eugine",
            "location": "Mombasa ",
            "happening on": "5th Jan",
            "summary": "ES6 syntax",
            "tags": "react redux ",
            
        }
