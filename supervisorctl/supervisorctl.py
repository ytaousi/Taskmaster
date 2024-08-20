import readline
import subprocess
from command import my_command
import signal
import os

class my_supervisorctl:
    
    def __init__(self, args):
        self.args = args
        self.command = my_command
        self.signals = {
            "SIGHUP": "Hangup",
            "SIGTERM": "Terminate",
            "SIGINT": "Interrupt",
            "SIGUSR2": "User-defined signal 2",
            "SIGQUIT": "Quit"
        }
        #self.pid = 

    def execute_command(self, command):
        cmd = self.command(command)
        cmd.execute()
    
    def send_signal(self, signal, frame):
        print(f"Caught signal {signal} ({self.signals[signal]})")
        if signal == signal.SIGQUIT:
            print("Sending SIGQUIT to the server")
            os.kill(os.getpid(), signal.SIGQUIT)
        if signal == signal.SIGTERM:
            print("Sending SIGTERM to the server")
            os.kill(os.getpid(), signal.SIGTERM)
        if signal == signal.SIGINT:
            print("Sending SIGINT to the server")
            os.kill(os.getpid(), signal.SIGINT)
        if signal == signal.SIGUSR2:
            print("Sending SIGUSR2 to the server")
            os.kill(os.getpid(), signal.SIGUSR2)
        if signal == signal.SIGHUP:
            print("Sending SIGHUP to the server")
            os.kill(os.getpid(), signal.SIGHUP)


def main():
    # Initialize readline for command history
    readline.parse_and_bind('tab: complete')
    readline.parse_and_bind('set editing-mode vi')
    readline.parse_and_bind('set keymap vi')
    readline.parse_and_bind('set history-size 1000')

    # Create a new instance of the class
    supervisorclient = my_supervisorctl(args=[])
    try :
        while True:
            # Prompt the user for a command
            command = input("supervisorctl> ").strip()

            # Execute the command using the supervisorclient
            supervisorclient.execute_command(command)
    except KeyboardInterrupt:
        exit(0)
    except EOFError:
        exit(0)
        

if __name__ == '__main__':
    main()