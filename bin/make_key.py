#!/usr/bin/env python


"""\
This generates a secret key file in the file lapsite/.secret-key.
"""


import os
import random


CWD = os.path.dirname(os.path.abspath(__file__))

key_file = os.path.join(CWD, '..', 'lapsite', '.secret-key')
print 'writing to', key_file

with open(key_file, 'w') as f:
    f.write(os.urandom(24))

