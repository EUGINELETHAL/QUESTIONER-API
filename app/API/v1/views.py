from flask import Flask, request, jsonify
from .import v1
from app.API.v1.models.meetup_models import Meetup


@v1.route('/api/v1/meetups/', methods=["POST"])
def post_meetup():
    '''post meetup'''

    meetupdata = request.get_json()
    
    topic = meetupdata('topic')
    location = meetupdata('location')
    happeningon = meetupdata('happeningon')
    createdon = meetupdata('created_on')
    tags = meetupdata('tags')
    
    new_meetup = Meetup(topic, createdon, location, happeningon, tags)
    added_meetup = new_meetup.save_meetup()

    return jsonify({'meetup': added_meetup}), 201


@v1.route('/api/v1/meetups/', methods=["GET"])
def get_meetups():
    
    return jsonify(Meetup.meetup_list)