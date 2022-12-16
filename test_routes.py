from repository.feedback_repository import FeedbackRepository
from models import EventModel, FeedbackModel
from routes import *
from repository.event_repository import EventRepository
from unittest.mock import MagicMock
from flask import Request
from app import app
from dotenv import load_dotenv

event1 = EventModel(1, 'test1', 'test1_desc', 'test1_loc', 2, '', 'test1_date')
event2 = EventModel(2, 'test2', 'test2_desc', 'test2_loc', 3, '', 'test2_date')
event3 = EventModel(3, 'test3', 'test3_desc', 'test3_loc', 4, '', 'test3_date')

feedback1 = FeedbackModel(1, 1, 'a timeless classic')
feedback2 = FeedbackModel(2, 1, 'I hated it')
feedback3 = FeedbackModel(3, 2, 'an even more timeless classic')
feedback4 = FeedbackModel(4, 2, 'I hated it even more')

event_list = [event1, event2, event3]
feedback_list = [feedback1, feedback2, feedback3, feedback4]

def test_eventlist_get():
    load_dotenv(".env")
    repo = MagicMock(spec=EventRepository)
    repo.get_events_all.return_value = event_list
    events = EventListAPI(repo).get()[0]
    assert events[0]['id'] == 1
    assert events[1]['title'] == 'test2'


def test_event_post():
    load_dotenv(".env")
    with app.test_request_context():
        repo = MagicMock(spec=EventRepository)
        req = MagicMock(spec=Request)
        data = EventModel(-1, 'tets4_title', 'tets4_desc', 'tets4_loc', 4, [], '2022-11-08T11:12:00')
        req.json.return_value = data.__dict__
        repo.add_event.return_value = event1
        event = EventListAPI(repo).post(req)[0]
        assert event['title'] == event1.title
        assert event['description'] == event1.description
        assert event['location'] == event1.location
        assert event['likes'] == event1.likes
        assert event['image'] == event1.image
        assert event['event_datetime'] == event1.event_datetime
        assert event['feedbacks'] == None


def test_event_get():
    load_dotenv(".env")
    repo = MagicMock(spec=EventRepository)
    repo.get_event_by_id.return_value = event1
    event = EventAPI(repo).get(1)[0]
    assert event['id'] == 1
    assert event['title'] == 'test1'


def test_event_put():
    load_dotenv(".env")
    with app.test_request_context():
        repo = MagicMock(spec=EventRepository)
        req = MagicMock(spec=Request)
        data = EventModel(-1, 'tets5_title', 'tets5_desc', 'tets5_loc', 4, [], '2022-11-08T12:12:00')
        req.json.return_value = data.__dict__
        repo.update_event.return_value = None
        event = EventAPI(repo).put(1, req)[0]
        assert event == None


def test_event_patch():
    load_dotenv(".env")
    with app.test_request_context():
        repo = MagicMock(spec=EventRepository)
        req = MagicMock(spec=Request)
        data = EventModel(-1, 'tets6_title', 'tets6_desc', 'tets6_loc', 4, [], '2022-11-08T11:12:00')
        req.json.return_value = data.__dict__
        repo.modify_event.return_value = None
        event = EventAPI(repo).patch(1, req)[0]
        assert event == None


def test_event_delete():
    load_dotenv(".env")
    with app.test_request_context():
        repo = MagicMock(spec=EventRepository)
        repo.delete_event.return_value = None
        event = EventAPI(repo).delete(1)
        assert event == (None, 204)


def test_feedbacklist_get():
    load_dotenv(".env")
    repo = MagicMock(spec=FeedbackRepository)
    repo.get_feedbacks_all.return_value = feedback_list
    feedback = FeedbackListAPI(repo).get(1)[0]
    assert feedback[0]['id'] == 1
    assert feedback[1]['content'] == 'I hated it'


def test_feedback_post():
    load_dotenv(".env")
    with app.test_request_context():
        repo = MagicMock(spec=FeedbackRepository)
        req = MagicMock(spec=Request)
        data = FeedbackModel(-1, 2, 'test7')
        req.json.return_value = data.__dict__
        repo.add_feedback.return_value = data
        feedback = FeedbackListAPI(repo).post(2, req)[0]
        assert feedback['event_id'] == data.event_id
        assert feedback['content'] == data.content
        assert feedback['created_at'] == data.created_at


def test_feedback_get():
    load_dotenv(".env")
    repo = MagicMock(spec=FeedbackRepository)
    repo.get_feedback_by_id.return_value = feedback1
    feedback = FeedbackAPI(repo).get(1)[0]
    assert feedback['id'] == 1
    assert feedback['content'] == 'a timeless classic'


def test_feedback_put():
    load_dotenv(".env")
    with app.test_request_context():
        repo = MagicMock(spec=FeedbackRepository)
        req = MagicMock(spec=Request)
        data = FeedbackModel(-1, 2, 'I hated it even more test6')
        req.json.return_value = data.__dict__
        repo.update_feedback.return_value = None
        event = FeedbackAPI(repo).put(1, req)[0]
        assert event == None


def test_feedback_patch():
    load_dotenv(".env")
    with app.test_request_context():
        repo = MagicMock(spec=FeedbackRepository)
        req = MagicMock(spec=Request)
        string = MagicMock(str=Request)
        j_s_o_n = MagicMock(json=Request)
        data = FeedbackModel(-1, 2, 'I hated it even more test7')
        j_s_o_n.loads.return_value = data
        string.replace.return_value = "{'id':-1, 'event_id':2, 'content':'I hated it even more test7'}"
        req.json.return_value = "{'id':-1, 'event_id':2, 'content':'I hated it even more test7'}"
        repo.modify_feedback.return_value = None
        event = FeedbackAPI(repo).patch(1, req)[0]
        assert event == None


def test_feedback_delete():
    load_dotenv(".env")
    with app.test_request_context():
        repo = MagicMock(spec=FeedbackRepository)
        repo.delete_feedback.return_value = None
        event = FeedbackAPI(repo).delete(2)
        assert event == (None, 204)
