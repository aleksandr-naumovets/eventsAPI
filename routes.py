from flask_restful import Resource, reqparse
from flask_restful import Resource
from repository import Repository
from flask import request
repo = Repository()

class EventList(Resource):
    def get(self):
       return [book.__dict__ for book in repo.events_get_all()]
    
    def post(self):
        data = request.get_json()
        return repo.event_add(data).__dict__

class Event(Resource):
    def get(self, event_id):
        return repo.event_get_by_id(int(event_id)).__dict__

    # def delete(self, event_id):
    #     del TODOS[event_id]
    #     return ''
        
        
# class ReviewList(Resource):
#     def get(self):
#         return {'hello': 'from reviews'}
# class Review(Resource):
#     def get(self):
#         return {'hello': 'from review'}