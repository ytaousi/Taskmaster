# only standard libraries are used to build the supervisord logging management system.
import sys
import os

class supervisorLogHandler:
    def __init__(self, args):
        self.args = args
        self.supervisorLogFilePath = ""

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


def main():
    supervisorloghandler = supervisorLogHandler(args=[
        "This is a test argument",
        "This is a seconf test argument",
        "This is a third test argument",
        "This is a fourth test argument",
    ])


if __name__ == '__main__':
    main()

