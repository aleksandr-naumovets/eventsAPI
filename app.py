from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from routes import EventList, Event, Feedback, FeedbackList
from flask_cors import CORS

BASE_URL = '/api'

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(EventList, f'{BASE_URL}/events')
api.add_resource(Event, f'{BASE_URL}/event/<event_id>')
api.add_resource(FeedbackList, f'{BASE_URL}/feedbacks/<event_id>')
api.add_resource(Feedback, f'{BASE_URL}/feedback/<feedback_id>')

if __name__ == '__main__':
    app.run(debug=True)
    