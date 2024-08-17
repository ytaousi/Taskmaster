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

        # Exit the loop if the command is 'exit' or 'quit'
        if command in ['exit', 'quit']:
            break

        # Check if the command is 'help'
        if command.startswith('help'):
            parts = command.split()
            if len(parts) == 1:
                supervisorclient.displayCommands()
            elif len(parts) == 2:
                supervisorclient.display_help(parts[1])
            else:
                print("*** Invalid help command")
        else:
            # Process other commands
            supervisorclient.display_help(command)

if __name__ == '__main__':
    main()
    