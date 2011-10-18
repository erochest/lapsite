
import os

CWD = os.path.dirname(os.path.abspath(__file__))

DATABASE_URI = 'sqlite:///%s/lap.db' % (CWD,)
DATA_FILE = 'sqlite3-data.sql'
DEBUG = True
TESTING = False
if os.path.exists(os.path.join(CWD, '.secret-key')):
    with open(os.path.exists(os.path.join(CWD, '.secret-key'))) as f:
        SECRET_KEY = f.readline().strip()
ADMINS = ['erochest@gmail.com']

