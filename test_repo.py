from flask import Flask
import psycopg2
from unittest.mock import MagicMock, patch
from models import *
from psycopg2 import pool
from repository.event_repository import EventRepository
from repository.feedback_repository import FeedbackRepository

class EventModelTest:
    def __init__(self, description=None, location=None, likes=None, event_date=None):
        self.description = description
        self.location = location
        self.likes = likes
        self.event_date = event_date
        
class FeedbackModelTest:
    def __init__(self, id=-1, event_id=None, content=None, created_at=None):
        self.id = id
        self.event_id = event_id
        self.content = content
        self.created_at = created_at

eventPatch = EventModelTest('description', 'location', 1, 'date')

feedback1 = FeedbackModel(1, 1, 'a timeless classic', 'date')
feedback2 = FeedbackModel(2, 1, 'I hated it', 'date')
feedback3 = FeedbackModel(3, 2, 'an even more timeless classic', 'date')
feedback4 = FeedbackModel(4, 2, 'I hated it even more', 'date')


feedbacks_for_first_event = [feedback1, feedback2]
feedbacks_for_second_event = [feedback3, feedback4]

event1 = EventModel(1, 'test1', 'test1_desc', 'test1_loc', 2, '', 'test1_date',
                    [feedback.__dict__ for feedback in feedbacks_for_first_event])
event2 = EventModel(2, 'test2', 'test2_desc', 'test2_loc', 3, '', 'test2_date',
                    [feedback.__dict__ for feedback in feedbacks_for_second_event])
event3 = EventModel(3, 'test3', 'test3_desc', 'test3_loc', 4, '', 'test3_date')

event_list = [event1, event2, event3]

event_row = [
    (event1.id, event1.title, event1.description, event1.location, event1.likes, event1.image, event1.event_date),
    (event2.id, event2.title, event2.description, event2.location, event2.likes, event2.image, event2.event_date),
    (event3.id, event3.title, event3.description, event3.location, event3.likes, event3.image, event3.event_date)
]

feedback_row = [
    (feedback1.id, feedback1.event_id, feedback1.content, feedback1.created_at),
    (feedback2.id, feedback2.event_id, feedback2.content, feedback2.created_at),
    (feedback3.id, feedback3.event_id, feedback3.content, feedback3.created_at),
    (feedback4.id, feedback4.event_id, feedback4.content, feedback4.created_at)
]

feedback_list = [feedback1, feedback2, feedback3, feedback4]

def test_events_get_all():
    app = Flask(__name__)
    with app.app_context():
        p_mock = MagicMock(spec=psycopg2.pool.SimpleConnectionPool)
        app.config['pSQL_pool'] = p_mock
        conn_mock = MagicMock(spec=psycopg2.extensions.connection)
        cursor_mock = MagicMock()
        p_mock.getconn.return_value = conn_mock
        conn_mock.cursor.return_value = cursor_mock
        cursor_mock.fetchall.return_value = event_row
        cursor_mock.fetchone.return_value = [True]
        repo = EventRepository()
        events = repo.get_events_all()
        assert events[0].title == event1.title
        assert events[1].description == event2.description

def test_events_get_by_id():
    app = Flask(__name__)
    with app.app_context():
        p_mock = MagicMock(spec=psycopg2.pool.SimpleConnectionPool)
        app.config['pSQL_pool'] = p_mock
        conn_mock = MagicMock(spec=psycopg2.extensions.connection)
        cursor_mock = MagicMock()
        p_mock.getconn.return_value = conn_mock
        conn_mock.cursor.return_value = cursor_mock
        cursor_mock.fetchall.return_value = feedback_row
        cursor_mock.fetchone.return_value = event_row[0]
        repo = EventRepository()
        event = repo.get_event_by_id(1)
        assert event.title == event1.title
        assert event.description == event1.description


