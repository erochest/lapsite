

import os
import unittest
import tempfile

from flask import g

import lapsite
from lapsite import testing_config
from lapsite.database import load_data
from lapsite.models import Community


class LapSiteTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['LAPTARGET'] = 'testing'
        (self.db_fd, self.db_file) = tempfile.mkstemp()

        app = lapsite.create_app()
        app.config['DATABASE_URI'] = 'sqlite:///' + self.db_file

        with app.test_client() as c:
            c.get('/')
            load_data()

    def tearDown(self):
        os.close(self.db_fd)
        os.remove(self.db_file)

    def test_db_loaded(self):
        with lapsite.app.test_client() as c:
            c.get('/')
            assert len(g.session.query(Community).all()) == 528


if __name__ == '__main__':
    unittest.main()

