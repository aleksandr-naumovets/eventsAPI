import json
from models import EventModel, FeedbackModel
from routes import *
from repository import Repository
from unittest.mock import MagicMock, Mock
from flask import Request
from app import app

event1 = EventModel(1, 'test1', 'test1_desc', 'test1_loc', 2, '', 'test1_date')
event2 = EventModel(2, 'test2', 'test2_desc', 'test2_loc', 3, '', 'test2_date')
event3 = EventModel(3, 'test3', 'test3_desc', 'test3_loc', 4, '', 'test3_date')

feedback1 = FeedbackModel(1, 1, 'a timeless classic')
feedback2 = FeedbackModel(2, 1, 'I hated it')
feedback3 = FeedbackModel(3, 2, 'an even more timeless classic')
feedback4 = FeedbackModel(4, 2, 'I hated it even more')

event_list = [event1,event2,event3]
feedback_list = [feedback1,feedback2,feedback3,feedback4]

def test_eventlist_get():
    repo = MagicMock(spec=Repository)
    repo.events_get_all.return_value = event_list
    events = EventList(repo).get()
    assert events[0]['id'] == 1
    assert events[1]['title'] == 'test2'

def test_event_post():
    with app.test_request_context():
        repo = MagicMock(spec=Repository)
        req = MagicMock(spec=Request)
        data = EventModel(-1, 'tets4_title', 'tets4_desc', 'tets4_loc', 4, [], '2022-11-08T11:12:00')
        req.json.return_value = data.__dict__
        repo.event_add.return_value = 4
        event = EventList(repo).post(req)
        assert event == 4
        
def test_event_get():
    repo = MagicMock(spec=Repository)
    repo.event_get_by_id.return_value = event1
    event = Event(repo).get(1)
    assert event['id'] == 1
    assert event['title'] == 'test1'
        
def test_event_put():
    with app.test_request_context():
        repo = MagicMock(spec=Repository)
        req = MagicMock(spec=Request)
        data = EventModel(-1, 'tets5_title', 'tets5_desc', 'tets5_loc', 4, [], '2022-11-08T12:12:00')
        req.json.return_value = data.__dict__
        repo.event_update.return_value = None
        event = Event(repo).put(1, req)
        assert event == None

# TODO FIX TEST FOR PATCH EVENT
def test_event_patch():
    with app.test_request_context():
        repo = MagicMock(spec=Repository)
        req = MagicMock(spec=Request)
        data = EventModel(-1, 'tets6_title', 'tets6_desc', 'tets6_loc', 4, [], '2022-11-08T11:12:00')
        req.json.return_value = data.__dict__
        repo.event_modify.return_value = None
        event = Event(repo).patch(1, req)
        assert event == None
        
def test_event_delete():
    with app.test_request_context():
        repo = MagicMock(spec=Repository)
        repo.event_delete.return_value = None
        event = Event(repo).delete(1)
        assert event == (None, 204)

def test_feedbacklist_get():
    repo = MagicMock(spec=Repository)
    repo.feedback_get_all.return_value = feedback_list
    feedback = FeedbackList(repo).get(1)
    assert feedback[0]['id'] == 1
    assert feedback[1]['content'] == 'I hated it'

def test_feedback_post():
    with app.test_request_context():
        repo = MagicMock(spec=Repository)
        req = MagicMock(spec=Request)
        data = FeedbackModel(-1, 2, 'test7')
        req.json.return_value = data.__dict__
        repo.feedback_add.return_value = 4
        event = FeedbackList(repo).post(2, req)
        assert event == 4

def test_feedback_get():
    repo = MagicMock(spec=Repository)
    repo.feedback_get_by_id.return_value = feedback1
    feedback = Feedback(repo).get(1)
    assert feedback['id'] == 1
    assert feedback['content'] == 'a timeless classic'

def test_feedback_put():
    with app.test_request_context():
        repo = MagicMock(spec=Repository)
        req = MagicMock(spec=Request)
        data = FeedbackModel(-1, 2, 'I hated it even more test6')
        req.json.return_value = data.__dict__
        repo.feedback_update.return_value = None
        event = Feedback(repo).put(1, req)
        assert event == None

# TODO FIX TEST FOR PATCH FEEDBACK
def test_feedback_patch():
    with app.test_request_context():
        repo = MagicMock(spec=Repository)
        req = MagicMock(spec=Request)
        string = MagicMock(str=Request)
        j_s_o_n = MagicMock(json=Request)
        data = FeedbackModel(-1, 2, 'I hated it even more test7')
        j_s_o_n.loads.return_value = data
        string.replace.return_value = "{'id':-1, 'event_id':2, 'content':'I hated it even more test7'}"
        req.json.return_value = "{'id':-1, 'event_id':2, 'content':'I hated it even more test7'}"
        repo.feedback_modify.return_value = None
        event = Feedback(repo).patch(1, req)
        assert event == None

def test_feedback_delete():
    with app.test_request_context():
        repo = MagicMock(spec=Repository)
        repo.feedback_delete.return_value = None
        event = Feedback(repo).delete(2)
        assert event == (None, 204)
