from supervisorctl import *
# from supervisord import *
# from multiprocessing import Process
import os



# i need to test if my_supervisorctl class only is working whitout using my_supervisord in the code

if __name__ == '__main__':
    # Create a new instance of the class
    my_supervisorctl = my_supervisorctl()
    # Display the available commands
    my_supervisorctl.displayCommands()
    # Start a process
    my_supervisorctl.start("my_process")
    # Stop a process
    my_supervisorctl.stop("my_process")
    # Restart a process
    my_supervisorctl.restart("my_process")
    # Stop all processes
    my_supervisorctl.shutdown()
    # Reload the configuration file
    my_supervisorctl.reload()
    # Exit the supervisorctl shell
    my_supervisorctl.quit()
    # Show status of all processes
    my_supervisorctl.status()
    # Show the list of available commands
    my_supervisorctl.help()
    # Exit the supervisorctl shell
    my_supervisorctl.exit()
    
    