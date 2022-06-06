from app import app, limiter
from controller.Uri import *

@app.errorhandler(429)
def ratelimit_handler(e):
    return {
        "message": "Too many request, please wait a little longer",
        "errors": True
    }, 429
