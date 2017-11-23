from src.settings import DevConfig, ProdConfig

from flask.helpers import get_debug_flag
from src.app import create_app

config = DevConfig if get_debug_flag() else ProdConfig

app = create_app(config)
