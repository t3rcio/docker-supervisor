
import sys
import os
from datetime import datetime
import time

while True:
    with open('out2.log', 'a') as logfile:
        content = '{} {}\n'.format(datetime.now(), 'WORKER_2')
        logfile.write(content)
        time.sleep(10)
