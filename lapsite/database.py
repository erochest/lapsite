

from contextlib import closing
import sqlite3

from flask import g

import lapsite


def load_data():
    app = lapsite.app
    app.logger.info('Loading data from %(DATA_FILE)s.' % lapsite.app.config)

    cxn = g.db.connect() if hasattr(g, 'db') else lapsite.connect_db(app).connect()
    with closing(cxn):
        txn = cxn.begin()
        try:
            with app.open_resource(app.config['DATA_FILE']) as f:
                buffer = ''
                for line in f:
                    buffer += line

                    if sqlite3.complete_statement(buffer):
                        cxn.execute(buffer)
                        buffer = ''
            txn.commit()

        except:
            txn.rollback()
            raise

    app.logger.info('Done loading data.')


if __name__ == '__main__':
    app = lapsite.create_app()
    load_data()

