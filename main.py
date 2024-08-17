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
            elif command == 'start':
                supervisorclient.start()
            elif command == 'restart':
                supervisorclient.restart()
            elif command == 'reload':
                supervisorclient.reload()
            elif command == 'shutdown':
                supervisorclient.shutdown()
            elif command == 'stop':
                supervisorclient.stop()
            elif command == 'version':
                supervisorclient.version()
            elif command == 'status':
                supervisorclient.status()
            else:
                print(f"*** Unknown syntax: {command}")
if __name__ == '__main__':
    main()
    