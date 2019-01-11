from flask import Flask
from flask import request, jsonify, abort
from .import v1
from app.API.v1.models.meetup_models import Meetup

@v1.route('/api/v1/')