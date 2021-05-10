from flask import Flask
from config import config


from apps.api import configure_api


def create_app(config_name: str) -> Flask:
    app = Flask('api-imdb-lookup')
    app.config.from_object(config[config_name])
    configure_api(app)

    return app
