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

        self.question = {
            "question_id": 1,
            "createdon" : "Thu, 10 Jan 2019 18:17:59 GMT",
            "createdby" : "Eugine",
            "meetup" : "Javascript",
            "title" :  "Javascript",
            "body" : "Javascript",
            "votes" : 0}

            
        
    def test_post_question(self):
        '''test the endpoint of posting new question'''

        res = self.client.post("/api/v1/questions/", data=json.dumps(self.question),
                               content_type="application/json")
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_data["message"], "question created successfully")
