import json
from datetime import datetime

class Question():
    """Question Model."""
    question_list = []
    
    def __init__(self, createdby, meetup, title, body, votes,createdOn):
        """Question Model class constructor."""
        self.question_id = len(Question.question_list) + 1
        self.createdon = datetime.now()
        self.createdby = createdby
        self.meetup = meetup
        self.title = title
        self.body = body
        self.votes = votes

    def create_question_record(self):
        """Creating Question Record."""
        new_question = {
            "question_id": self.question_id,
            "createdon": datetime.now(),
            "createdby": self.createdby,
            "meetup": self.meetup,
            "title": self.title,
            "body": self.body,
            "votes": self.votes
        }
        Question.question_list.append(new_question)
        return new_question

    
    def upvote_question(self, question_id):
            """Upvote question"""
            questions = Question.question_list
            upvote_question = [question for question in questions if question["id"] == question_id]
            if upvote_question:
                upvote_question[0]["votes"] = upvote_question[0]["votes"] + 1
            return upvote_question

    def downvote_question(self, question_id):
            """Upvote question"""
            questions = Question.question_list
            downvote_question = [question for question in questions if question["id"] == question_id]
            if downvote_question:
                downvote_question[0]["votes"] = downvote_question[0]["votes"] - 1
            return downvote_question
                            
    