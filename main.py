from supervisorctl import *
from supervisord import *
from multiprocessing import Process
import os


class Taskmaster(Process):
    def run(self):
        print('module name:', __name__)
        print('parent process:', os.getppid())
        print('process id:', os.getpid())
    def __init__(self, value):
        Process.__init__(self)
        self.value = value   

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    info('main line')
    process = Process(target=f, args=('bob',))
    process.start()
    process.join()