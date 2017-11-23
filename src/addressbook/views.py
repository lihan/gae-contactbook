from google.appengine.ext import ndb
from flask import (
    Blueprint,
    render_template,
)
from flask import request
from src.addressbook.models import Contact
from src.addressbook.serialisers import ContactSchema
from flask import jsonify
import csv


blueprint = Blueprint(
    'address_book',
    __name__,
    url_prefix='/address_book',
    static_folder='static',
    template_folder='templates'
)


@blueprint.route('/', methods=['GET'])
def address_book_home_handler():
    conatcts_query = Contact.query()
    return render_template('addressbook_home.html', contacts=conatcts_query)


@blueprint.route('/api/import_csv/', methods=['POST'])
@ndb.transactional(xg=True)
def import_csv_handler():
    """
    The API that imports or rejects the uploaded CSV
    """
    uploaded_csv = request.files['csv_file']
    allow_override = request.form.get('allow_override', None)

    schema = ContactSchema(many=True)
    reader = csv.DictReader(
        uploaded_csv.readlines(),
        fieldnames=['first_name', 'last_name', 'email'])
    contacts_list = list(reader)[1:]       # Skip CSV Header
    _contacts, _validation_errs = schema.load(contacts_list)

    if _validation_errs:
        if not allow_override:
            return jsonify({
                'status': 'error',
                'errors': map(lambda e: e['email'][0], _validation_errs.values())
            }), 400
        else:
            duplicated_emails = map(lambda x: contacts_list[x]['email'], _validation_errs.keys())
            ndb.delete_multi(Contact.ndb_key(x) for x in duplicated_emails)

    contacts_entries = [Contact.create(**c) for c in contacts_list]
    created_contacts = ndb.put_multi(contacts_entries)

    return jsonify({
        'status': 'ok',
        'created': len(created_contacts)
    })