def test_event_delete():
    app = Flask(__name__)
    with app.app_context():
        p_mock = MagicMock(spec=psycopg2.pool.SimpleConnectionPool)
        app.config['pSQL_pool'] = p_mock
        conn_mock = MagicMock(spec=psycopg2.extensions.connection)
        cursor_mock = MagicMock()
        p_mock.getconn.return_value = conn_mock
        conn_mock.cursor.return_value = cursor_mock
        repo = EventRepository()
        events = repo.delete_event(1)
        assert events == None


def test_update_event():
    app = Flask(__name__)
    with app.app_context():
        p_mock = MagicMock(spec=psycopg2.pool.SimpleConnectionPool)
        app.config['pSQL_pool'] = p_mock
        conn_mock = MagicMock(spec=psycopg2.extensions.connection)
        cursor_mock = MagicMock()
        p_mock.getconn.return_value = conn_mock
        conn_mock.cursor.return_value = cursor_mock
        repo = EventRepository()
        event = repo.update_event(event3.__dict__, 1)
        assert event == None


def test_add_event():
    app = Flask(__name__)
    with app.app_context():
        p_mock = MagicMock(spec=psycopg2.pool.SimpleConnectionPool)
        app.config['pSQL_pool'] = p_mock
        conn_mock = MagicMock(spec=psycopg2.extensions.connection)
        cursor_mock = MagicMock()
        p_mock.getconn.return_value = conn_mock
        conn_mock.cursor.return_value = cursor_mock
        cursor_mock.fetchone.return_value = [3]
        repo = EventRepository()
        event = repo.add_event(event3.__dict__)
        assert event.title == event3.title
        assert event.location == event3.location
        assert event.description == event3.description
        assert event.image == event3.image
        assert event.event_date == event3.event_date
        
def test_modify_event():
    app = Flask(__name__)
    with app.app_context():
        p_mock = MagicMock(spec=psycopg2.pool.SimpleConnectionPool)
        app.config['pSQL_pool'] = p_mock
        conn_mock = MagicMock(spec=psycopg2.extensions.connection)
        cursor_mock = MagicMock()
        p_mock.getconn.return_value = conn_mock
        conn_mock.cursor.return_value = cursor_mock
        cursor_mock.fetchall.return_value = []
        cursor_mock.fetchone.return_value = event_row[0]
        repo = EventRepository()
        event = repo.modify_event(eventPatch.__dict__, event1.id)
        assert event == None
        
def test_feedbacks_get_all():
    app = Flask(__name__)
    with app.app_context():
        p_mock = MagicMock(spec=psycopg2.pool.SimpleConnectionPool)
        app.config['pSQL_pool'] = p_mock
        conn_mock = MagicMock(spec=psycopg2.extensions.connection)
        cursor_mock = MagicMock()
        p_mock.getconn.return_value = conn_mock
        conn_mock.cursor.return_value = cursor_mock
        cursor_mock.fetchall.return_value = feedback_row
        cursor_mock.fetchone.return_value = [True]
        repo = FeedbackRepository()
        feedbacks = repo.get_feedbacks_all(1)
        assert feedbacks[0].content == feedback1.content
        assert feedbacks[1].created_at == feedback2.created_at

def test_feedback_get_by_id():
    app = Flask(__name__)
    with app.app_context():
        p_mock = MagicMock(spec=psycopg2.pool.SimpleConnectionPool)
        app.config['pSQL_pool'] = p_mock
        conn_mock = MagicMock(spec=psycopg2.extensions.connection)
        cursor_mock = MagicMock()
        p_mock.getconn.return_value = conn_mock
        conn_mock.cursor.return_value = cursor_mock
        cursor_mock.fetchone.return_value = feedback_row[0]
        repo = FeedbackRepository()
        feedback = repo.get_feedback_by_id(1)
        assert feedback.content == feedback1.content
        assert feedback.created_at == feedback1.created_at
        
def test_feedback_delete():
    app = Flask(__name__)
    with app.app_context():
        p_mock = MagicMock(spec=psycopg2.pool.SimpleConnectionPool)
        app.config['pSQL_pool'] = p_mock
        conn_mock = MagicMock(spec=psycopg2.extensions.connection)
        cursor_mock = MagicMock()
        p_mock.getconn.return_value = conn_mock
        conn_mock.cursor.return_value = cursor_mock
        repo = FeedbackRepository()
        feedback = repo.delete_feedback(1)
        assert feedback == None

