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

    pids = [3356, 4489, 5567, 6678]
    pidStdFileLogs = {
        3356: ["program1name", "/home/normal-user/Desktop/Taskmaster/logs/program1name_stdout.log", "/home/normal-user/Desktop/Taskmaster/logs/program1name_stderr.log"],
        4489: ["program2name", "/home/normal-user/Desktop/Taskmaster/logs/program2name_stdout.log", "/home/normal-user/Desktop/Taskmaster/logs/program2name_stderr.log"],
        5567: ["program3name", "/home/normal-user/Desktop/Taskmaster/logs/program3name_stdout.log", "/home/normal-user/Desktop/Taskmaster/logs/program3name_stderr.log"],
        6678: ["program4name", "/home/normal-user/Desktop/Taskmaster/logs/programn4ame_stdout.log", "/home/normal-user/Desktop/Taskmaster/logs/program4name_stderr.log"],
    }

    log_types = ["supervisord", "program"]

    destionations = {
        "supervisord": [sys.stdout, sys.stderr],
        "program": [sys.stdout, sys.stderr],
    }

    supervisorloghandler = supervisorLogHandler(args=[
        pidStdFileLogs,
        pids,
        log_types,
        destionations,
    ])

    

if __name__ == '__main__':
    main()

