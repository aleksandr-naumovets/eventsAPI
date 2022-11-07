from flask import Flask
from flask_restful import Api
from routes import EventList, Event

BASE_URL = '/api'

app = Flask(__name__)
api = Api(app)

api.add_resource(EventList, f'{BASE_URL}/events')
api.add_resource(Event, f'{BASE_URL}/events/<event_id>')
# api.add_resource(ReviewList, f'{BASE_URL}/Reviews/<book_id>')
# api.add_resource(Review, f'{BASE_URL}/Reviews')

if __name__ == '__main__':
    app.run(debug=True)