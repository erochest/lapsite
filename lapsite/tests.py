

import os
import unittest
import tempfile

from flask import g

import lapsite
from lapsite import testing_config
from lapsite.database import load_data
from lapsite.models import (Community, FieldWorker, Informant, Project,
                            Response, Target, WorkSheet)


class DatabaseTestCase(unittest.TestCase):

    def setUp(self):
        (self.db_fd, self.db_file) = tempfile.mkstemp()

        app = lapsite.create_app('testing_config.py')
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
            assert g.session.query(Community).count() == 528
            assert g.session.query(FieldWorker).count() == 0
            assert g.session.query(Informant).count() == 1224
            assert g.session.query(Project).count() == 2
            assert g.session.query(Response).count() == 403879
            assert g.session.query(Target).count() == 1028
            assert g.session.query(WorkSheet).count() == 0


class ViewTestCase(unittest.TestCase):

    def setUp(self):
        pass

if __name__ == '__main__':
    unittest.main()

