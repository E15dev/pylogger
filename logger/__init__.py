import time


black = '§0'
dark_blue = '§1'
dark_green = '§2'
dark_aqua = '§3'
dark_red = '§4'
dark_magenta = '§5'
gold = '§6'
silver = '§7'
gray = '§8'
blue = '§9'
green = '§a'
aqua = '§b'
red = '§c'
pink = '§d'
gold = '§e'
white = '§f'

cinfo = silver
cwarning = dark_magenta
cerror = dark_red
cfatal = red

version = "2.0"


class logger:
    def __init__(self, logdir, realprint):
        global rp, lastlog, thislog
        # last log
        lln = str(logdir) + 'lastlog.txt'
        lastlog = open(lln, 'w', encoding="utf-8")
        lastlog.write(str(time.time()) + '\n')
        lastlog.close()
        lastlog = open(lln, 'a', encoding="utf-8")
        # this log
        tln = str(logdir) + str(time.time()) + '.txt'
        thislog = open(tln, 'w', encoding="utf-8")
        thislog.write(str(time.time()) + '\n')
        thislog.close()
        thislog = open(tln, 'a', encoding="utf-8")
        rp = realprint
        self.info("logging with logger version : {0]".format(version))

    def log(self, c, text, level):
        global rp, lastlog, thislog
        t = str(time.time()) + ' | ' + level + ' | ' + c + str(text) + '\n'
        if rp:
            print(t, end='')
        lastlog.write(t)
        thislog.write(t)
        lastlog.flush()
        thislog.flush()
        return 0

    def info(self, text, ):
        self.log(cinfo, str(text), level="info")
        return 0

    def warning(self, text):
        self.log(cwarning, str(text), level="warning")
        return 0

    def error(self, text):
        self.log(cerror, str(text), level="error")
        return 0

    def fatal(self, text):
        self.log(cfatal, str(text), level="fatal")
        return 0

    def end(self, exitcode):
        if exitcode == 0:
            self.info(f'game end with exit code {str(exitcode)}')
        else:
            self.fatal(f'game end with invalid exit code {str(exitcode)}')
        exit(exitcode)
        return 0


test = """
if __name__ == '__main__':
    llog = logger('../../logs/', True)
    llog.info('this is info test')
    llog.warning('this is warning test')
    llog.error('error test')
    llog.fatal('fatal test')
    """
