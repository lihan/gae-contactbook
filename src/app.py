from flask import Flask
from src import (
    addressbook,
    public,
)


def create_app(config_object):
    """An application factory
    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config_object)
    register_blueprints(app)

    return app


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(addressbook.views.blueprint)
    app.register_blueprint(public.views.blueprint)
    return None

