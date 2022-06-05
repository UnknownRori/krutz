from flask import render_template, redirect, request
from database.db import Url, UrlSchema
from router.router import app

class UriController:
    
    @app.route('/')
    def index():
        return render_template('index.html')


    @app.route('/', methods=['post'])
    def store():
        errors = UrlSchema().validate(request.json)

        if errors:
            return {
                'message': 'Failed to shorten url',
                'errors': errors
            }, 400

        try:
            url = Url.create(request.json['url'])

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
    def show(short):
        url = Url.find(short)

        if(url is None):
            return render_template('404.html'), 404

        return redirect(url.raw)