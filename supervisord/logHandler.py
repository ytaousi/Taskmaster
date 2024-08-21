import logging
import logging.handlers
import os

class supervisorLogHandler:
    def __init__(self, args):
        self.args = args

    def initFileLogger(self):
        self.loger = logging.getLogger("supervisor log file")
        self.loger.name = "supervisord file logger"
        self.loger.setLevel(logging.INFO)
        self.formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

        self.handler = logging.FileHandler(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs/supervisor.log'))
        self.handler.setFormatter(self.formatter)
        self.loger.addHandler(self.handler)

    def initStreamLogger(self):
        self.loger = logging.getLogger("supervisor log stream")
        self.loger.name = "supervisord stream logger"
        self.loger.setLevel(logging.INFO)
        self.formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

        self.handler = logging.StreamHandler()
        self.handler.setFormatter(self.formatter)
        self.loger.addHandler(self.handler)
    
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
        self.initFileLogger()
        self.initStreamLogger()
        


def main():

    supervisorloghandler = supervisorLogHandler(args=[])
    

    i = 0
    while i < 10:
        supervisorloghandler.loger.warning(f'This is a log entry from {supervisorloghandler.loger.name}')
        i += 1


__all__ = ['supervisorLogHandler']




if __name__ == "__main__":
    main()