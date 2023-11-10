from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

DB_URL = "postgresql+psycopg2://postgres:admin@db:5432/parking_db"
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.json.sort_keys = False
app.app_context().push()
db=SQLAlchemy()

db.init_app(app)
