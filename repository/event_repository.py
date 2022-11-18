import json
from models import EventModel, FeedbackModel
from flask import g, current_app
import sql
from repository.feedback_repository import FeedbackRepository

feedback_repository = FeedbackRepository()

class EventRepository:
    
    def __init__(self, repo=feedback_repository):
        self.repo = repo

    def get_db(self):
        if 'db' not in g:
            g.db = current_app.config['pSQL_pool'].getconn()
        return g.db

    def get_events_all(self):
        conn = self.get_db()
        if (conn):
            ps_cursor = conn.cursor()
            ps_cursor.execute(sql.GET_ALL_EVENTS)
            event_records = ps_cursor.fetchall()
            event_list = []
            for row in event_records:
                event_id = str(row[0])
                feedbacks = feedback_repository.get_feedbacks_all(event_id)
                event_list.append(
                    EventModel(event_id, row[1], row[2], row[3], row[4],
                               row[5], str(row[6]),
                               [feedback.__dict__ for feedback in feedbacks]))
            ps_cursor.close()
        return event_list

    def get_event_by_id(self, event_id):
        event = None
        if self.check_event_existence(event_id):
            conn = self.get_db()
            feedbacks = feedback_repository.get_feedbacks_all(event_id)
            if (conn):
                ps_cursor = conn.cursor()
                ps_cursor.execute(
                    f"SELECT id, title, description, location, likes, image, event_date FROM tbl_events WHERE id = {event_id}")
                event_record = ps_cursor.fetchone()
                event = EventModel(event_record[0], event_record[1],
                                   event_record[2], event_record[3],
                                   event_record[4], event_record[5],
                                   str(event_record[6]),
                                   [feedback.__dict__ for feedback in feedbacks])
                ps_cursor.close()
        return event

    def add_event(self, data):
        conn = self.get_db()
        if (conn):
            ps_cursor = conn.cursor()
            ps_cursor.execute(
                sql.ADD_EVENT,
                (data['title'], data['description'], data['location'],
                 data['likes'], data['image'], data['event_date']))
            conn.commit()
            id = ps_cursor.fetchone()[0]
            ps_cursor.close()
        return EventModel(id, data['title'], data['description'],
                          data['location'], data['likes'], data['image'],
                          data['event_date'])

    def update_event(self, data, event_id):
        conn = self.get_db()
        if (conn):
            ps_cursor = conn.cursor()
            ps_cursor.execute(
                sql.UPDATE_EVENT,
                (data['title'], data['description'], data['location'],
                 int(data['likes']), data['image'], data['event_date'],
                 event_id))
            conn.commit()
            ps_cursor.close()

    def delete_event(self, event_id):
        feedbacks = feedback_repository.get_feedbacks_all(event_id)
        for feedback in feedbacks:
            feedback_repository.delete_feedback(feedback.id)
        conn = self.get_db()
        if (conn):
            ps_cursor = conn.cursor()
            ps_cursor.execute(f"DELETE FROM tbl_events WHERE id = {event_id}")
            conn.commit()
            ps_cursor.close()

    def modify_event(self, data, event_id):
        old: EventModel = self.get_event_by_id(event_id)
        json_str = str(data).replace("\'", "\"")
        new: EventModel = json.loads(json_str,
                                     object_hook=lambda d: EventModel(**d))
        updated = EventModel(
            int(event_id),
            new.title if new.title is not None else old.title,
            new.description if new.description is not None else old.description,
            new.location if new.location is not None else old.location,
            new.likes if new.likes is not None else old.likes,
            new.image if new.image is not None else old.image,
            new.event_date if new.event_date is not None else old.event_date)
        self.update_event(updated.__dict__, event_id)

    def check_event_existence(self, event_id):
        conn = self.get_db()
        if (conn):
            ps_cursor = conn.cursor()
            ps_cursor.execute(
                f"SELECT EXISTS(SELECT 1 FROM tbl_events WHERE id = {event_id})")
            event_existence_flag = ps_cursor.fetchone()
            ps_cursor.close()
        return event_existence_flag[0]

    