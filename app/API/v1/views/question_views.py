from flask import Flask, request, jsonify, abort
from app.API import v1
from app.API.v1.models.questions_model import Question
from flask import Flask, request, jsonify,Blueprint
questionbp = Blueprint('questionbp', __name__)


@questionbp.route('/api/v1/questions/', methods=["POST"])
def post():
        """POST request."""
        if not request.json or not 'title' in request.json:
            abort(400)
        title = request.json["title"],
        createdby = request.json.get("createdby"),
        meetup = request.json.get("meetup"),
        body = request.json.get("body"),
        votes = request.json.get("votes"),
        createdon = request.json.get("createdon"),

        new_question = Question(createdby, meetup, title, body, votes, createdon)
        save_question = new_question.create_question_record()
        return jsonify(({'question': save_question,"status": 201, "message":
                    "question created  sucessfully"}),201)

@questionbp.route('/questions/<int:question_id>/upvote', methods=["PATCH"])
def upvote_question(question_id):
    '''
    endpoint for upvoting a question
    '''

    vote_up = Question().upvote_question(question_id)

    return jsonify({"status": 400, "data": vote_up}), 400

@questionbp.route('/questions/<int:question_id>/upvote', methods=["PATCH"])
def downvote_question(question_id):
    '''
    endpoint for upvoting a question
    '''

    vote = Question().downvote_question(question_id)

    return jsonify({"status": 400, "data": vote}), 400


   