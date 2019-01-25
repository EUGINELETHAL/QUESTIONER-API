from flask import Flask, request, jsonify
from .import v1
from app.API.v1.models import meetup_models



@v1.route('/api/v1/meetups/', methods=["POST"])
def post_meetup():
    '''post meetup'''

    meetupdata = request.get_json()
    if not meetupdata:
        return jsonify({"status": 400, "message": "expects only Application/JSON data"}), 400

    topic = meetupdata.get('topic')
    location = meetupdata.get('location')
    happeningon = meetupdata.get('happeningon')
    createdon = meetupdata.get('created_on')
    tags = meetupdata.get('tags')
    
    new_meetup = meetup_models.Meetup(topic, createdon, location, happeningon, tags).save_meetup()
    return jsonify({'meetup': new_meetup}), 201



   