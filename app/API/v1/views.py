from flask import Flask, request, jsonify, abort
from .import v1
from app.API.v1.models.meetup_models import Meetup
from app.API.v1.models.questions_model import Question


@v1.route('/api/v1/meetups/', methods=["POST"])
def post_meetup():
    '''post meetup'''

    meetupdata = request.get_json()
    if not meetupdata:
        return jsonify({"status": 400, 
                       "message": "expects only Application/JSON data"}), 400
    
    topic = meetupdata('topic')
    location = meetupdata('location')
    happeningon = meetupdata('happeningon')
    createdon = meetupdata('created_on')
    tags = meetupdata('tags')
    
    new_meetup = Meetup(topic, createdon, location, happeningon, tags)
    added_meetup = new_meetup.save_meetup()

    return jsonify({'meetup': added_meetup, "status": 201, "message":
                    "meetup created  sucessfully"})


@v1.route('/api/v1/meetups/', methods=["GET"])
def get_meetups():
    
    return jsonify(Meetup.meetup_list)


@v1.route('/api/v1/meetups/<meetupId>', methods=["GET"])
def fetch_single_meetup(meetupId):
        """Deals with fetching a single meetup."""
        meetups = Meetup.meetup_list
        single_meetup = [mp for mp in meetups if mp["meeetupId"] == meetupId]
        if single_meetup:
            return single_meetup
        else:
            return "meetup Not Found"


@v1.route('/api/v1/questions/', methods=["POST"])
def post():
        """POST request."""
        if not request.json or not 'title' in request.json:
            abort(400)
        user = request.json["user"]
        meetup = request.json["meetup"]
        title = request.json["title"]
        body = request.json["body"]

        new_question = Question(user, meetup, title, body)
        save_question = new_question.create_question_record()
        return jsonify({'question': save_question}), 201
