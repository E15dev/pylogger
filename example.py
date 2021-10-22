import logger

l = logger.log('./logs/', False)
l.info('this is info test')
l.warning('this is warning test')
l.error('error test')
l.fatal('fatal test')
