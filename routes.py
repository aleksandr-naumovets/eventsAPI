from flask_restful import Resource, reqparse
from flask_restful import Resource
from repository import Repository
from flask import request, Request

repository = Repository()

class EventList(Resource):
    
    def __init__(self, repo=repository):
        self.repo = repo
        
    def get(self):
       return [event.__dict__ for event in repository.events_get_all()]
   
    def post(self, req=request):
        print(req)
        data = req.get_json()
        return self.repo.event_add(data)

class Event(Resource):
    
    def __init__(self, repo=repository):
        self.repo = repo
    
    def get(self, event_id):
        return self.repo.event_get_by_id(event_id).__dict__
    
    def put(self, event_id, req=request):
        data = req.get_json()
        self.repo.event_update(data, event_id)
        
    def patch(self, event_id, req=request):
        data = req.get_json()
        self.repo.event_modify(data, event_id)
    
    def delete(self, event_id):
        return self.repo.event_delete(event_id), 204
        
class FeedbackList(Resource):
    
    def __init__(self, repo=repository):
        self.repo = repo
    
    def get(self, event_id):
        event_id
        return [feedback.__dict__ for feedback in self.repo.feedback_get_all()]
   
    def post(self, event_id, req=request):
        data = req.get_json()
        return self.repo.feedback_add(data, event_id)
   
class Feedback(Resource):
    
    def __init__(self, repo=repository):
        self.repo = repo
    
    def get(self, feedback_id):
        return self.repo.feedback_get_by_id(feedback_id).__dict__
    
    def put(self, feedback_id, req=request):
        data = req.get_json()
        self.repo.feedback_update(data, feedback_id)
        
    def patch(self, feedback_id, req=request):
        data = req.get_json()
        self.repo.feedback_modify(data, feedback_id)
    
    def delete(self, feedback_id):
        return self.repo.feedback_delete(feedback_id), 204
    