def test_update_feedback():
    app = Flask(__name__)
    with app.app_context():
        p_mock = MagicMock(spec=psycopg2.pool.SimpleConnectionPool)
        app.config['pSQL_pool'] = p_mock
        conn_mock = MagicMock(spec=psycopg2.extensions.connection)
        cursor_mock = MagicMock()
        p_mock.getconn.return_value = conn_mock
        conn_mock.cursor.return_value = cursor_mock
        repo = FeedbackRepository()
        event = repo.update_feedback(feedback3.__dict__, 1)
        assert event == None


def test_add_feedback():
    app = Flask(__name__)
    with app.app_context():
        p_mock = MagicMock(spec=psycopg2.pool.SimpleConnectionPool)
        app.config['pSQL_pool'] = p_mock
        conn_mock = MagicMock(spec=psycopg2.extensions.connection)
        cursor_mock = MagicMock()
        p_mock.getconn.return_value = conn_mock
        conn_mock.cursor.return_value = cursor_mock
        cursor_mock.fetchone.return_value = [3]
        repo = FeedbackRepository()
        feedback = repo.add_feedback(feedback2.__dict__, 1)
        assert feedback.content == feedback2.content
        assert feedback.created_at == feedback2.created_at
        assert feedback.event_id == feedback2.event_id
        
def test_modify_feedback():
    app = Flask(__name__)
    with app.app_context():
        p_mock = MagicMock(spec=psycopg2.pool.SimpleConnectionPool)
        app.config['pSQL_pool'] = p_mock
        conn_mock = MagicMock(spec=psycopg2.extensions.connection)
        cursor_mock = MagicMock()
        p_mock.getconn.return_value = conn_mock
        conn_mock.cursor.return_value = cursor_mock
        cursor_mock.fetchall.return_value = []
        cursor_mock.fetchone.return_value = feedback_row[0]
        repo = FeedbackRepository()
        feedback = repo.modify_feedback(feedback3.__dict__, feedback1.id)
        assert feedback == None
        
def test_check_feedback_existence():
    app = Flask(__name__)
    with app.app_context():
        p_mock = MagicMock(spec=psycopg2.pool.SimpleConnectionPool)
        app.config['pSQL_pool'] = p_mock
        conn_mock = MagicMock(spec=psycopg2.extensions.connection)
        cursor_mock = MagicMock()
        p_mock.getconn.return_value = conn_mock
        conn_mock.cursor.return_value = cursor_mock
        cursor_mock.fetchone.return_value = [False]
        repo = FeedbackRepository()
        feedback = repo.check_feedback_existence(feedback1.id)
        assert feedback == False

def test_check_feedback_existence_by_event_id():
    app = Flask(__name__)
    with app.app_context():
        p_mock = MagicMock(spec=psycopg2.pool.SimpleConnectionPool)
        app.config['pSQL_pool'] = p_mock
        conn_mock = MagicMock(spec=psycopg2.extensions.connection)
        cursor_mock = MagicMock()
        p_mock.getconn.return_value = conn_mock
        conn_mock.cursor.return_value = cursor_mock
        cursor_mock.fetchone.return_value = [False]
        repo = FeedbackRepository()
        feedback = repo.check_feedback_existence_by_event_id(feedback1.id)
        assert feedback == False
        
def test_check_event_existence():
    app = Flask(__name__)
    with app.app_context():
        p_mock = MagicMock(spec=psycopg2.pool.SimpleConnectionPool)
        app.config['pSQL_pool'] = p_mock
        conn_mock = MagicMock(spec=psycopg2.extensions.connection)
        cursor_mock = MagicMock()
        p_mock.getconn.return_value = conn_mock
        conn_mock.cursor.return_value = cursor_mock
        cursor_mock.fetchone.return_value = [False]
        repo = FeedbackRepository()
        feedback = repo.check_event_existence(feedback1.id)
        assert feedback == False
        
        