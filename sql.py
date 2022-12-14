GET_ALL_EVENTS = "SELECT id, title, description, location, likes, image, event_datetime FROM events ORDER BY title"
ADD_EVENT = "INSERT INTO events(title, description, location, likes, image, event_datetime) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
UPDATE_EVENT = "UPDATE events SET title = %s, description = %s, location = %s, likes = %s, image = %s, event_datetime = %s WHERE id = %s"

ADD_FEEDBACK = "INSERT INTO feedbacks(content, event_id, created_at) VALUES (%s, %s, %s) RETURNING id"
UPDATE_FEEDBACK = "UPDATE feedbacks SET content = %s, created_at = %s WHERE id = %s"
