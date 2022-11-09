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
        return repository.event_add(data)

class Event(Resource):
    
    def __init__(self, repo=repository):
        self.repo = repo
    
    def get(self, event_id):
        return repository.event_get_by_id(event_id).__dict__
    
    def put(self, event_id, req=request):
        data = req.get_json()
        repository.event_update(data, event_id)
        
    def patch(self, event_id, req=request):
        data = req.get_json()
        repository.event_modify(data, event_id)
    
    def delete(self, event_id):
        return repository.event_delete(event_id), 204
        
class FeedbackList(Resource):
    
    def __init__(self, repo=repository):
        self.repo = repo
    
    def get(self, event_id):
        event_id
        return [feedback.__dict__ for feedback in self.repo.feedback_get_all()]
   
    def post(self, event_id, req=request):
        data = req.get_json()
        return repository.feedback_add(data, event_id)
   
class Feedback(Resource):
    
    def __init__(self, repo=repository):
        self.repo = repo
    
    def get(self, feedback_id):
        return repository.feedback_get_by_id(feedback_id).__dict__
    
    def put(self, feedback_id, req=request):
        data = req.get_json()
        repository.feedback_update(data, feedback_id)
        
    def patch(self, feedback_id, req=request):
        data = req.get_json()
        repository.feedback_modify(data, feedback_id)
    
    def delete(self, feedback_id):
        return repository.feedback_delete(feedback_id), 204
    