from models import EventModel

event1 = EventModel('test1', 'test1_id', 'test1_desc', 'test1_loc', 2, '', 'test1_date')
event2 = EventModel('test2', 'test2_id', 'test2_desc', 'test2_loc', 3, '', 'test2_date')

event_list = [event1,event2]
# review1 = ReviewModel('a timeless classic', 1)
# review2 = ReviewModel('I hated it', 1)
# review3 = ReviewModel('an even more timeless classic', 2)
# review4 = ReviewModel('I hated it even more', 2)

class Repository():
    def events_get_all(self):
        return event_list
    
    def event_get_by_id(self, event_id):
        books=event_list
        return next((x for x in event_list if x.id == event_id), None)

    # def reviews_get_by_book_id(self, event_id):
    #     reviews = [review1,review2,review3,review4]
    #     return [x for x in reviews if x.id == event_id]
    
    # def review_add(self, data):
    #     return ReviewModel(data['content'], data['id'], 1)
    
    def event_add(self, data):
        return EventModel(data['title'], data['id'], data['description'],data['location'],data['likes'], data['image'], data['event_date'])
