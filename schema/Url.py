from marshmallow import fields
from database.db import ma

class UrlSchema(ma.Schema):
    url = fields.Url(required=True)