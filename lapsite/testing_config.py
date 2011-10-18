
import os
import tempfile

CWD = os.path.dirname(os.path.abspath(__file__))

DATA_FILE = 'sqlite3-data.sql'
DATABASE_URI = 'sqlite:////tmp/lap-testing.db'
DEBUG = True
TESTING = True
if os.path.exists(os.path.join(CWD, '.secret-key')):
    with open(os.path.join(CWD, '.secret-key')) as f:
        SECRET_KEY = f.readline().strip()
ADMINS = []

