from threading import current_thread
from multiprocessing import active_children
from multiprocessing import managers
from multiprocessing.managers import BaseManager
from multiprocessing import current_process
from multiprocessing import Process
import os

class CustomManager(BaseManager):
    # nothing
    pass

class CustomClass():
    # constructor
    def __init__(self):
        # get the current process and thread
        process = current_process()
        thread = current_thread()
        # report details
        print(f'Constructor:\n {thread}\n {process}')
 
    # do something with the data
    def task(self):
        # get the current process and thread
        process = current_process()
        thread = current_thread()
        # report details
        print(f'Task:\n {thread}\n {process}')
    
    def printProcs(self):
        for child in active_children():
            print(f"{child}\n")



# protect the entry point
if __name__ == '__main__':
    pass
