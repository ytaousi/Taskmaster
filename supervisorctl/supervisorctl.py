import argparse
import subprocess


class my_supervisorctl:
    
    def __init__(self, args):
        self.args = args
        self.help_messages = {
            "quit": "quit    Exit the supervisor shell.",
            "exit": "exit    Exit the supervisor shell.",
            "status": (
                "status <name>           Get status for a single process\n"
                "status <gname>:*        Get status for all processes in a group\n"
                "status <name> <name>    Get status for multiple named processes\n"
                "status                  Get all process status info"
            ),
            "help": (
                "help            Print a list of available actions\n"
                "help <action>   Print help for <action>"
            ),
            "reload": "reload          Restart the remote supervisord.",
            "shutdown": "shutdown        Shut the remote supervisord down.",
            "restart": (
                "restart <name>          Restart a process\n"
                "restart <gname>:*       Restart all processes in a group\n"
                "restart <name> <name>   Restart multiple processes or groups\n"
                "restart all             Restart all processes\n"
                "Note: restart does not reread config files. For that, see reread and update."
            ),
            "stop": (
                "stop <name>             Stop a process\n"
                "stop <gname>:*          Stop all processes in a group\n"
                "stop <name> <name>      Stop multiple processes or groups\n"
                "stop all                Stop all processes"
            ),
            "start": (
                "start <name>            Start a process\n"
                "start <gname>:*         Start all processes in a group\n"
                "start <name> <name>     Start multiple processes or groups\n"
                "start all               Start all processes"
            )
        }
    def display_help(self, command=None):
        if command:
            if command in self.help_messages:
                print(self.help_messages[command])
            else:
                print(f"*** No help on {command}")
        else:
            self.displayCommands()
    
    def displayCommands(self):
        print("default commands (type help <topic>):")
        print("=====================================")
        print("start     exit    reload  restart")
        print("shutdown  status  stop    quit")
        print("version   help")
    
    def start(self, name):
        print("Starting process: " + name)
    
    def stop(self, name):
        print("Stopping process: " + name)
    
    def restart(self, name):
        print("Restarting process: " + name)
    
    def shutdown(self):
        print("Stopping all processes")
    
    def reload(self):
        print("Reloading the configuration file")
    
    def quit(self):
        print("Exiting the supervisorctl shell")
    
    def status(self):
        print("Showing status of all processes")
     
    def help(self):
        self.displayCommands()
    
    def exit(self):
        print("Exiting the supervisorctl shell")

__all__ = ['my_supervisorctl']
