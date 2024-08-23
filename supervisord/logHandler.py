# only standard libraries are used to build the supervisord logging management system.
import sys
import os
import time

class supervisorLogHandler:
    def __init__(self, args):
        self.args = args
        self.supervisorLogFilePath = "/home/normal-user/Desktop/Taskmaster/logs/supervisord_test.log"
        self.destinations = {}

    def print_config(self):
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

    def add_destionation(self, log_type, destination):
        if log_type not in self.destionations:
            self.destionations[log_type] = []
        self.destionations[log_type].append(destination)

    def logsFormatter(self, message, log_type="supervisord", level="INFO"):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        formattedMessage = f"{timestamp} [{level}] {message}"
        if log_type in self.destionations:
            for dest in self.destionations[log_type]:
                dest.write(formattedMessage)

def main():
    supervisorloghandler = supervisorLogHandler(args=[
        "This is a test argument",
        "This is a seconf test argument",
        "This is a third test argument",
        "This is a fourth test argument",
    ])


if __name__ == '__main__':
    main()

