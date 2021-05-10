from logging import info
from apps.movies import lookup_blueprint, init_lookup_blueprint

def configure_api(app):
    info('configuring blueprints...')
    init_lookup_blueprint()
    app.register_blueprint(lookup_blueprint, url_prefix='/api/movies')
    app.url_map.strict_slashes = False
    info(app.url_map)
