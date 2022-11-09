GET_ALL_EVENTS = "SELECT id, title, description, location, likes, image, event_date FROM tbl_events ORDER BY title"
ADD_EVENT = "INSERT INTO tbl_events(title, description, location, likes, image, event_date) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
UPDATE_EVENT = "UPDATE tbl_events SET title = %s, description = %s, location = %s, likes = %s, image = %s, event_date = %s WHERE id = %s"

ADD_FEEDBACK = "INSERT INTO tbl_feedbacks(content, event_id, created_at) VALUES (%s, %s, %s) RETURNING id"
UPDATE_FEEDBACK = "UPDATE tbl_feedbacks SET content = %s, created_at = %s WHERE id = %s"
