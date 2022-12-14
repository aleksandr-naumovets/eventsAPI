import routes
from models import EventModel, FeedbackModel
from unittest.mock import patch
from unittest import TestCase
from app import app
import json
from dotenv import load_dotenv

BASE_URL = ''

event1 = EventModel(1, 'test1', 'test1_desc', 'test1_loc', 2, '', 'test1_date')
event2 = EventModel(2, 'test2', 'test2_desc', 'test2_loc', 3, '', 'test2_date')
event3 = EventModel(3, 'test3', 'test3_desc', 'test3_loc', 4, '', 'test3_date')

feedback1 = FeedbackModel(1, 1, 'a timeless classic')
feedback2 = FeedbackModel(2, 1, 'I hated it')
feedback3 = FeedbackModel(3, 2, 'an even more timeless classic')
feedback4 = FeedbackModel(4, 2, 'I hated it even more')

class ApiTests(TestCase):

    @patch('routes.EventListAPI.get')
    def test_get_all_events(self, test_patch):
        load_dotenv(".env")
        with app.test_client() as client:
            test_patch.return_value = [event1.__dict__, event2.__dict__, event3.__dict__]
            print(f'{BASE_URL}/events')
            response = client.get(f'{BASE_URL}/events')
            assert response.status_code == 200
            events = json.loads(response.data)
            assert events[0]['id'] == 1

    @patch('routes.EventListAPI.post')
    def test_events_post(self, test_patch):
        load_dotenv(".env")
        with app.test_client() as client:
            test_patch.return_value = 1
            response = client.post(f'{BASE_URL}/events', data={
                "title": "test5",
                "description": "test5_desc",
                "location": "test5_loc",
                "likes": 5,
                "image": [],
                "event_date": "2022-11-07T19:41:59"
            })
            assert response.status_code == 200
            assert test_patch.return_value == 1

    @patch('routes.EventAPI.get')
    def test_get_event_by_id(self, test_patch):
        load_dotenv(".env")
        with app.test_client() as client:
            test_patch.return_value = event1.__dict__
            response = client.get(f'{BASE_URL}/event/1')
            assert response.status_code == 200
            events = json.loads(response.data)
            assert events['id'] == 1

    @patch('routes.EventAPI.put')
    def test_event_put(self, test_patch):
        load_dotenv(".env")
        with app.test_client() as client:
            test_patch.return_value = None
            response = client.put(f'{BASE_URL}/event/1', data={
                "title": "test5",
                "description": "test5_desc",
                "location": "test5_loc",
                "likes": 5,
                "image": [],
                "event_date": "2022-11-07T19:41:59"
            })
            assert response.status_code == 200
            assert test_patch.return_value is None

    @patch('routes.EventAPI.patch')
    def test_event_patch(self, test_patch):
        load_dotenv(".env")
        with app.test_client() as client:
            test_patch.return_value = None
            response = client.patch(f'{BASE_URL}/event/1', data={
                "title": "test5",
                "description": "test5_desc",
                "location": "test5_loc",
                "likes": 5,
                "image": [],
                "event_date": "2022-11-07T19:41:59"
            })
            assert response.status_code == 200
            assert test_patch.return_value is None

    @patch('routes.EventAPI.delete')
    def test_event_delete(self, test_patch):
        load_dotenv(".env")
        with app.test_client() as client:
            test_patch.return_value = None
            response = client.delete(f'{BASE_URL}/event/1')
            assert response.status_code == 200
            assert test_patch.return_value is None

    @patch('routes.FeedbackListAPI.get')
    def test_get_all_feedbacks(self, test_patch):
        load_dotenv(".env")
        with app.test_client() as client:
            test_patch.return_value = [feedback1.__dict__, feedback2.__dict__, feedback3.__dict__, feedback4.__dict__]
            response = client.get(f'{BASE_URL}/feedbacks/1')
            assert response.status_code == 200
            feedbacks = json.loads(response.data)
            assert feedbacks[0]['id'] == 1

    @patch('routes.FeedbackListAPI.post')
    def test_feedbacks_post(self, test_patch):
        load_dotenv(".env")
        with app.test_client() as client:
            test_patch.return_value = 1
            response = client.post(f'{BASE_URL}/feedbacks/1', data={
                "id": 1,
                "event_id": 1,
                "content": "a timeless classic"
            })
            assert response.status_code == 200
            assert test_patch.return_value == 1

    @patch('routes.FeedbackAPI.get')
    def test_get_feedback_by_id(self, test_patch):
        load_dotenv(".env")
        with app.test_client() as client:
            test_patch.return_value = feedback1.__dict__
            response = client.get(f'{BASE_URL}/feedback/1')
            assert response.status_code == 200
            feedback = json.loads(response.data)
            assert feedback['id'] == 1

    @patch('routes.FeedbackAPI.put')
    def test_feedback_put(self, test_patch):
        load_dotenv(".env")
        with app.test_client() as client:
            test_patch.return_value = None
            response = client.put(f'{BASE_URL}/feedback/1', data={
                "id": 1,
                "event_id": 1,
                "content": "a timeless classic"
            })
            assert response.status_code == 200
            assert test_patch.return_value is None

    @patch('routes.FeedbackAPI.patch')
    def test_feedback_patch(self, test_patch):
        load_dotenv(".env")
        with app.test_client() as client:
            test_patch.return_value = None
            response = client.patch(f'{BASE_URL}/feedback/1', data={
                "id": 1,
                "event_id": 1,
                "content": "a timeless classic"
            })
            assert response.status_code == 200
            assert test_patch.return_value is None

    @patch('routes.FeedbackAPI.delete')
    def test_feedback_delete(self, test_patch):
        load_dotenv(".env")
        with app.test_client() as client:
            test_patch.return_value = None
            response = client.delete(f'{BASE_URL}/feedback/1')
            assert response.status_code == 200
            assert test_patch.return_value is None
