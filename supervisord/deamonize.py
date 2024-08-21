from multiprocessing import Process
from multiprocessing import current_process
from logHandler import supervisorLogHandler
import os
import sys
import logging
import time


def daemonize():
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

    # Test the daemon with a loop that logs a message every few seconds
    while True:
        logging.info("Daemon is running...")
        time.sleep(5)  # Sleep for a bit before logging again

if __name__ == "__main__":
    # demonize the process to run in the background
    # daemonize()
    main()