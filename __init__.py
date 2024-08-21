from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config.from_object('config.config.Config')

db = SQLAlchemy(app)

from middleware.request_middleware import before_request_func, after_request_func
app.before_request(before_request_func)
app.after_request(after_request_func)

from routes import user_routes
app.register_blueprint(user_routes.bp)

with app.app_context():
    db.create_all()