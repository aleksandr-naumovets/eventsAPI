from typing import Union

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
