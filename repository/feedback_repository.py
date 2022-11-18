import json
from models import FeedbackModel
from flask import g, current_app
import sql


class FeedbackRepository:
        
    def get_db(self):
        if 'db' not in g:
            g.db = current_app.config['pSQL_pool'].getconn()
        return g.db
    
    def get_feedbacks_all(self, event_id):
            feedback_list = []
            feedback_flag = self.check_feedback_existence_by_event_id(event_id);
            event_flag = self.check_event_existence(event_id);
            if feedback_flag and event_flag:
                conn = self.get_db()
                if (conn):
                    ps_cursor = conn.cursor()
                    ps_cursor.execute(
                        f"SELECT id, event_id, content, created_at FROM tbl_feedbacks WHERE event_id = {event_id} ORDER BY created_at DESC")
                    feedback_records = ps_cursor.fetchall()
                    for row in feedback_records:
                        feedback_list.append(
                            FeedbackModel(row[0], row[1], row[2], str(row[3])))
                    ps_cursor.close()
            return feedback_list

    def get_feedback_by_id(self, feedback_id):
        feedback = None
        if self.check_feedback_existence(feedback_id):
            conn = self.get_db()
            if (conn):
                ps_cursor = conn.cursor()
                ps_cursor.execute(
                    f"SELECT id, event_id, content, created_at FROM tbl_feedbacks WHERE id = {feedback_id}")
                feedback_record = ps_cursor.fetchone()
                feedback = FeedbackModel(feedback_record[0],
                                         feedback_record[1],
                                         feedback_record[2],
                                         str(feedback_record[3]))
                ps_cursor.close()
        return feedback

    def add_feedback(self, data, event_id):
        conn = self.get_db()
        if (conn):
            ps_cursor = conn.cursor()
            ps_cursor.execute(sql.ADD_FEEDBACK,
                              (data['content'], event_id, data['created_at']))
            conn.commit()
            id = ps_cursor.fetchone()[0]
            ps_cursor.close()
            return FeedbackModel(id, int(event_id), data['content'], data['created_at'])

    def update_feedback(self, data, feedback_id):
        conn = self.get_db()
        if (conn):
            ps_cursor = conn.cursor()
            ps_cursor.execute(sql.UPDATE_FEEDBACK,
                              (data['content'], data['created_at'], feedback_id))
            conn.commit()
            ps_cursor.close()

    def delete_feedback(self, feedback_id):
        conn = self.get_db()
        if (conn):
            ps_cursor = conn.cursor()
            ps_cursor.execute(
                f"DELETE FROM tbl_feedbacks WHERE id = {feedback_id}")
            conn.commit()
            ps_cursor.close()

    def modify_feedback(self, data, feedback_id):
        old: FeedbackModel = self.get_feedback_by_id(feedback_id)
        json_str = str(data).replace("\'", "\"")
        new: FeedbackModel = json.loads(
            json_str, object_hook=lambda d: FeedbackModel(**d))
        updated = FeedbackModel(
            int(feedback_id),
            int(old.event_id),
            new.content if new.content is not None else old.content,
            new.created_at if new.created_at is not None else old.created_at,
        )
        self.update_feedback(updated.__dict__, feedback_id)

    def check_feedback_existence(self, feedback_id):
        conn = self.get_db()
        if (conn):
            ps_cursor = conn.cursor()
            ps_cursor.execute(
                f"SELECT EXISTS(SELECT 1 FROM tbl_feedbacks WHERE id = {feedback_id})")
            feedback_existence_flag = ps_cursor.fetchone()
            ps_cursor.close()
        return feedback_existence_flag[0]

    def check_feedback_existence_by_event_id(self, event_id):
        conn = self.get_db()
        if (conn):
            ps_cursor = conn.cursor()
            ps_cursor.execute(
                f"SELECT EXISTS(SELECT 1 FROM tbl_feedbacks WHERE event_id = {event_id})")
            feedback_existence_flag = ps_cursor.fetchone()
            ps_cursor.close()
        return feedback_existence_flag[0]
    
    def check_event_existence(self, event_id):
        conn = self.get_db()
        if (conn):
            ps_cursor = conn.cursor()
            ps_cursor.execute(
                f"SELECT EXISTS(SELECT 1 FROM tbl_events WHERE id = {event_id})")
            event_existence_flag = ps_cursor.fetchone()
            ps_cursor.close()
        return event_existence_flag[0]
