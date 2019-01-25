from datetime import datetime

meetup_list = [
        
]


class Meetup():
    """
    define all meetup attributes and methods
    """

    def __init__(self, createdon, topic, location, happeningon, tags):
        '''
        initialize class
        '''
        self.meetupId = str(len(meetup_list) + 1)
        self.created_on = datetime.now()
        self.topic = topic
        self.location = location
        self.happeningon = happeningon
        self.tags = tags
       
    def save_meetup(self):
        '''
        Method for creating a new meetup record
        '''

        meetup = {
            "meetupId": self.meetupId,
            "created_on": self.created_on,
            "topic": self.topic,
            "location": self.location,
            "tags": self.tags
        }

        meetup_list.append(meetup)
        return meetup, {"message": "Meetup created successfully"}

    def get_meetup(self, meetupId):
        '''
        Method for getting one meetup record
        '''
        for meetup in meetup_list:
            if meetup['meetupId'] == meetupId:
                return meetup, {"message": "success"}

    def allMeetups(self):
        '''method for getting all meetup records'''
        return meetup_list
