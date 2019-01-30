from flask import Flask, request, jsonify,Blueprint,make_response
from app.API.v1.models.meetup_models import Meetup
meetupbp = Blueprint('meetupbp', __name__)


@meetupbp.route('/api/v1/meetups/', methods=["POST"])
def post_meetup():
    '''post meetup'''

    meetupdata = request.get_json()
    if not meetupdata:
        return jsonify({"status": 400, 
                       "message": "expects only Application/JSON data"}), 400
    
    topic = meetupdata['topic'],
    location = meetupdata['location'],
    happeningon = meetupdata['happeningon'],
    createdon = meetupdata['createdon'],
    tags = meetupdata['tags'] 
    new_meetup = Meetup(topic, createdon, location, happeningon, tags)
    added_meetup = new_meetup.save_meetup()

    return jsonify({'meetup': added_meetup, "status": 201, "message":
                    "meetup created successfully"})
    

@meetupbp.route('/api/v1/meetups/', methods=["GET"])
def get_meetups():
    meetups = Meetup.meetup_list
    return make_response(jsonify({"meetups":meetups, "status":200, "message":"success"}),200)



@meetupbp.route('/api/v1/meetups/<meetupId>', methods=["GET"])
def fetch_single_meetup(meetupId):
        """Deals with fetching a single meetup."""
        meetups = Meetup.meetup_list
        single_meetup = [mp for mp in meetups if mp["meeetupId"] == meetupId]
        if single_meetup:
            return single_meetup
        else:
            return "meetup Not Found"
