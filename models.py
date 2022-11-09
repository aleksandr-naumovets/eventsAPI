from typing import Union

class EventModel:    
    def __init__(self, id=-1, title=None, description=None, location=None, likes=None, image=None, event_date=None):
        self.id = id
        self.title = title
        self.description = description
        self.location = location
        self.likes = likes
        self.image = image
        self.event_date = event_date
        

class FeedbackModel:
    def __init__(self, id=-1, event_id=None, content=None, ):
        self.id = id
        self.event_id = event_id
        self.content = content
