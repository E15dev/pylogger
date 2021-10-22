import math
import time
from colors import *
import os

class logger:
    def __init__(self, logdir, realprint):
        global rp, lastlog, thislog
        lln = str(logdir) + 'lastlog.txt'
        lastlog = open(lln, 'w')
        lastlog.write(str(time.time()) + '\n')
        lastlog.close()
        lastlog = open(lln, 'a')
        tln = str(logdir) + str(time.time()) + '.txt'
        thislog = open(tln, 'w')
        thislog.write(str(time.time()) + '\n')
        thislog.close()
        thislog = open(tln, 'a')
        rp = realprint

    def log(self, c, text):
        global rp, lastlog, thislog
        t = str(time.time()) + ' | ' + c + str(text) + '\n'
        if rp:
            print(t, end='')
        lastlog.write(t)
        thislog.write(t)
        return 0

    def info(self, text):
        self.log(cinfo, str(text))
        return 0

    def warning(self, text):
        self.log(cwarning, str(text))
        return 0

    def error(self, text):
        self.log(cerror, str(text))
        return 0

    def fatal(self, text):
        self.log(cfatal, str(text))
        return 0


test = """
if __name__ == '__main__':
    llog = logger('../../logs/', True)
    llog.info('this is info test')
    llog.warning('this is warning test')
    llog.error('error test')
    llog.fatal('fatal test')
    """
