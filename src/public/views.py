from flask import (
    Blueprint,
    redirect)


blueprint = Blueprint(
    'public',
    __name__,
    url_prefix='/',
)


@blueprint.route('/', methods=['GET'])
def homepage_redirect_view():
    return redirect("/address_book", code=302)
