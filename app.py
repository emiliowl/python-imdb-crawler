from logging import info, warn, root, INFO
from os import getenv
from os.path import dirname, isfile, join
from dotenv import load_dotenv

root.setLevel(level=INFO)

_ENV_FILE = join(dirname(__file__), '.env-development') # play here if you want to work in multiple envs

if isfile(_ENV_FILE):
    info(f'loading dotenv from file {_ENV_FILE}')
    load_dotenv(dotenv_path=_ENV_FILE)
else:
    warn(f'failed loading dotenv from file {_ENV_FILE}')

from apps import create_app
app = create_app(getenv('FLASK_ENV') or 'default')


if __name__ == '__main__':
    ip = '127.0.0.1'
    port = app.config['APP_PORT']
    debug = app.config['DEBUG']

    app.run(host=ip, debug=debug, port=port, use_reloader=debug)
