class my_command:
    def __init__(self, name):
        self.name = name
        self.help_messages = {
            "quit": "quit    Exit the supervisor shell.",
            "exit": "exit    Exit the supervisor shell.",
            "status": (
                "status <name>           Get status for a single process\n"
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
                "restart <name> <name>   Restart multiple processes or groups\n"
                "restart all             Restart all processes\n"
                "Note: restart does not reread config files. For that, see reread and update."
            ),
            "stop": (
                "stop <name>             Stop a process\n"
                "stop <name> <name>      Stop multiple processes or groups\n"
                "stop all                Stop all processes"
            ),
            "start": (
                "start <name>            Start a process\n"
                "start <name> <name>     Start multiple processes or groups\n"
                "start all               Start all processes"
            ),
            "version": "version         Show the version of the remote supervisord process"
        }

    def execute(self):
        if self.name == 'quit':
            self.quit()
        elif self.name == 'exit':
            self.exit()
        elif self.name == 'version':
            self.version()
        elif self.name.startswith('start'):
            parts = self.name.split()
            if len(parts) == 1:
                print(f"Error: start requires a process name")
                self.display_help('start')
            else:
                for process in parts[1:]:
                    self.start(process)
        elif self.name.startswith('restart'):
            parts = self.name.split()
            if len(parts) == 1:
                print(f"Error: restart requires a process name")
                self.display_help('restart')
            else:
                for process in parts[1:]:
                    self.restart(process)
        elif self.name == 'reload':
            self.reload()
        elif self.name == 'shutdown':
            self.shutdown()
        elif self.name.startswith('stop'):
            parts = self.name.split()
            if len(parts) == 1:
                print(f"Error: stop requires a process name")
                self.display_help('stop')
            else:
                for process in parts[1:]:
                    self.stop(process)
        elif self.name == 'status':
            self.status()
        elif self.name.startswith('help'):
            parts = self.name.split()
            if len(parts) == 1:
                self.displayCommands()
            elif len(parts) == 2:
                self.display_help(parts[1])
            else:
                print(f"*** No help on {parts[1]}")
        else:
            print(f"*** Unknown syntax: {self.name}")

    def quit(self):
        print("Exiting the supervisorctl shell")

    def exit(self):
        print("Exiting the supervisorctl shell")
    
    def version(self):
        print("My supervisorctl version Gheyerha.1.0.0")

    def start(self, process):
        print(f"Starting process: {process}")
    
    def stop(self, process):
        print(f"Stopping process: {process}")
    
    def restart(self, process):
        print(f"Restarting process: {process}")
    
    def shutdown(self):
        confirmation = input("Really shut the remote supervisord process down y/N? ").strip().lower()
        if confirmation == 'y':
            try:
                print("Remote supervisord process has been shut down.")
            except Exception as e:
                print(f"Failed to shut down the remote supervisord process: {e}")

    def reload(self):
        confirmation = input("Really restart the remote supervisord process y/N? ").strip().lower()
        if confirmation == 'y':
            try:
                print("Remote supervisord process has been restarted.")
            except Exception as e:
                print(f"Failed to restart the remote supervisord process: {e}")
    
    def status(self):
        print("Showing status of all processes")
     
    def help(self):
        self.displayCommands()

    def displayCommands(self):
        print("default commands (type help <topic>):")
        print("=====================================")
        print("start     exit    reload  restart")
        print("shutdown  status  stop    quit")
        print("version   help")

    def display_help(self, command=None):
        if command:
            if command in self.help_messages:
                print(self.help_messages[command])
            else:
                print(f"*** No help on {command}")
        else:
            self.displayCommands()