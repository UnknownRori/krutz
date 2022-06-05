from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import string
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['post'])
def store_url():
    raw = request.json['url']
    short = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    return {
        "message": "Successfully shortened url",
        "url": "/" + short
    }


@app.route('/<token>')
def show_url(token):
    return 'Redirect to...'
