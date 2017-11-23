from google.appengine.ext import ndb


class Contact(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    email = ndb.StringProperty(required=True)

    @classmethod
    def ndb_key(cls, email):
        return ndb.Key(Contact, email)

    @classmethod
    def create(cls, first_name='', last_name='', email=''):
        key = Contact.ndb_key(email)
        return Contact(
            key=key,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
