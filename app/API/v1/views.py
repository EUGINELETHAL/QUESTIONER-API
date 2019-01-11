from flask import Flask
from flask import request, jsonify, abort
from .import v1
from app.API.v1.models. meetup_models import meetup



@v1.route('/api/vi/meetups/', methods=["GET"])
def get_all_meetups():
    """
    View all meetups.
    """
    return jsonify({"status":200,'meetup':meetup,"message":"request was successful"})
