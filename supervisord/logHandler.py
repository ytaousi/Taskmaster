import logging
import logging.handlers
import os
import smtplib

class supervisorLogHandler:
    def __init__(self, args):
        self.args = args
        self.loggingConfig = {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'verbose': {
                    'format': '%(asctime)s | %(levelname)s | %(message)s | %(pid)s | %(module)s | %(process)d | %(thread)d'
                },
            },
            'handlers': {
                'file': {
                    'level': 'INFO',
                    'class': 'logging.FileHandler',
                    'filename': os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs/supervisor.log'),
                    'formatter': 'verbose'
                },
                'stdout': {
                    'level': 'INFO',
                    'class': 'logging.StreamHandler',
                    'formatter': 'verbose'
                },
                'stderr': {
                    'level': 'ERROR',
                    'class': 'logging.StreamHandler',
                    'formatter': 'verbose'
                },
                'mail': {
                    'level': 'ERROR',
                    'class': 'logging.handlers.SMTPHandler',
                    'mailhost': 'smtp.gmail.com',
                    'fromaddr': 'yassir_ta@hotmail.com',
                    'toaddrs': 'yassir.taous@gmail.com',
                    'subject': 'Test mail from email handler',
                    'credentials': ('', ''),
                    'secure': None,
                },
            },
            'loggers': {
                'supervisor logger': {
                    'handlers': ['file', 'stdout', 'stderr', 'mail'],
                    'level': 'INFO',
                    'propagate': True,
                },
            },
            'filters': {},
            'adapter': {},
        }

        self.name = "supervisord log handler"
        self.loger = logging.getLogger("supervisor logger")
        self.loger.setLevel(logging.INFO)
        self.formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(filename)s | %(message)s | %(pid)s')
        self.logerAdapter = logging.LoggerAdapter(self.loger, {'pid': os.getpid()})
        self.setupHandlers()

    def initFileHandler(self):
        self.handler = logging.FileHandler(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs/supervisor.log'))
        self.handler.setFormatter(self.formatter)
        self.loger.addHandler(self.handler)

    def initStdoutHandler(self):
        self.handler = logging.StreamHandler()
        self.handler.setFormatter(self.formatter)
        self.handler.setLevel(logging.INFO)
        self.loger.addHandler(self.handler)
    
    def initStderrHandler(self):
        self.handler = logging.StreamHandler()
        self.handler.setFormatter(self.formatter)
        self.handler.setLevel(logging.ERROR)
        self.loger.addHandler(self.handler)
    
    def initEmailHandler(self):
        self.handler = logging.handlers.SMTPHandler(mailhost=('smtp.gmail.com', 587),
                                                    fromaddr='yassir_ta@hotmail.com',
                                                    toaddrs='yassir.taous@gmail.com',
                                                    subject='Test mail from email handler',
                                                    credentials=('', ''),
                                                    secure=None)
        self.handler.setLevel(logging.CRITICAL)
        self.handler.setFormatter(self.formatter)
        self.loger.addHandler(self.handler)

    def sendEmailNotification(self):
        
        pass

    def initSyslogHandler(self):
        pass

    def inithttpHandler(self):
        pass
    
    def collectSupervisorLogs(self):
        pass

    def collectProgramLogs(self):
        pass

    def writeSupervisorLogs(self):
        pass

    def writeProgramLogs(self):
        self.writeErrorLogs()
        self.writeOutputLogs()
        pass

    def writeErrorLogs(self):
        pass

    def writeOutputLogs(self):
        pass

    def setupHandlers(self):
        self.initFileHandler()
        # self.initStdoutHandler()
        # self.initStderrHandler()
        self.initEmailHandler()
        


def main():

    supervisorloghandler = supervisorLogHandler(args=[])

    try:
        i = 0
        while i < 10:
            print("This is normal behavior of logged program")
            i += 1
    except Exception as e:
        supervisorloghandler.loger.error("This is an error message", exception=e)

__all__ = ['supervisorLogHandler']




if __name__ == "__main__":
    main()