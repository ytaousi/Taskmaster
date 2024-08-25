import socket
import sys
import os
import multiprocessing as Process
import socket



class Server:

    def __init__(self, args):
        self.args = args
        self.pids = {
            "program1": 3356,
            "program2": 4489,
            "program3": 5567,
            "program4": 6678
        }
        # {[]: 0, []: 1,}
        self.numberProcessPerProgram = {}
        
        # {"event": 0, "event": 1,}
        self.eventsQueue = {}
        self.shutdownEvent = False
        pass

        def startServer(self):
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.bind(("localhost", 9001))
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.settimeout(800)
            self.socket.listen(5)

            # while True:
            #     try:
            #         pass
            #     except socket.timeout:
            #         print("Socket timeout")
            #         break
        def shutdownServer(self):
            self.socket.close()

        def exec_fork(self, numberProcessPerProgram, ):
            supervisorPid = os.fork()
            if supervisorPid == 0:
                print("Child process")
                pass

                os._exit(0)
            else:
                

                os.waitpid(supervisorPid, 0)
                print("Child process finished")
                os._exit(0)
        pass


def main():
    pass


if __name__ == '__main__':
    main()