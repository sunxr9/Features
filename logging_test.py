# -*- encoding: utf-8 -*-

# import re
# import logging
# from logging.handlers import TimedRotatingFileHandler
# from logging.handlers import RotatingFileHandler
#
# log_fmt = '%(asctime)s %(levelname) %(message)s'
# formatter = logging.Formatter(log_fmt)
#
# log_file_handler = TimedRotatingFileHandler(filename='test.log', when='D', interval=1, backupCount=7)
# # log_file_handler.suffix = '%Y-%m-%d.log'
# # log_file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.log$")
# log_file_handler.setFormatter(formatter)
# logging.basicConfig(level=logging.INFO)
#
# log = logging.getLogger()
#
# log.addHandler(log_file_handler)
# log.removeHandler(log_file_handler)
#
# if __name__ == '__main__':
#     for i in range(100):
#         logging.info('start')
#         logging.warning('warning test')
#         logging.debug('debug ')
#         print(i)


import logging
import time
from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler

def create_rotating_log(path):
    logger = logging.getLogger('Rotating log')
    logger.setLevel(logging.INFO)

    # handler = RotatingFileHandler(path, maxBytes=20, backupCount=5)
    handler = TimedRotatingFileHandler(path, when='M', interval=1, backupCount=5)
    logger.addHandler(handler)

    for i in range(100):
        logger.info('This is test log {0}'.format(i))
        time.sleep(2)
        print(i)



if __name__ == '__main__':
    create_rotating_log('test.log')
