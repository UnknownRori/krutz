from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import string
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    raw = db.Column(db.String, nullable=False)
    short = db.Column(db.String, unique=True, nullable=False)
# TODO move this class to separate file

db.create_all()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['post'])
def store_url():
    raw = request.json['url']
    short = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    # TODO do some validation
    # TODO and add error handler
    url = Url(raw=raw, short=short)
    db.session.add(url)
    db.session.commit()

    return {
        "message": "Successfully shortened url",
        "result": "/" + url.short
    }


@app.route('/<short>')
def show_url(short):
    url = Url.query.filter_by(short=short).first()

    if(url is None):
        return render_template('404.html'), 404

    return redirect(url.raw)
