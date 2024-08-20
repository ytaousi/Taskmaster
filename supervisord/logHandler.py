import logging
import logging.handlers
import os

class supervisorLogHandler:
    def __init__(self, args):
        self.args = args

    def setupHandlers(self):
        pass

    def initLogger(self):
        logging.basicConfig(format="%(levelname)s | %(asctime)s | %(message)s")
            


__all__ = ['supervisorLogHandler']