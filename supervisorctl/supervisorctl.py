import readline
from command import my_command

class my_supervisorctl:
    
    def __init__(self, args):
        self.args = args

    

def main():
    # Initialize readline for command history
    readline.parse_and_bind('tab: complete')
    readline.parse_and_bind('set editing-mode vi')
    readline.parse_and_bind('set keymap vi')
    readline.parse_and_bind('set history-size 1000')

    # Create a new instance of the class
    supervisorclient = my_supervisorctl(args=[])

    while True:
        # Prompt the user for a command
        command = input("supervisorctl> ").strip()

        # Initialize my_command with the input command and supervisorclient
        cmd = my_command(command)
        cmd.execute()

        # Exit the loop if the command is 'exit' or 'quit'
        if command in ['exit', 'quit']:
            break

if __name__ == '__main__':
    main()