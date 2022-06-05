from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields
import string
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Url(db.Model):
    # TODO move this class to separate file
    id = db.Column(db.Integer, primary_key=True)
    raw = db.Column(db.String, nullable=False)
    short = db.Column(db.String, unique=True, nullable=False)


class UrlSchema(ma.Schema):
    # TODO move this class to separate file
    url = fields.Url(required=True)

db.create_all()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['post'])
def store_url():
    errors = UrlSchema().validate(request.json)

    if errors:
        return {
            'message': 'Failed to shorten url',
            'errors': errors
        }, 400

    raw = request.json['url']
    short = ''.join(
        random.choices(string.ascii_letters + string.digits, k=6)
    )

    try:
        url = Url(raw=raw, short=short)
        db.session.add(url)
        db.session.commit()

        return {
            "message": "Successfully shortened url",
            "result": "/" + url.short
        }
    except Exception as e:
        return {
            "message": "Failed to shorten url",
            "errors": "Something went wrong. Please try again!"
        }, 400


@app.route('/<short>')
def show_url(short):
    url = Url.query.filter_by(short=short).first()

    if(url is None):
        # TODO render not found page
        return '', 404

    return redirect(url.raw)
