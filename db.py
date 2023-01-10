from pymongo import MongoClient
import os


mongodb_host = os.environ.get('MONGO_HOST', 'mongo')
mongodb_port = int(os.environ.get('MONGO_PORT', '27017'))

client = MongoClient(mongodb_host, mongodb_port, username='root', password='example')

db = client['web_form']
forms = db.forms
