from crypt import methods
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['post'])
def store_url():
    url = request.json['url']
    return "Shorten the url to"


@app.route('/<token>')
def show_url(token):
    return 'Redirect to...'
