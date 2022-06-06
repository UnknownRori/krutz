# Initialize flask

from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
limiter = Limiter(app, key_func=get_remote_address)

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200/day", "60/minute"]
)