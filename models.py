class EventModel:
    def __init__(self, title, id=-1, description='', location='', likes=0, image='', event_date='1900-01-01'):
        self.title = title
        self.id = id
        self.description = description
        self.location = location
        self.likes = likes
        self.image = image
        self.event_date = event_date

# class ReviewModel:
#     def __init__(self, content, bookId, id=-1):
#         self.content = content
#         self.bookId = bookId
#         self.id = id