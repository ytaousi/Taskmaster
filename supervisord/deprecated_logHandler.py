import logging
import logging.handlers
import os
import json

class supervisorLogHandler:
    def __init__(self, args):
        self.args = args
        self.loggingConfig = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config.json')).read()

        self.name = "supervisord log handler"
        self.rootLoger = logging.getLogger("supervisor logger")
        self.rootLoger.setLevel(logging.INFO)
        self.rootFormatter = logging.Formatter('%(asctime)s | %(levelname)s | %(filename)s | %(message)s | %(pid)s')
        self.logerAdapter = logging.LoggerAdapter(self.rootLoger, {'pid': os.getpid()})
        self.setupHandlers()

    def initFileHandler(self):
        self.handler = logging.FileHandler(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs/supervisor.log'))
        self.handler.setFormatter(self.rootFormatter)
        self.rootLoger.addHandler(self.handler)

    def initStdoutFilehandler(self):
        self.handler = logging.StreamHandler()
        self.handler.setFormatter(self.rootFormatter)
        self.handler.setLevel(logging.INFO)
        self.rootLoger.addHandler(self.handler)
    
    def initStderrFileHandler(self):
        self.handler = logging.StreamHandler()
        self.handler.setLevel(logging.ERROR)
        self.handler.setFormatter(self.rootFormatter)
        self.rootLoger.addHandler(self.handler)
    
    def initEmailHandler(self):
        self.handler = logging.handlers.SMTPHandler(mailhost=('smtp.gmail.com', 587),
                                                    fromaddr='yassir_ta@hotmail.com',
                                                    toaddrs='yassir.taous@gmail.com',
                                                    subject='Test mail from email handler',
                                                    credentials=('', ''),
                                                    secure=None)
        self.handler.setLevel(logging.CRITICAL)
        self.handler.setFormatter(self.rootFormatter)
        self.rootLoger.addHandler(self.handler)

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
        self.writeStdErrorLogs()
        self.writeStdOutLogs()
        pass

    def writeStdErrorLogs(self):
        pass

    def writeStdOutLogs(self):
        pass

    def setupHandlers(self):
        self.initFileHandler()
        # self.initStdoutFilehandler()
        # self.initStderrFileHandler()
        self.initEmailHandler()
        


def main():

    supervisorloghandler = supervisorLogHandler(args=[])

    try:
        i = 0
        while i < 10:
            print("This is normal behavior of logged program")
            i += 1
    except Exception as e:
        supervisorloghandler.rootLoger.error("This is an error message", exception=e)

__all__ = ['supervisorLogHandler']




if __name__ == "__main__":
    main()