from flask_sqlalchemy import SQLAlchemy

orm_db = SQLAlchemy()

class EventModel:
    def __init__(self, id=-1, title=None, description=None, location=None, likes=None, image=None, event_datetime=None, feedbacks=None):
        self.id = id
        self.title = title
        self.description = description
        self.location = location
        self.likes = likes
        self.image = image
        self.event_datetime = event_datetime
        self.feedbacks = feedbacks


class FeedbackModel:
    def __init__(self, id=-1, event_id=None, content=None, created_at=None):
        self.id = id
        self.event_id = event_id
        self.content = content
        self.created_at = created_at
        

class Feedback(orm_db.Model):
    __tablename__ = 'feedbacks'
    
    id = orm_db.Column('id', orm_db.Integer, primary_key = True)
    event_id = orm_db.Column(orm_db.Integer, orm_db.ForeignKey('events.id'))
    content = orm_db.Column(orm_db.String(30))
    img = orm_db.relationship('Image', backref='feedback', lazy=True)
    images = orm_db.Column(orm_db.ARRAY(orm_db.String))
    created_at = orm_db.Column(orm_db.DateTime)
    
    def __init__(self, event_id=None, content=None, created_at=None, img=[]):
        self.event_id = event_id
        self.content = content
        self.created_at = created_at
        self.img = img
        
class Event(orm_db.Model):
    __tablename__ = 'events'
    
    id = orm_db.Column('id', orm_db.Integer, primary_key = True)
    title = orm_db.Column(orm_db.String(30))
    description = orm_db.Column(orm_db.String(30))
    location = orm_db.Column(orm_db.String(30))
    likes = orm_db.Column(orm_db.Integer)
    img = orm_db.relationship('Image', backref='event', lazy=True)
    images = orm_db.Column(orm_db.ARRAY(orm_db.String))
    event_datetime = orm_db.Column(orm_db.DateTime)
    feedbacks = orm_db.relationship('Feedback', backref='event', lazy=True)
    
    def __init__(self, title=None, description=None, location=None, likes=None, img=[], event_datetime=None, feedbacks=[]):
        self.title = title
        self.description = description
        self.location = location
        self.likes = likes
        self.img = img
        self.event_datetime = event_datetime
        self.feedbacks = feedbacks
        
events_participants = orm_db.Table('events_participants',
    orm_db.Column('event_id', orm_db.Integer, orm_db.ForeignKey('events.id'), primary_key=True),
    orm_db.Column('participant_id', orm_db.Integer, orm_db.ForeignKey('participants.id'), primary_key=True)
)

class Participant(orm_db.Model):
    __tablename__ = 'participants'
    
    id = orm_db.Column('id', orm_db.Integer, primary_key = True)
    email = orm_db.Column(orm_db.String(30))
    phone_number = orm_db.Column(orm_db.String(30))
    name = orm_db.Column(orm_db.String(30))  
    surname = orm_db.Column(orm_db.String(30))  
    description = orm_db.Column(orm_db.String(30))
    username = orm_db.Column(orm_db.String(30))
    images = orm_db.Column(orm_db.ARRAY(orm_db.String))
    img = orm_db.relationship('Image', backref='participant', lazy=True)
    events = orm_db.relationship('Event', secondary=events_participants, lazy='subquery',
        backref=orm_db.backref('participants', lazy=True))
    
    def __init__(self, name=None, surname=None, description=None, events=[], phone_number=None, email=None, username=None, img=[]):
        self.name = name
        self.surname = surname
        self.description = description
        self.events = events
        self.phone_number = phone_number
        self.email = email
        self.username = username
        self.img = img

class Image(orm_db.Model):
    __tablename__ = 'images'
    id = orm_db.Column('id', orm_db.Integer, primary_key = True)
    event_id = orm_db.Column(orm_db.Integer, orm_db.ForeignKey('events.id'))
    participant_id = orm_db.Column(orm_db.Integer, orm_db.ForeignKey('participants.id'))
    feedback_id = orm_db.Column(orm_db.Integer, orm_db.ForeignKey('feedbacks.id'))
    name = orm_db.Column(orm_db.String(30))  
    content = orm_db.Column(orm_db.String(30))
    
    def __init__(self, name=None, content=None, event_id=None, participant_id=None, feedback_id=None):
        self.event_id = event_id
        self.participant_id = participant_id
        self.feedback_id = feedback_id
        self.name = name
        self.content = content
    