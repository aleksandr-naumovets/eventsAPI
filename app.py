from flask_restful import Api
from models import Image, Participant, Event, Feedback, orm_db
from routes import EventListAPI, EventAPI, FeedbackAPI, FeedbackListAPI
from flask_cors import CORS
from flask import Flask, g
from flask_restful import Api
from flask_cors import CORS
from psycopg2 import pool
import os
from flask_restless import APIManager
from google.cloud import storage
import base64
from codecs import encode


HOST = os.environ.get("HOST")
DATABASE = os.environ.get("DATABASE")
DB_PORT = os.environ.get("DB_PORT")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
MIN = os.environ.get("MIN")
MAX = os.environ.get("MAX")
DEBUG = os.environ.get("DEBUG")
BUCKET_NAME = os.environ.get("BUCKET_NAME")
PROJECT_ID = os.environ.get("PROJECT_ID")

app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@{HOST}:5432/{DATABASE}'
orm_db.init_app(app)
apimanager = APIManager(app, session=orm_db.session)

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
api.add_resource(EventListAPI, f'/events')
api.add_resource(EventAPI, f'/event/<event_id>')
api.add_resource(FeedbackListAPI, f'/feedbacks/<event_id>')
api.add_resource(FeedbackAPI, f'/feedback/<feedback_id>')

if __name__ == '__main__':
    app.run(debug=DEBUG)
    
def save_image(result=None, **kw):
    image = result['data']['attributes']['content']
    filename = result['data']['attributes']['name']
    client = storage.Client(PROJECT_ID)
    bucket = client.get_bucket(BUCKET_NAME)
    blob = bucket.blob(filename)
    decode(image, filename)
    blob.upload_from_filename(f'images/{filename}')
    os.remove(f'images/{filename}')
    
def decode(encodeFile=None, filename=None):
    bytes_img = encode(encodeFile, 'utf-8')
    binary_img = base64.decodebytes(bytes_img)
    with open(f'images/{filename}', "wb") as fh:
        fh.write(binary_img)
    return binary_img
    
    
postprocessors = {'POST_RESOURCE': [save_image]}
    
with app.app_context():
    orm_db.create_all()
    apimanager.create_api(Participant, methods=['GET', 'DELETE', 'PATCH', 'POST'])
    apimanager.create_api(Event, methods=['GET', 'DELETE', 'PATCH', 'POST'])
    apimanager.create_api(Feedback, methods=['GET', 'DELETE', 'PATCH', 'POST'])
    apimanager.create_api(Image, methods=['GET', 'DELETE', 'PATCH', 'POST'], postprocessors=postprocessors)
