from database.db import db
import string
import random

# Url model
class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    raw = db.Column(db.String, nullable=False)
    short = db.Column(db.String, unique=True, nullable=False)

    # Create new Url and store it to database
    def create(url):
        raw = url
        short = ''.join(
            random.choices(string.ascii_letters + string.digits, k=6)
        )
        
        url = Url(raw=raw, short=short)
        
        db.session.add(url)
        db.session.commit()
        
        return url

    # Find url using short url version
    def find(short):
        return Url.query.filter_by(short=short).first()