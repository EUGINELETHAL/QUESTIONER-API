from flask import Flask
from flask import request, jsonify, abort
from .import v1
from .models import 


@v1.route('api/vi/post_meetup/', methods=["POST"])
def post_meetup(self):
        """
    Method to Posts a new meetup
        responses:
        200:
            description: The request was successful.
        201:
            description: New request created.
        400:
            description: Bad request made.
        401:
            description: Unauthorised access.
        404:
            description: Page not found.
        """
        if 'topic' in request.json and not request.json['topic']:
            return {"message": "topic is required"}, 400

        created On, location,topic = request.json['createdOn'], request.json['location'], request.json['topic']
        post_meetup = {
       'id': question_list[-1]['id'] + 1,
       'createdOn': createdOn
       "location" : location
       "topic" : topic
       "happeningOn" :happeningOn
    }
        meetup.add_meetup(post_meetup)

        return jsonify({'status': 201,
                       "message": "request successfull!"},
                       {"post_meetup":post_meetup),201

                    