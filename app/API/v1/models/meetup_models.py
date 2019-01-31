from datetime import datetime


class Meetup():

    meetup_list = [ {"meetupId": 1,
            "topic": "Javascript",
            "createdon": "Thu, 10 Jan 2019 18:17:59 GMT",
            "host": "Eugine",
            "location": "Mombasa ",
            "happeningon": "5th Jan",
            "summary": "ES6 syntax",
            "tags": "react redux "}]
    rsvps = []

    """
    define all meetup attributes and methods

    """

    def __init__(self, createdon, topic, location, happeningon, tags):
        '''
        initialize class
        '''
        self.meetupId = len(Meetup.meetup_list) + 1
        self.createdon = createdon
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
            "created_on": self.createdon,
            "topic": self.topic,
            "location": self.location,
            "happeningon": self.happeningon,
            "tags": self.tags
        }

        Meetup.meetup_list.append(meetup)
        return meetup, {"message": "Meetup created successfully"}

    def get_meetup(self, meetupId):
        '''
        Method for getting one meetup record
        '''
        meetups = Meetup.meetup_list
        single_meetup = [meetup for meetup in meetups if meetup["meetupId"] == meetupId]
        if single_meetup:
            return single_meetup,{"message":"Meetup found"}
        

    def allMeetups(self):
        '''method for getting all meetup records'''
        return Meetup.meetup_list
    def meetupRsvp(self, userId, meetupId, response):
        '''
        Method for getting rsvp meetup
        '''
        rsvp_data = {
            "rsvpId": str(len(Meetup.rsvps) + 1),
            "meetupId": meetupId,
            "userId": userId,
            "response": response
        }

        Meetup.rsvps.append(rsvp_data)
        return rsvp_data, {"message": "attendance status confirmed"}
