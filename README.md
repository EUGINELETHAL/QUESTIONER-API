# QUESTIONER-API
Questioner web app, is an online platform that crowd-sources questions from users about meetups.it is an api that utilizes object oriented techniques and data structures.

## API ENDPOINTS
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/470df32a30646e961eb9)
#### Question Endpoints.
| API Endpoint  | Description | Methods |
| ------------- | ------------- | ------------- |
| /api/v1/questions  | Create a question for a specific meetup  | POST  |
| /api/v1/questions  | Get all questions for a specific meetup  | GET  |
| /api/v1/questions/question-id | Get a specific question  | GET  |
| /api/v1//questions/question-id/upvote  | Upvote a specific question.  | PATCH  |
|/api/v1/questions/question-id/downvote  | Downvote a specific question. | PATCH |

#### Meetup Endpoints
| API Endpoint  | Description | Methods |
| ------------- | ------------- | ------------- |
| /api/v1/meetups  | Get all meetups  | GET  |
| /api/v1/meetups  | Create a meetup  | POST  |
|/api/v1/meetups/meetup-id | Get a specific meetup record  | GET  |
|/api/v1/meetups/meetup-id/rsvps  | Respond to meetup RSVP  | POST  |

## Getting Started
To get started:
 Git clone the repository using https://github.com/EUGINELETHAL/QUESTIONER-API.git
 For the API to run smoothly you will need the following:
```
1. Python 3.4 or higher installed.
2. Pip3
3. Pipenv or virtualenv installed.
```
### Installing
> __Installation Guide.__

1. Git clone the repository using 
2. Through your terminal, navigate to the location with the cloned repository.
3. Open the cloned repo folder using your terminal.
4. You're currently on the `develop` branch.
5. Set up a virtual environment:
    > Using virtualenv: `virtualenv -p python3 env`
    > Using pipenv: `pipenv shell`
6. To activate the virtual environment:
    > Using virtualenv: `source env/bin/activate`
    > Using pipenv: `not necessary`(since it automatically activates itself after creation)
7. Install the packages:
    > Using virtualenv: `pip3 install -r requirements.txt`
    > Using pipenv: `pipenv install`
8. There is already a `.env` file containing all the necessary environment variables.
9. Export all the environment variables by running `source .env`.
10. To launch your app now, use `flask run`.

## Running the tests
To view all the unit tests, from your root directory of the project (Inside cloned repository folder), run `pytest --cov=app`

### Style Guide.
PEP 8

## Deployment


## Built With
* [Flask](http://flask.pocoo.org/docs/1.0/) - The web framework used

## Authors
* **Ochung Eugine.** 
