from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from routes import EventList, Event
from flask_cors import CORS


BASE_URL = '/api'

app = Flask(__name__)
api = Api(app)
CORS(app)


api.add_resource(EventList, f'{BASE_URL}/events')
api.add_resource(Event, f'{BASE_URL}/events/<event_id>')
# api.add_resource(ReviewList, f'{BASE_URL}/Reviews/<book_id>')
# api.add_resource(Review, f'{BASE_URL}/Reviews')

if __name__ == '__main__':
    app.run(debug=True)