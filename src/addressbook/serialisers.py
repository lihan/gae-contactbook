from google.appengine.ext import ndb

from marshmallow import (
    fields,
    ValidationError,
)
from marshmallow import Schema
from src.addressbook.models import Contact


def _validate_unique_email(email):
    key = ndb.Key(Contact, email)
    contact = key.get()
    if contact:
        # Record exist, raise
        raise ValidationError('Email (%s) exists in database' % email)


class ContactSchema(Schema):
    first_name = fields.Str()
    last_name = fields.Str()
    email = fields.Email(validate=_validate_unique_email)
