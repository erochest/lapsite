
import os

CWD = os.path.dirname(os.path.abspath(__file__))

DATABASE_URI = 'sqlite:///%s/lap.db' % (CWD,)
DATA_FILE = 'sqlite3-data.sql'
DEBUG = True
TESTING = False
SECRET_KEY = '&\x1d7\xaa\xa7+\xc8A\xff\x99\x00\\\xc0\x92\xfc\xbe\xf9\x9eC,w\x86\xec\xc8'
ADMINS = ['erochest@gmail.com']

