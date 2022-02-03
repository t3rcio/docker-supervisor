
import sys
import os
from datetime import datetime
import time

while True:
    with open('out1.log', 'a') as logfile:
        content = '{} {}\n'.format(datetime.now(), 'WORKER_1')
        logfile.write(content)
        time.sleep(10)
