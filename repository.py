import json
from models import EventModel, FeedbackModel

event1 = EventModel(1, 'test1', 'test1_desc', 'test1_loc', 2, '', 'test1_date')
event2 = EventModel(2, 'test2', 'test2_desc', 'test2_loc', 3, '', 'test2_date')
event3 = EventModel(3, 'test3', 'test3_desc', 'test3_loc', 4, '', 'test3_date')

feedback1 = FeedbackModel(1, 1, 'a timeless classic')
feedback2 = FeedbackModel(2, 1, 'I hated it')
feedback3 = FeedbackModel(3, 2, 'an even more timeless classic')
feedback4 = FeedbackModel(4, 2, 'I hated it even more')

event_list = [event1,event2,event3]
feedback_list = [feedback1,feedback2,feedback3,feedback4]

class Repository():
    
    def events_get_all(self):
        return event_list
    
    def event_get_by_id(self, event_id):
        return next((event for event in event_list if event.id == int(event_id)), None)
    
    def event_add(self, data):
        id = len(event_list) + 1
        event_list.append(EventModel(id, data['title'], data['description'],data['location'],data['likes'], data['image'], data['event_date']))
        return id
    
    def event_update(self, data, event_id):
        for event in event_list :
            if (event.id == int(event_id)) :
                event_list[event_list.index(event)] = EventModel(event_id, data['title'], data['description'], data['location'], data['likes'], data['image'], data['event_date'])

    def event_delete(self, event_id):
        event_list.remove(next((current for current in event_list if current.id == int(event_id)), None))

    def event_modify(self, data, event_id):
        json_str = str(data).replace("\'", "\"")
        old: EventModel = json.loads(json_str, object_hook=lambda d: EventModel(**d))
        for event in event_list :
            if (event.id == int(event_id)) :
                event_list[event_list.index(event)] = EventModel(
                    int(event_id), 
                    old.title if old.title else event.title, 
                    old.description if old.description else event.description, 
                    old.location if old.location else event.location, 
                    old.likes if old.likes else event.likes,
                    old.image if old.image else event.image, 
                    old.event_date if old.event_date else event.event_date
                    )          

    def feedback_get_all(self):
        return feedback_list
    
    def feedback_get_by_id(self, feedback_id):
        return next((feedback for feedback in feedback_list if feedback.id == int(feedback_id)), None)
    
    def feedback_add(self, data, event_id):
        id = len(feedback_list) + 1
        feedback_list.append(FeedbackModel(id, int(event_id), data['content']))
        return id
    
    def feedback_update(self, data, feedback_id):
        for feedback in feedback_list :
            if (feedback.id == int(feedback_id)) :
                feedback_list[feedback_list.index(feedback)] = FeedbackModel(int(feedback_id), int(feedback.event_id), data['content'])

    def feedback_delete(self, feedback_id):
        feedback_list.remove(next((feedback for feedback in feedback_list if feedback.id == int(feedback_id)), None))

    def feedback_modify(self, data, feedback_id):
        json_str = str(data).replace("\'", "\"")
        old: FeedbackModel = json.loads(json_str, object_hook=lambda d: FeedbackModel(**d))
        for feedback in feedback_list :
            if (feedback.id == int(feedback_id)) :
                feedback_list[feedback_list.index(feedback)] = FeedbackModel(
                    int(feedback_id),
                    int(feedback.event_id),
                    old.content if old.content else feedback.content, 
                    )
                