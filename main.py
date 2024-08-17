from supervisorctl import *
# from supervisord import *
# from multiprocessing import Process
import os



# i need to test if my_supervisorctl class only is working whitout using my_supervisord in the code

if __name__ == '__main__':
    # Create a new instance of the class
    supervisorclient = my_supervisorctl(args=[])
    # Display the available commands
    # supervisorclient.displayCommands()
    # Display the help message for specific command
    supervisorclient.display_help("shutdown")
    