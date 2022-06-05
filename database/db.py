# Main Entry point for database

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from app import app

db = SQLAlchemy(app)
ma = Marshmallow(app)

from schema.Url import UrlSchema
from model.Url import Url

db.create_all()