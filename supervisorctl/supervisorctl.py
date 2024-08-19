import readline
from command import my_command
from supervisord import my_supervisord
import subprocess

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

    def execute_command(self, command):
        cmd = self.command(command)
        cmd.execute()
    
    def send_signal(self, signal, supervisord_pid):
        if signal in self.signals:
            if signal == "SIGUSR2":
                subprocess.call(["echo", "sending SIGUSR2"]) #str(supervisord_pid)
            if signal == "SIGQUIT":
                subprocess.call(["echo", "sending SIGQUIT"])
            if signal == "SIGTERM":
                subprocess.call(["echo", "sending SIGTERM"])
            if signal == "SIGHUP":
                subprocess.call(["echo", "sending SIGHUP"])
            if signal == "SIGINT":
                subprocess.call(["echo", "sending SIGINT"])
        else:
            print(f"Unknown signal {signal}")

def main():
    # Initialize readline for command history
    readline.parse_and_bind('tab: complete')
    readline.parse_and_bind('set editing-mode vi')
    readline.parse_and_bind('set keymap vi')
    readline.parse_and_bind('set history-size 1000')

    # Create a new instance of the class
    supervisorclient = my_supervisorctl(args=[])
    # Get the PID of the supervisord process
    supervisord_pid = my_supervisord(args=[])
    
    supervisorclient.send_signal("SIGUSR2", supervisord_pid.getPid())
    while True:
        # Prompt the user for a command
        command = input("supervisorctl> ").strip()

        # Execute the command using the supervisorclient
        supervisorclient.execute_command(command)
        
        

if __name__ == '__main__':
    main()