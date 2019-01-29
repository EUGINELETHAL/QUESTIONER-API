import json
from datetime import datetime

class Question():
    """Question Model."""
    question_list = []
    
    def __init__(self, createdby, meetup, title, body, votes,createdOn):
        """Question Model class constructor."""
        # TODO: Link Questions to users to get the user who posted the question
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

    