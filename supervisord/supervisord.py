import argparse
import sys
import os
from config import configFile
from logHandler import supervisorLogHandler
import socket

class my_supervisord:
    def __init__(self, args):
        self.config_file = configFile(args)
        #self.pid = subprocess.call(["lsof", "-t -i:9001 -sTCP:LISTEN"])

    def print_config(self):
        if self.config_file.is_valid:
            self.config_file.print_config()
        else:
            print("Invalid configuration file. Please fix the warnings and try again.")

    def getPid(self):
        os.getpid()

    def initPrograms(self):
        pass 

    def watchPrograms(self):

        self.collectLogs()
        pass

    def initServer(self):

        self.initPrograms()
        self.watchPrograms()
        pass

    def collectLogs(self):
        logHandler = supervisorLogHandler(self.config_file)
    
    def daemonize(self):
        # First fork to create a background process
        if os.fork() > 0:
            sys.exit(0)  # Exit parent process

        os.chdir('/')
        os.setsid()  # Create a new session
        os.umask(0)

        # Second fork to prevent the process from acquiring a controlling terminal
        if os.fork() > 0:
            sys.exit(0)  # Exit the second parent process

        # Redirect standard file descriptors to /dev/null
        sys.stdout.flush()
        sys.stderr.flush()
        with open('/dev/null', 'r') as devnull:
            os.dup2(devnull.fileno(), sys.stdin.fileno())
        with open('/dev/null', 'a+') as devnull:
            os.dup2(devnull.fileno(), sys.stdout.fileno())
            os.dup2(devnull.fileno(), sys.stderr.fileno())

def main():
    parser = argparse.ArgumentParser(description='Supervisord')
    default_config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config.ini')
    parser.add_argument('-c', '--config_file', type=str, default=default_config_path, help='Path to the configuration file')
    args = parser.parse_args()
    
    try:
        supervisor = my_supervisord(args)
        #supervisor.print_config()
        supervisor.initServer()
        
        
        #supervisor.daemonize()
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        sys.exit(1)

__all__ = ['my_supervisord']

if __name__ == '__main__':
    main()