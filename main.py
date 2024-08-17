from supervisorctl import *
# from supervisord import *
# from multiprocessing import Process
import os

def main():
    # Create a new instance of the class
    supervisorclient = my_supervisorctl(args=[])

    while True:
        # Prompt the user for a command
        command = input("supervisorctl> ").strip()

        # Check if the command is 'help'
        if command.startswith('help'):
            parts = command.split()
            if len(parts) == 1:
                supervisorclient.displayCommands()
            elif len(parts) == 2:
                supervisorclient.display_help(parts[1])
            else:
                print("*** No help on {parts[1]}")
        else:
            # Exit the loop if the command is 'exit' or 'quit'
            if command in ['exit', 'quit']:
                break
            elif command.startswith('start'):
                parts = command.split()
                if len(parts) == 1:
                    print(f"Error: start requires a process name")
                    supervisorclient.display_help('start')
                else:
                    for process in parts[1:]:
                        supervisorclient.start(process)
            elif command.startswith('restart'):
                parts = command.split()
                if len(parts) == 1:
                    print(f"Error: restart requires a process name")
                    supervisorclient.display_help('restart')
                else:
                    for process in parts[1:]:
                        supervisorclient.restart(process)
            elif command == 'reload':
                supervisorclient.reload()
            elif command == 'shutdown':
                supervisorclient.shutdown()
            elif command.startswith('stop'):
                parts = command.split()
                if len(parts) == 1:
                    print(f"Error: stop requires a process name")
                    supervisorclient.display_help('stop')
                else:
                    for process in parts[1:]:
                        supervisorclient.stop(process)
            elif command == 'version':
                supervisorclient.version()
            elif command == 'status':
                supervisorclient.status()
            else:
                print(f"*** Unknown syntax: {command}")
if __name__ == '__main__':
    main()
    