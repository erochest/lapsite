

from contextlib import closing
import sqlite3

from flask import g

import lapsite


def load_data():
    lapsite.app.logger.info('Loading data from %(DATA_FILE)s.' %
                            lapsite.app.config)

    cxn = g.db.connect()
    with closing(cxn):
        txn = cxn.begin()
        try:
            with open(lapsite.app.config['DATA_FILE']) as f:
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

    lapsite.app.logger.info('Done loading data.')


