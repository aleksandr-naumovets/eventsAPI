from flask_sqlalchemy import SQLAlchemy

orm_db = SQLAlchemy()

class EventModel:
    def __init__(self, id=-1, title=None, description=None, location=None, likes=None, image=None, event_date=None, feedbacks=None):
        self.id = id
        self.title = title
        self.description = description
        self.location = location
        self.likes = likes
        self.image = image
        self.event_date = event_date
        self.feedbacks = feedbacks


class FeedbackModel:
    def __init__(self, id=-1, event_id=None, content=None, created_at=None):
        self.id = id
        self.event_id = event_id
        self.content = content
        self.created_at = created_at


class User(orm_db.Model):
    __tablename__ = 'user'
    
    id = orm_db.Column('id', orm_db.Integer, primary_key = True)
    email = orm_db.Column(orm_db.String(30))
    password = orm_db.Column(orm_db.String(30))
    phone_number = orm_db.Column(orm_db.String(30))
    name = orm_db.Column(orm_db.String(30))  
    surname = orm_db.Column(orm_db.String(30))  
    description = orm_db.Column(orm_db.String(30))
    
    def __init__(self, name=None, surname=None, description=None, events=None, phone_number=None, email=None):
        self.name = name
        self.surname = surname
        self.description = description
        self.events = events
        self.phone_number = phone_number
        self.email = email
        