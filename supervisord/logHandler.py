import logging
import logging.handlers
import os

class supervisorLogHandler:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.handler = logging.handlers.WatchedFileHandler(os.environ.get("LOGFILE", "/home/normal-user/Desktop/42-projects/Taskmaster/supervisord/supervisord_test.log"))
        self.logger.addHandler(self.handler)

    def log(self, message):
        self.logger.info(message)



__all__ = ['supervisorLogHandler']