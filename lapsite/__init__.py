

import os
import sys

from flask import Flask, g
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URI = 'sqlite:///tmp/lap.db'
LOG_FILE = '/tmp/lap.log'
DEBUG = False
TESTING = False
SECRET_KEY = 'development key'
ADMINS = []


def config_app(app, config_file):
    app.config.from_object(__name__)
    # One of dev_config.py, test_config.py, heroku_config.py, or
    # production_config.py.
    if 'LAP_SETTINGS' in os.environ:
        app.config.from_envvar('LAP_SETTINGS', silent=True)
    app.config.from_pyfile(config_file, silent=True)


def get_mail_handler(app):
    import logging
    from logging.handlers import SMTPHandler
    from logging import Formatter

    mail_handler = SMTPHandler('127.0.0.1',
                               'server-error@example.com',
                               ADMINS, 'Flaskr Failed')
    mail_handler.setLevel(logging.ERROR)
    mail_handler.setFormatter(Formatter('''
        Message type:   %(levelname)s
        Location:       %(pathname)s:%(lineno)d
        Module:         %(module)s
        Function:       %(funcName)s
        Time:           %(asctime)s

        Message:
        %(message)s
        '''))

    return mail_handler


def get_file_handler(app):
    import logging
    from logging.handlers import RotatingFileHandler
    from logging import Formatter

    file_handler = RotatingFileHandler(app.config['LOG_FILE'],
                                       maxBytes=2**20,
                                       backupCount=10)
    file_handler.setLevel(logging.WARN)
    file_handler.setFormatter(Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[%(pathname)s:%(lineno)d]'
        ))

    return file_handler


def create_app(config_file=None):
    global app

    if config_file is None:
        config_file = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                '%s_config.py' % (os.environ.get('LAPTARGET', 'prod'),),
                )

    app = Flask(__name__)
    config_app(app, config_file)

    if not app.debug:
        setup_logging(app)

    if 'lapsite.views' in sys.modules:
        reload(sys.modules['lapsite.views'])
    else:
        import lapsite.views

    set_request_handlers(app)

    return app


def connect_db(app):
    app.logger.info('Connecting to %(DATABASE_URI)s.' % app.config)
    return create_engine(app.config['DATABASE_URI'])


def setup_logging(app):
    import logging

    loggers = [
            app.logger,
            logging.getLogger('sqlalchemy'),
            ]
    handlers = [
            get_mail_handler(app),
            get_file_handler(app),
            ]

    # TODO: Perhaps set to write to STDERR for Heroku.
    for logger in loggers:
        for handler in handlers:
            logger.addHandler(handler)


def set_request_handlers(app):
    @app.before_request
    def before_request():
        g.db = connect_db(app)
        Session = sessionmaker(bind=g.db)
        g.session = Session()
    @app.teardown_request
    def teardown_request(exc):
        if exc is None:
            g.session.commit()
        else:
            g.session.rollback()

