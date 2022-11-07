from flask_restful import Resource, reqparse
from flask_restful import Resource
from repository import Repository
from flask import request

repo = Repository()

class EventList(Resource):
    def get(self):
       return [event.__dict__ for event in repo.events_get_all()]
   
    def post(self):
        data = request.get_json()
        return repo.event_add(data)

class Event(Resource):
    def get(self, event_id):
        return repo.event_get_by_id(event_id).__dict__
    
    def put(self, event_id):
        data = request.get_json()
        repo.event_update(data, event_id)
        
    def patch(self, event_id):
        data = request.get_json()
        repo.event_modify(data, event_id)
    
    def delete(self, event_id):
        return repo.event_delete(event_id), 204
        
class FeedbackList(Resource):
    def get(self, event_id):
       return [feedback.__dict__ for feedback in repo.feedback_get_all(event_id)]
   
    def post(self, event_id):
        data = request.get_json()
        return repo.feedback_add(data, event_id)
   
    
class Feedback(Resource):
    def get(self, event_id, feedback_id):
        return repo.feedback_get_by_id(event_id, feedback_id).__dict__
    
    def put(self, event_id, feedback_id):
        data = request.get_json()
        repo.feedback_update(data, event_id, feedback_id)
        
    def patch(self, event_id, feedback_id):
        data = request.get_json()
        repo.feedback_modify(data, event_id, feedback_id)
    
    def delete(self, feedback_id):
        return repo.feedback_delete(feedback_id), 204
    