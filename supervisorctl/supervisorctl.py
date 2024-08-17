import argparse
import subprocess


class my_supervisorctl:
    
    def __init__(self, name="", *args, **kwargs):
        self.name = name
        self.args = args
        self.kwargs = kwargs
    
    def displayCommands(self):
        print("Available commands:")
        print("  start <name>    Start a process")
        print("  stop <name>     Stop a process")
        print("  restart <name>  Restart a process")
        print("  shutdown        Stop all processes")
        print("  reload          Reload the configuration file")
        print("  quit            Exit the supervisorctl shell")
        print("  status          Show status of all processes")
        print("  help            Show the list of available commands")
        print("  exit            Exit the supervisorctl shell")
    
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
        print("Showing the list of available commands")
        self.displayCommands()
    
    def exit(self):
        print("Exiting the supervisorctl shell")

__all__ = ['my_supervisorctl']
