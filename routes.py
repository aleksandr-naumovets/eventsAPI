from flask_restful import Resource
from repository.event_repository import EventRepository
from flask import request
from repository.feedback_repository import FeedbackRepository

event_repository = EventRepository()
feedback_repository = FeedbackRepository()

class EventList(Resource):

    def __init__(self, repo=event_repository):
        self.repo = repo

    def get(self):
        return [event.__dict__ for event in self.repo.get_events_all()], 200

    def post(self, req=request):
        data = req.get_json()
        return self.repo.add_event(data).__dict__, 201


class Event(Resource):

    def __init__(self, repo=event_repository):
        self.repo = repo

    def get(self, event_id):
        event = self.repo.get_event_by_id(event_id)
        return event.__dict__ if event else event, 200

    def put(self, event_id, req=request):
        data = req.get_json()
        return self.repo.update_event(data, event_id), 204

    def patch(self, event_id, req=request):
        data = req.get_json()
        return self.repo.modify_event(data, event_id), 200

    def delete(self, event_id):
        return self.repo.delete_event(event_id), 204


class FeedbackList(Resource):

    def __init__(self, repo=feedback_repository):
        self.repo = repo

    def get(self, event_id):
        return [feedback.__dict__ for feedback in self.repo.get_feedbacks_all(event_id)], 200

    def post(self, event_id, req=request):
        data = req.get_json()
        return self.repo.add_feedback(data, event_id).__dict__, 201


class Feedback(Resource):

    def __init__(self, repo=feedback_repository):
        self.repo = repo

    def get(self, feedback_id):
        feedback = self.repo.get_feedback_by_id(feedback_id)
        return feedback.__dict__ if feedback else feedback, 200

    def put(self, feedback_id, req=request):
        data = req.get_json()
        return self.repo.update_feedback(data, feedback_id), 204

    def patch(self, feedback_id, req=request):
        data = req.get_json()
        return self.repo.modify_feedback(data, feedback_id), 200

    def delete(self, feedback_id):
        return self.repo.delete_feedback(feedback_id), 204
