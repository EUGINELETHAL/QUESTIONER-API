from flask import Flask
from flask import request, jsonify, abort
from .import v1
from app.API.v1.models. meetup_models import meetups


@v1.route('/api/v1/meetups/', methods=["GET"])
def get_all_meetups():
    """
    View all meetups.
    """
    return jsonify({"status":200,'meetup':meetups,"message":"request was successful"})


@v1.route('/api/v1/meetups/<int:id>', methods=['GET'])
def get_meetup(id):
        # retrive a meetup by it's ID
        meetup= [meetup for meetup in meetups if meetup['id'] ==id]
        if len(meetup) == 0:
            return jsonify({'Message': "Meetup not found"})
        return jsonify({"status":200,'meetup':meetup[0],"message":"request was successful"})