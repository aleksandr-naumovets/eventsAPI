from flask_restful import Api
from models import User, orm_db
from routes import EventList, Event, Feedback, FeedbackList
from flask_cors import CORS
from flask import Flask, g, request
from flask_restful import Api
from flask_cors import CORS
from psycopg2 import pool
import os
from flask_sqlalchemy import BaseQuery
from flask_restless import APIManager

BASE_URL = os.environ.get("BASE_URL")
HOST = os.environ.get("HOST")
DATABASE = os.environ.get("DATABASE")
DB_PORT = os.environ.get("DB_PORT")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
MIN = os.environ.get("MIN")
MAX = os.environ.get("MAX")
DEBUG = os.environ.get("DEBUG")

app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@{HOST}:5432/{DATABASE}'
orm_db.init_app(app)
apimanager = APIManager(app, flask_sqlalchemy_db=orm_db)

app.config['pSQL_pool'] = pool.SimpleConnectionPool(MIN,
                                                    MAX,
                                                    user=DB_USER,
                                                    password=DB_PASSWORD,
                                                    host=HOST,
                                                    port=DB_PORT,
                                                    database=DATABASE)

@app.teardown_appcontext
def close_conn(e):
    db = g.pop('db', None)
    if db is not None:
        app.config['pSQL_pool'].putconn(db)
        print('released connection back to pool')

api = Api(app)
CORS(app)
api.add_resource(EventList, f'{BASE_URL}/events')
api.add_resource(Event, f'{BASE_URL}/event/<event_id>')
api.add_resource(FeedbackList, f'{BASE_URL}/feedbacks/<event_id>')
api.add_resource(Feedback, f'{BASE_URL}/feedback/<feedback_id>')
apimanager.create_api(User, methods=['GET'], results_per_page = 10, max_results_per_page=10)

def _limit(self):
    return self.limit()

setattr(BaseQuery, '_limit', _limit)

if __name__ == '__main__':
    app.run(debug=DEBUG)
    
with app.app_context():
    orm_db.create_all()  
